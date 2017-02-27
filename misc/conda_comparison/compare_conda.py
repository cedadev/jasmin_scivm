import string
import re
import urllib2
from subprocess import Popen, PIPE

"""
Compares packages in the JAP with those in Conda Forge, and produces an HTML 
document summarising the situation

To run this:

either:

- use lists copied from a machine that is running the JAP, that were 
  generated as follows:

    *  rpm -qa > all-rpms        

    *  (rpm -qR jasmin-sci-vm ; rpm -qR jasmin-common-vm) > all-deps

  also wget a copy of:

    * wget -o feedstocks.html https://conda-forge.github.io/feedstocks.html


- OR run on node that has the JAP installed, and have it do the 'rpm' commands 
  live as well as getting the feedstocks.html on the fly.  In that case, set 
  "live=True" in the call to main() at the bottom of the code.

"""


def list_pkgs_in_conda(url="https://conda-forge.github.io/feedstocks.html",
                       file=None):
    """
    Opens conda-forge feedstocks.html on conda site or local copy, and returns
    list of package names in conda-forge.
    """
    if file:
        fh = open(file)
    else:
        fh = urllib2.urlopen(url)

    matcher = re.compile('<a href="https://github.com/conda-forge/(.*?)-feedstock">').search

    pkgs = []
    for line in fh:
        m = matcher(line)
        if m:
            pkgs.append(m.group(1))
    pkgs.sort()
    return pkgs


def read_file_or_run_commands(file, commands):
    if file:
        fh = open(file)
        content = fh.read()
        fh.close()
    else:
        content = ""
        for cmd in commands:
            proc = Popen(cmd, shell=True, stdout=PIPE)
            content += proc.communicate()[0]    
    return content

def list_pkgs_in_jap(file=None):
    """
    obtains rpm dependencies of jasmin-sci-vm and jasmin-common-vm, or
    opens local file with same 'rpm' output, and returns list of packages
    """
    content = read_file_or_run_commands(file, 
                                        ["rpm -qR jasmin-sci-vm",
                                         "rpm -qR jasmin-common-vm"])
    pkgs = []
    for line in content.split("\n"):
        bits = line.split()
        if len(bits) == 3 and bits[1] in ('==', '>=', '<='):
            pkg = bits[0]
            if not pkg.startswith("rpmlib("):
                pkgs.append(pkg)
    return pkgs

def list_all_ceda_pkgs(file=None):
    """
    Obtains list of all installed RPMs that are packaged by CEDA, or 
    takes this from a file containing 'rpm -qa' output.  These will 
    normally be included via the JAP, but might not be direct dependencies.
    """
    content = read_file_or_run_commands(file, ["rpm -qa"])
    pkgs = []
    for pkg_full in content.split("\n"):
        if '.ceda.' in pkg_full:
            bits = pkg_full.split("-")
            pkg = string.join(bits[:-2], "-")
            pkgs.append(pkg)
    return pkgs

def full_list_pkgs_in_jap(use_files=False):
    """
    Get list of packages which are either packaged by CEDA or a direct 
    dependency of the JAP meta RPMs.  Returns a list of 2-tuples 
    (pkg, is_ceda_pkg)
    """
    if use_files:
        pkgs_jap = list_pkgs_in_jap(file="all-deps")
        ceda_pkgs = list_all_ceda_pkgs(file="all-rpms")
    else:
        pkgs_jap = list_pkgs_in_jap()
        ceda_pkgs = list_all_ceda_pkgs()

    all_pkgs = list(set(pkgs_jap) | set(ceda_pkgs))
    all_pkgs.sort()
    return [(pkg, pkg in ceda_pkgs) for pkg in all_pkgs]

def map_name(pkg):
    """
    translate package name in JAP to equivalent we expect to find in conda
    """

    # python packages - conda-forge just has package name without "python"
    if pkg.startswith("python27-"):
        return pkg[9:]

    # for identifiable sub-packages, return just the base name, 
    # as do not expect conda-forge to have separate subpackages

    # known prefixes with subpackages
    for prefix in ("gdal", "esmf", "emacs", "grib_api", "subversion", "graphviz", "proj"):
        if pkg.startswith(prefix + "-"):
            return prefix

    # for known suffixes for subpackages
    for suffix in ("devel", "lib", "libs", "python27"):
        if pkg.endswith("-" + suffix):
            return pkg[: -len(suffix) - 1]
    
    return pkg
    
def start_html(out_file):
    f = open(out_file, "w")
    f.write("""
<html>
<head><title>JAP / Conda forge comparison</title></head>
<body>
<H1>JAP / Conda forge comparison</H1>

<p>Colour key in table below:</p>
<ul>
<li>Red: not found in Conda Forge, and packaged by CEDA
<li>Yellow: not found in Conda Forge, but not packaged by CEDA (i.e. RPMs from standard repositories)
<li>Green: found in Conda Forge
<li>Grey: package that can be ignored</li>
</ul>

<table border="1" cellpadding="3" cellspacing="0">
<tr>
  <th>Package name in JAP</th>
  <th>packaged by CEDA</th>
  <th>mapped name looked for in Conda Forge</th>
  <th>found in Conda Forge</th>
</tr>
""")
    return f

def end_html(f):
    f.write("</table></body></html>")
    f.close()

def compare_pkg_lists(pkgs_conda, pkgs_jap, out_file):
    """
    Compare packages lists and report which JAP packages are provided by
    conda.
    """
    f = start_html(out_file)
    pkgs_conda = set(pkgs_conda)
    for pkg, is_ceda_pkg in pkgs_jap:
        cells = []
        pkg_conda = map_name(pkg)
        found = (pkg_conda in pkgs_conda)

        if pkg in ('jasmin-sci-vm', 'jasmin-common-vm'):
            col = '#c0c0c0'
        elif found:
            col = "#80ff80"
        elif not is_ceda_pkg:
            col = "ffff80"
        else:
            col = "#ff8080"

        cells = [pkg, str(is_ceda_pkg), pkg_conda, str(found)]
        f.write('<tr bgcolor="%s">' % col)
        for cell in cells:
            f.write("<td>%s</td>" % cell)
        f.write("</tr>\n")
    end_html(f)

def main(live=True):
    if live:
        pkgs_conda = list_pkgs_in_conda()
    else:
        pkgs_conda = list_pkgs_in_conda(file="feedstocks.html")
    pkgs_jap = full_list_pkgs_in_jap(use_files = (not live))
    compare_pkg_lists(pkgs_conda, pkgs_jap, "report.html")
        

if __name__ == '__main__':
    main(live=False)
