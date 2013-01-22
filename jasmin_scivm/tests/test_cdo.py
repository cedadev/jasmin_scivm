"""
Test cdo operators

"""

import subprocess as sp
import re
import os.path as op

from jasmin_scivm.tests import TESTS_DIR

def test_cdo_help():
    p = sp.Popen("cdo -h", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    output = p.stdout.read()

    assert 'usage : cdo ' in output
    assert re.search(r'CDO version .*, Copyright \(C\) \d+-\d+ Uwe Schulzweida',
                     output, re.M)

def test_cdo_info():
    p = sp.Popen("cdo info %s/data/rain.nc" % TESTS_DIR, shell=True,
                 stdout=sp.PIPE)
    output = p.stdout.read()
    assert output.strip() == '''-1 :       Date  Time    Param        Level    Size    Miss :     Minimum        Mean     Maximum
     1 : 2009-06-01 06:59:59 -1               0   27840       0 :      0.0000  2.4566e-05  0.00022504'''
