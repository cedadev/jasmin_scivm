"""
Test virtualenv works.

"""

from unittest import TestCase
from jasmin_scivm.tests import TESTS_DIR

import os
import shutil
import subprocess as S

class TestVirtualenv(TestCase):
    def setUp(self):
        self.venvs_dir = os.path.join(TESTS_DIR, 'venvs')
        os.mkdir(self.venvs_dir)

    def test_venv1(self):
        p = S.Popen("virtualenv {0}/v1".format(self.venvs_dir), shell=True, stdout=S.PIPE)
        p.wait()
        output = p.stdout.read()
        print output
        assert p.returncode == 0

    def test_venv2(self):
        p = S.Popen("virtualenv --system-site-packages {0}/v2".format(self.venvs_dir), 
                    shell=True, stdout=S.PIPE)
        p.wait()
        output = p.stdout.read()
        print output
        assert p.returncode == 0

    def tearDown(self):
        shutil.rmtree(self.venvs_dir)
