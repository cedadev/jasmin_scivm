"""
Read the SciVM configuration and expose as an object

"""

from ConfigParser import SafeConfigParser as ConfigParser
import rpm
import sys

class SciVMConf(object):
    def __init__(self, config):
        self._config = config

    @property
    def supported_rpms(self):
        rpm_str = self._config.get('rpms', 'supported')
        return rpm_str.split()

    @property
    def system_rpms(self):
        rpm_str = self._config.get('rpms', 'system')
        return rpm_str.split()

    @property
    def system_groups(self):
        rpm_str = self._config.get('rpms', 'system_groups')
        # Split by newline only
        return [x1 for x1 in (x.strip() for x in rpm_str.split('\n'))
                if x1]

    @classmethod
    def from_file(cls, config_file):
        config = ConfigParser()
        config.read(config_file)

        return cls(config)

def iter_rpm_info(rpms, tags):
    """
    Return an iterator of dictionaries containing information about selected
    packages.

    :param rpms: A sequence of rpm names
    :param tags: A sequence of rpm tags to include in the returned data.

    """
    ts = rpm.TransactionSet()
    for r in rpms:
        for h in ts.dbMatch('name', r):
            info = dict((tag, h[tag]) for tag in ['name'] + tags)
            yield info


def write_supported_dat(conf, fh=sys.stdout):
    """
    Write a tab separated file of name, version, release.
    This format is designed to be compatible with the rpms.csv file originally
    used to list the supported rpms.

    """
    #!TODO: release
    data = iter_rpm_info(conf.supported_rpms, ['name', 'version', 'distribution'])

    print '# NAME\tVERSION\tDISTRIBUTION'
    for d in data:
        print '{0}\t{1}\t{2}'.format(
            d['name'], d['version'], d['distribution']
            )

if __name__ == '__main__':
    conf = SciVMConf.from_file('scivm.conf')

    write_supported_dat(conf)
