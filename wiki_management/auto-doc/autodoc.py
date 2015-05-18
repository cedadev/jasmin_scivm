import os
import re
import sys
import time
from pkg_resources import parse_version

import config
import commands

"""
Produces automatic documentation of RPMs for use on wiki documenting
jasmin science VMs.  See http://proj.badc.rl.ac.uk/cedaservices/ticket/34


Usage: 
   customise config.py as required, and then

   python autodoc.py <filename>
"""


def get_output(command):
    """
    get output of a command, or raise exception if unsuccessful
    """
    status, output = commands.getstatusoutput("%s 2>&1" % command)
    if status != 0:
        raise Exception("command %s returned %s; output follows:\n------\n%s\n------" % (command, status, output))
    return output


class LocalRPMS(object):
    """
    A class representing a set of local directories that contain RPMs.
    In particular it provides the rpm_path method, which looks up the path
    of the lastest version of a given RPM in these directories.
    """

    def __init__(self, dir_list, debug=False):
        self.dir_list = dir_list
        self.packages = {}
        self._re_match = re.compile(r"([^\s]+)-([^\s-]+)-([^\s-]+)\.([^\s\.-]+)\.rpm").match
        self.debug = debug
        self._scan_dirs()
    
    def _scan_dirs(self):
        """
        Build up a dictionary (self.packages) of the latest versions of each 
        RPM found in the local directories.  The keys are the package names,
        and the values are dictionaries containing the version and the path.
        """
        for dir_name in self.dir_list:
            for file_name in os.listdir(dir_name):
                m = self._re_match(file_name)
                if not m:
                    continue
                name = m.group(1)
                version = m.group(2)
                release = m.group(3)
                # arch = m.group(4)
                parsed_version = parse_version(version)
                parsed_release = parse_version(release)
                if self.debug:
                    print "considering name=%s version=%s release=%s:" % (name, version, release)
                if (name not in self.packages
                    or ((parsed_version, parsed_release) > 
                        (self.packages[name]["parsed_version"], self.packages[name]["parsed_release"]))):
                    if self.debug:
                        print "  best so far"
                    path = os.path.join(dir_name, file_name)
                    self.packages[name] = {"version": version,
                                           "parsed_version": parsed_version, 
                                           "release": release,
                                           "parsed_release": parsed_release,
                                           "path": path}
                elif self.debug:
                    print ("  ignoring - already have version %s release %s" % 
                           (self.packages[name]["version"], self.packages[name]["release"]))

    def rpm_path(self, name):
        """
        Returns the path of the latest version of RPM in the 
        specified directories, or None if not found
        """
        if name in self.packages:
            return self.packages[name]["path"]
        else:
            return None

local_rpms = LocalRPMS(config.package_dirs)


class RPM(object):
    def __init__(self, name, 
                 min_version = None,
                 local_path_finder = local_rpms.rpm_path):
        self.name = name
        self.local_path = local_path_finder(name)
        self.is_local = (self.local_path != None)
        self.remote_path = None

    @property
    def path(self):
        """
        Return the path of the RPM.  If it does not exist locally,
        then this forces a download to the cache dir.  (If you don't
        want this to happen, use local_path instead.)
        """
        if self.is_local:
            return self.local_path
        if not self.remote_path:
            self.remote_path = self.download()
        return self.remote_path

    def download(self, 
                 dir_name = config.cache_dir,
                 try_download_every_time = config.try_download_every_time):
        """
        Downloads an RPM via yum and returns the path of the 
        downloaded file
        """
        name = self.name
        dir_name = config.cache_dir

        command_stem = config.yumdownloader_command
        command_args = "--destdir=%s %s" % (dir_name, name)

        download_command = "%s %s" % (command_stem, command_args)
        urls_command = "%s --urls %s" % (command_stem, command_args)

        # get the URL path by parsing the output of the URLs command
        output = get_output(urls_command)
        m = re.search(r"://[^\s]+/([^/\s]+(noarch|x86_64)\.rpm)\b", output)
        file_name = m.group(1)
        path = os.path.join(dir_name, file_name)

        # download if necessary
        if try_download_every_time or not os.path.exists(path):
            output = get_output(download_command)
            if not os.path.exists(path):
                raise Exception("expected path %s not found after RPM download of %s" % path, name)
        return path


    def rpm_query(self, rpm_tag):
        """
        return what 'rpm -qp' reports on a package file for a given query tag
        """
        command = 'rpm -qp --queryformat="%%{%s}" %s' % (rpm_tag,
                                                         self.path)
        try:
            output = get_output(command)
        except Exception:
            return None
        if output == "(none)":
            return None
        return output

    @property
    def version(self):
        return self.rpm_query("VERSION")

    @property
    def release(self):
        return self.rpm_query("RELEASE")

    @property
    def summary(self):
        return self.rpm_query("SUMMARY")

    @property
    def description(self):
        return self.rpm_query("DESCRIPTION")

    @property
    def url(self):
        return self.rpm_query("URL")

    @property
    def build_host(self):
        return self.rpm_query("BUILDHOST")

    @property
    def build_time_int(self):
        return int(self.rpm_query("BUILDTIME"))

    @property
    def build_time_ascii(self):
        return time.asctime(time.localtime(self.build_time_int))

    @property
    def dependencies(self):
        """
        A list of all RPM dependencies of a package.
        Output of rpm -qR but exclude anything with '/' or '(' because
        these are things other than names of RPM packages.
        Also strip off versions.
        """
        deps = []
        output = get_output("rpm -qpR %s" % self.path)
        for line in output.split("\n"):
            if "/" in line or "(" in line:
                continue
            name = line.split()[0]
            if name not in deps:
                deps.append(name)
        deps.sort()
        return deps
        

class MakeDocumentation(object):
    """
    class that makes the documentation
    """
    def __init__(self,
                 verbose = False):
        self.packages = {}
        self.verbose = verbose

    def add_package(self, rpm_arg,
                    recurse = False,
                    show_nonlocal_deps_for = []):
        """
        Add an rpm to the set of packages to be documented.
        rpm can be a name or an RPM object.
        Will recurse if recurse=True.
        During recursion, will include non-local dependencies
        if the name matches something in the "show_nonlocal_deps_for" list,
        otherwise only packages in the local repository are listed.
        """
        if isinstance(rpm_arg, str):
            name = rpm_arg
            rpm = RPM(name)
        else:
            assert(isinstance(rpm_arg, RPM))
            rpm = rpm_arg
            name = rpm.name

        if self.verbose:
            print "adding %s" % name

        if name in self.packages:
            if self.verbose:
                print "doing nothing - already got this"
            return

        self.packages[name] = rpm

        if recurse:
            for rpm_name in rpm.dependencies:
                if self.verbose:
                    print "found dependency %s (of %s)" % (rpm_name, name)
                other = RPM(rpm_name)
                if other.is_local or name in show_nonlocal_deps_for:
                    self.add_package(other, 
                                     recurse = other.is_local,
                                     show_nonlocal_deps_for = show_nonlocal_deps_for)

    def add_all_packages(self,
                         top_level_packages = config.top_level_packages,
                         show_nonlocal_deps_for = config.show_nonlocal_deps_for):
        """
        Add all packages to the list of packages to document, 
        from specified set of top-level meta packages
        """
        for name in top_level_packages:
            self.add_package(name, 
                             recurse=True, 
                             show_nonlocal_deps_for = show_nonlocal_deps_for)

    @property
    def packages_in_name_order(self):
        names = self.packages.keys()
        names.sort()
        return map(lambda name: self.packages[name], names)        

    def list_packages(self):
        """
        for testing..
        """
        for r in self.packages_in_name_order:
            print (r.name, r.path, r.is_local, r.version, r.summary, r.build_host,
                   r.dependencies, r.url)
    
    def _write_markdown_table_to_fh(self, fh):
        """
        (see write_markdown_table)
        """
        # fh.write("| **Package** | Version | Release | Build date | Summary |\n")
        # fh.write("| ------- | ------- | ------- | ---------- | ------- |\n")
        # for rpm in self.packages_in_name_order:
        #     fh.write("| %s | %s | %s | %s | %s |\n" %
        #              (self._markdown_link(rpm.name, rpm.url),
        #               rpm.version,
        #               rpm.release,
        #               rpm.build_time_ascii,
        #               rpm.summary))

        for rpm in self.packages_in_name_order:
            fh.write("* **%s** - %s. _Version_ %s-%s, _build date_ %s.\n" % 
                     (self._markdown_link(rpm.name, rpm.url), 
                      rpm.summary,
                      rpm.version,
                      rpm.release,
                      rpm.build_time_ascii))
            fh.write("\n")


    def _markdown_link(self, link_text, target):
        if target:
            return "[%s](%s)" % (link_text, target)
        return link_text

    def write_markdown_table(self, out = sys.stdout):
        """
        Write a table to specified output, which can be an open file handle
        or a filename
        """
        file_opened = None
        if isinstance(out, str):
            file_opened = out
            out = open(out, "w")
        self._write_markdown_table_to_fh(out)
        if file_opened:
            out.close()


def main():
    """
    writes wiki page to specified file or to stdout
    """
    m = MakeDocumentation(verbose = False)
    m.add_all_packages()
    try:
        kwargs = {"out": sys.argv[1]}
    except IndexError:
        kwargs = {}
    m.write_markdown_table(**kwargs)


if __name__ == "__main__":
    main()

    #m = MakeDocumentation(verbose = True)
    #m.add_all_packages()
    #m.list_packages()
