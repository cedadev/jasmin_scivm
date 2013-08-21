"""
Test nco operators


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

