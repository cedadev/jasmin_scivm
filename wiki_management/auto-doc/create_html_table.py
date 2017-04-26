#!/usr/bin/env python

import sys

from autodoc import MakeDocumentation

if __name__ == '__main__':
    fname = "packages.html"
    m = MakeDocumentation(verbose = True)
    m.add_all_packages()
    print "creating %s..." % fname,
    sys.stdout.flush()
    m.write_html_table(out=fname)
    print "done"
