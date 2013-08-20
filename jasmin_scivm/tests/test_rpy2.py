"""
Test rpy2 interface to R

"""

import subprocess as sp
import re
import os.path as op

from jasmin_scivm.tests import TESTS_DIR

def test_rpy2_robject():
    from rpy2.robjects import r
    
    assert 'language: R' in str(r)
    assert 'version.string: R version' in str(r)

def test_rpy2_eval():
    from rpy2.robjects import r

    sqr = r('function(x) x^2')
    assert sqr(2)[0] == 4.0

def test_rpy2_import():
    from rpy2.robjects.packages import importr
    utils = importr('utils')

    assert utils.data is not None
