"""
Test netCDF libraries are available and properly configured

"""

import subprocess as sp
import re

def test_nc_config():
    """
    Ensure the nc-config command is present and that it indicates
    the existence of HDF and OPeNDAP support.

    """
    p = sp.Popen("nc-config --all", shell=True, stdout=sp.PIPE)

    header = p.stdout.read()

    assert re.search(r'netCDF 4\.\d+\.\d+', header)
    assert re.search(r'--has-dap.*-> yes', header)
    assert re.search(r'--has-nc4.*-> yes', header)
    assert re.search(r'--has-hdf5.*-> yes', header)
