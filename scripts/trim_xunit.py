#!/usr/bin/env python
"""
Process an XUnit XML file to shorten test names thus making them easier to use
in reporting.

"""

import sys
from xml.etree import ElementTree as ET
import hashlib
import re
import os

SHORTEN_ATTRS = ('name', 'classname')
MAX_ATTR_LENGTH = 60

def shorten_attr(elem, attr):
    val = elem.get(attr, '')

    if len(val) > MAX_ATTR_LENGTH:
        # Normalise whitespace
        val = re.sub(r'\s+', ' ', val, flags=re.DOTALL | re.MULTILINE)

        match = re.match(r'(.*?)\((.*)\)$', val)
        if match:
            name, args = match.groups()
            md5 = hashlib.md5(args)
            short_val = '%s#%s' % (name, md5.hexdigest()[:6])
        else:
            md5 = hashlib.md5(val[MAX_ATTR_LENGTH-8:])
            short_val = '%s!%s' % (val[:MAX_ATTR_LENGTH-8], md5.hexdigest()[:6])
        elem.set(attr, short_val)

def main(argv=sys.argv):
    xunits = argv[1:]

    for xunit_xml_in in xunits:
        xunit_xml_out = os.path.splitext(xunit_xml_in)[0]+'_trimmed.xml'
        xunit_et = ET.parse(open(xunit_xml_in))

        for elem in xunit_et.findall('.//testcase'):
            for attr in SHORTEN_ATTRS:
                shorten_attr(elem, attr)

        with open(xunit_xml_out, 'w') as fh:
            xunit_et.write(fh)

    

if __name__ == '__main__':
    main()
