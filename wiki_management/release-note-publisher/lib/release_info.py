import re
import os
import datetime
import time

import config

def _read_index(filename = config.index_file):

    """
    read the index file into a list of (version, install_date), 
    ignoring any comment lines
    """
    all_releases = []
    f = open(filename)
    for line in f.readlines():
        if not line.startswith("#"):
            bits = line.split()
            if bits:
                try:
                    version, install_date = bits
                except ValueError:
                    print "skipping line %s in index file" % line
                    continue
                all_releases.append((version, install_date))
    f.close()
    return all_releases            


def _read_release_contents(version, dirname = config.release_notes_dir):
    """
    read contents of release with given version;
    this should just be the contents of ascii file named after the
    version, in the directory where these are kept
    """
    filename = os.path.join(dirname, version)
    f = open(filename)
    contents = f.read()
    f.close()
    return contents


_todays_date = datetime.date(*time.localtime()[:3])

class Release(object):
    def __init__(self, version, install_date, contents):
        self.version = version
        self.install_date = self._parse_date(install_date)
        self.contents = contents        

    def _parse_date(self, datestr):
        """
        parse a yyyymmdd string into datetime.date
        """
        m = re.match("^([0-9]{4})([0-9]{2})([0-9]{2})$", datestr)
        if not m:
            raise ValueError("%s is not yyyymmdd" % datestr)
        bits = map(int, m.groups())

        return datetime.date(*bits)
    
    def is_in_future(self):
        return self.install_date > _todays_date

    # sorted list will be chronological
    def __cmp__(self, other):
        return cmp(self.install_date, other.install_date)


def read_releases():
    """
    Read release notes into a list of Release objects
    """
    releases = []
    for version, install_date in _read_index():
        contents = _read_release_contents(version)
        releases.append(Release(version, install_date, contents))
    return releases
