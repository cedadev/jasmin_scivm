"""
Test the mpi4py python bindings.

"""

import os
import sys
import random
import string
import time
import signal
import subprocess as S
from unittest import TestCase

from jasmin_scivm.tests import TESTS_DIR

SECRET_LENGTH = 20
DEFAULT_CONF = '%s/.mpd.conf' % os.environ['HOME']



class TestMpi4py(TestCase):
    def setUp(self):
        self.mpd = MpdMonitor()
        self.mpd.start()

    def tearDown(self):
        self.mpd.stop()


    def test1(self):
        p = S.Popen('mpirun -np 4 python2.7 %s' % os.path.join(TESTS_DIR, 
                                                               'mpieg.py'),
                    shell=True,
                    stdout=S.PIPE,
                    stderr=S.STDOUT)
        data = p.stdout.read()
        print data
        
        expected_lines = '''
# Initial State for processor 0 is data=[1, 4, 9, 16]
# Initial State for processor 1 is data=None
# After scattering processor 1 has data 4
# Now something is done on processor 1
# After gathering processor 1 has None
# After scattering processor 0 has data 1
# Now something is done on processor 0
# Initial State for processor 3 is data=None
# Initial State for processor 2 is data=None
# After scattering processor 2 has data 9
# Now something is done on processor 2
# After gathering processor 2 has None
# After scattering processor 3 has data 16
# Now something is done on processor 3
# After gathering processor 3 has None
# After gathering processor 0 has [101, 104, 109, 116]
'''
        for expected in expected_lines.split('\n'):
            assert expected.strip() in data



class MpdMonitor(object):
    def __init__(self):
        self._proc = None
        self.conf_file = DEFAULT_CONF

    def start(self):
        if self._proc is not None:
            raise Exception("mpd already running")

        if not os.path.exists(DEFAULT_CONF):
            self.create_mpd_conf()

        self._proc = S.Popen('mpd', shell=True)
        time.sleep(1)
        if self._proc.pid:
            print 'mpd started PID=%s' % self._proc.pid
        else:
            raise Exception("Failed starting mpd")

    def stop(self):
        if self._proc is None:
            raise Exception("mpd not running")

        self._proc.terminate()
        self._proc.wait()
        self._proc = None

    def create_mpd_conf(self):
        secret = ''.join(random.choice(string.ascii_letters + string.digits) 
                         for _ in range(SECRET_LENGTH))

        with open(self.conf_file, 'w') as fh:
            print >>fh, '''# Auto-generated mpd.conf by jasmin_scivm test suite

MPD_SECRETWORD={0}
'''.format(secret)

        os.chmod(self.conf_file, 0600)



