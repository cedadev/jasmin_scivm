"""
Test netCDF libraries are available and properly configured

"""

import subprocess as sp
import re
from unittest import TestCase

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

    def test_fortran(self):
        # Ensure f77 and f90 support
        assert re.search(r'--has-f77.*-> yes', self.header)
        assert re.search(r'--has-f90.*-> yes', self.header)


