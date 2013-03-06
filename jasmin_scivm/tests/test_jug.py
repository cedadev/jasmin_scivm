
from jasmin_scivm.tests import TESTS_DIR

import tempfile
from unittest import TestCase
import shutil
import os.path as op
import subprocess as S

## Typical status output
#
#Task name                                    Waiting       Ready    Finished     Running
#----------------------------------------------------------------------------------------
#do_jug.is_prime                                    0          48           0           0
#........................................................................................
#Total:                                             0          48           0           0



class TestJug(TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.script_path = op.join(TESTS_DIR, 'do_jug.py')

        shutil.copy2(self.script_path, self.tmpdir)

    def test1(self):
        p = S.Popen("jug_py27 status {0}".format(self.script_path), shell=True, stdout=S.PIPE)
        p.wait()
        output = p.stdout.read()
        print output
        assert p.returncode == 0

        assert 'do_jug.is_prime' in output 

    #!TODO: A test which runs the script

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

