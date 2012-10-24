"""
Test for the existance of octave.

"""

import subprocess as sp

def test_octave_exe():
    p = sp.Popen("octave --version", shell=True, stdout=sp.PIPE)

    header = p.stdout.read()

    assert 'GNU Octave' in header
