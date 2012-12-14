"""
Test netCDF libraries are available and properly configured

"""

import subprocess as sp
import re
import os

from unittest import TestCase
import tempfile

from jasmin_scivm.tests import TESTS_DIR

class TestNetCDF(TestCase):
    """
    Ensure the nc-config command is present and that it indicates
    the existence of Fortran, HDF and OPeNDAP support.
    
    """
    def setUp(self):
        p = sp.Popen("nc-config --all", shell=True, stdout=sp.PIPE)
        self.header = p.stdout.read()
        

    def test_nc_config(self):
        # Ensure NetCDF 4.x distribution
        assert re.search(r'netCDF 4\.\d+\.\d+', self.header)

    def test_dap(self):
        # Ensure DAP support
        assert re.search(r'--has-dap.*-> yes', self.header)

    def test_nc4(self):
        # Ensure NetCDF4 format support
        assert re.search(r'--has-nc4.*-> yes', self.header)
        assert re.search(r'--has-hdf5.*-> yes', self.header)

    def test_f90(self):
        # Ensure f90 support
        assert re.search(r'--has-f90.*-> yes', self.header)

    def test_f77(self):
        # Ensure f77 support
        assert re.search(r'--has-f77.*-> yes', self.header)
    test_f77.__test__ = False

    def test_fortran_compile(self):
        fflags = re.search(r'--fflags.*-> (.*)', self.header).group(1)
        fc = re.search(r'--fc.*-> (.*)', self.header).group(1)
        flibs = re.search(r'--flibs.*-> (.*)', self.header).group(1)

        test_file = os.path.join(TESTS_DIR, 'data', 'test.f')
        (fd, test_exe) = tempfile.mkstemp(prefix='test_fortran_')
        os.close(fd)
        try:

            p = sp.Popen('%s %s %s %s -o %s' % (fc, fflags, flibs, test_file,
                                                test_exe),
                         shell=True, stderr=sp.STDOUT, stdout=sp.PIPE)
        
            print p.stdout.read()

            p2 = sp.Popen('cd %s ; %s' % (TESTS_DIR+'/data', test_exe),
                          shell=True, stderr=sp.STDOUT, stdout=sp.PIPE)
            output = p2.stdout.read()
            print output
            
            assert re.search(r'There are\s+0 dimensions', output)

        finally:
            os.remove(test_exe)
        
