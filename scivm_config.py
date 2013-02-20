"""
Read the SciVM configuration and expose as an object

"""

from ConfigParser import SafeConfigParser as ConfigParser
import rpm
import sys


TRAC_PREAMBLE = '''
== JASMIN SciVM Supported Packages ==

Each JASMIN Science VM includes the standard development tools which
are part of the Redhat "Development Tools" group.  These include the
standard compilers (gcc, g++, gfortran) and version control systems
(subversion, git).  In addition each VM includes the following set of
general and science tools which we support in terms of managing
upgrades and bug fixes.

If a tool isn't in this list you can request their inclusion by
submitting a feature request at [wiki:JASMIN/ScientificAnalysisVM/Tickets]

'''

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
            info = dict((tag, _clean_tag_value(h[tag])) 
                        for tag in ['name'] + tags)
            yield info

def _clean_tag_value(value):
    """
    For some reason unusual characters have ended up in at least
    one RPM's metadata.  The cdo package has  the character 0xb6
    in it's summary.  Therefore this function cleans any known
    illegal characters.

    """
    if type(value) is str:
        value = value.replace('\xb6', '')

    return value

def write_supported_dat(conf, fh=sys.stdout):
    """
    Write a tab separated file of name, version, release.
    This format is designed to be compatible with the rpms.csv file originally
    used to list the supported rpms.

    """
    data = iter_rpm_info(conf.supported_rpms, ['name', 'version', 'distribution'])

    print '# NAME\tVERSION\tDISTRIBUTION'
    for d in data:
        print >>fh, '{0}\t{1}\t{2}'.format(
            d['name'], d['version'], d['distribution']
            )

def write_trac(conf, fh=sys.stdout):
    """
    Write a Trac Wiki page describing the supported packages.

    """

    data = dict((x['name'], x) for x in iter_rpm_info(
            conf.supported_rpms, 
            ['name', 'version', 'summary', 'distribution', 'url', 
             'release', 'packager', 'platform']))

    print >>fh, TRAC_PREAMBLE

    print >>fh, '||= Package =||= Version =||= Summary =||'
    for name in sorted(data):
        print >>fh, '|| [{url} {name}] || {version}-{release} || {summary} ||'.format(**data[name])


if __name__ == '__main__':
    conf = SciVMConf.from_file('scivm.conf')

    import cStringIO as StringIO
    import trac_rpc
    import getpass
    from xml.sax.saxutils import escape

    wiki_fh = StringIO.StringIO()
    write_trac(conf, wiki_fh)

    wiki_file = 'packages.wiki'
    with open(wiki_file, 'w') as fh:
        print >>fh, wiki_fh.getvalue()
    print 'Written packages wiki page to %s' % wiki_file
        
    wiki_page = 'JASMIN/ScientificAnalysisVM/Packages'
    print 'Would you like to send this content to Trac page %s? ' % wiki_page,
    resp = raw_input()
    if resp.strip().lower() in ['y', 'yes']:
        print 'Sending ...'
        proxy = trac_rpc.make_proxy()
        proxy.wiki.putPage(wiki_page, escape(wiki_fh.getvalue()), {})


