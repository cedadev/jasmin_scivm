"""
Test for the existance of octave.

"""

import os
import os.path as op
import subprocess as sp
import tempfile
import shutil

def test_octave_exe():
    p = sp.Popen("octave --version", shell=True, stdout=sp.PIPE)

    header = p.stdout.read()

    assert 'GNU Octave' in header


def test_octcdf():
    tmpdir = tempfile.mkdtemp()
    try:
        fn = 'nctest_file.oct'
        with open(op.join(tmpdir, fn), 'w') as fh:
            fh.write('nctest\n')

        p = sp.Popen('cd %s ; octave %s' % (tmpdir, fn),
                     stderr=sp.STDOUT, stdout=sp.PIPE, shell=True,)
        output = p.stdout.read()
        print output

        p.wait()
        assert p.returncode == 0

        #!TODO: pass output to find how many tests pass
        #!TODO: pass nctest.log in tmpdir to get details
        #!TODO: decide how many tests need to pass

    finally:
        shutil.rmtree(tmpdir)
