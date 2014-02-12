#!/usr/bin/env python2.7
"""
Run exactly the tests we want to verify the JAP SciVM is consistent.

This script offers better configurability than messing round with nose configuration options.

"""

import os, shutil

from nose.core import run
from nose.loader import TestLoader
from nose.config import Config
import numpy

def main():
    if os.path.exists('xunit_results'):
        shutil.rmtree('xunit_results')
        os.mkdir('xunit_results')

    numpy.test('full', extra_argv='--with-xunit --xunit-file=xunit_results/numpy_tests.xml'.split())

    run(defaultTest='jasmin_scivm/tests', 
        argv='dummy --with-xunit --xunit-file=xunit_results/jap_tests.xml'.split(),
        exit=False)

    run(defaultTest='cdat_lite', 
        argv='dummy --with-xunit --xunit-file=xunit_results/cdat_tests.xml'.split(),
        exit=False)
    

if __name__ == '__main__':
    main()
