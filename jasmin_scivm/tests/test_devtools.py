"""
Trivial tests for the presence of key development tools.

"""

import subprocess as S
import os
import sys


DEV_COMMANDS = [
    'yacc', 'bison', 'gfortran', 'gcc', 'c++', 'svn', 'git',
]

def check_installed(command):
    p = S.Popen('which %s' % command, shell=True,
                stdout=S.PIPE)
    output = p.stdout.read()
    status = p.wait()
    print 'which %s --> %s' % (command, output)
    assert status == 0


def test_installed():
    for cmd in DEV_COMMANDS:
        yield check_installed, cmd


