"""
Test cdo operators


]$ ncks jasmin_scivm/tests/data/foo.nc 
Summary of jasmin_scivm/tests/data/foo.nc: filetype = NC_FORMAT_CLASSIC, 0 groups (max. depth = 0), 0 dimensions (0 fixed, 0 record), 0 variables (0 atomic-type, 0 non-atomic), 2 attributes (2 global, 0 group, 0 variable)
Global attributes:
Global attribute 0: Conventions, size = 6 NC_CHAR, value = CF-1.0
Global attribute 1: bar, size = 1 NC_INT, value = 1



"""

import subprocess as sp
import re
import os.path as op

from jasmin_scivm.tests import TESTS_DIR

def test_ncks():
    p = sp.Popen("ncks {0}/data/foo.nc".format(TESTS_DIR),
                 shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    output = p.stdout.read()

    assert 'filetype = NC_FORMAT_CLASSIC' in output
    assert 'Global attribute 0: Conventions, size = 6 NC_CHAR, value = CF-1.0' in output

