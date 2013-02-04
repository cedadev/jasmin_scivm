"""
Tests for geos -- a dependency of IRIS.

"""

import sys
from jasmin_scivm.tests import TESTS_DIR
import os
import os.path as op
import tempfile

def test_geometry_transform():
    """
    This test dumps core.

    """
    src_file = op.join(TESTS_DIR, 'test_geos.c')
    fd, executable = tempfile.mkstemp()
    try:
        os.close(fd)
        os.system('gcc -o {0} {1} -lgeos_c'.format(executable, src_file))
        retcode = os.system(executable)
        assert retcode == 0

    finally:
        os.remove(executable)

                   
