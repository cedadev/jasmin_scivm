"""
Test nco operators


"""

import subprocess as sp
import re
import os.path as op
import unittest
import tempfile
import shutil

from jasmin_scivm.tests import TESTS_DIR


class TestNCO(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def test_ncks(self):
        p = sp.Popen("ncks {0}/data/foo.nc".format(TESTS_DIR),
                     shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
        output = p.stdout.read()
        
        assert 'filetype = NC_FORMAT_CLASSIC' in output
        assert 'Global attribute 0: Conventions, size = 6 NC_CHAR, value = CF-1.0' in output

    def test_ncks2(self):
        p = sp.check_call('ncks -d time,0 {0}/data/cru_reduced.nc {1}/cru_out.nc'.format(TESTS_DIR, self.tmpdir),
                          shell=True)

        assert op.exists('{0}/cru_out.nc'.format(self.tmpdir))

    def tearDown(self):
        shutil.rmtree(self.tmpdir)
