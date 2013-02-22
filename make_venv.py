"""
Create a virtual environment bootstrap script specifically for running the iris unit tests.

This script assumes the following packages are available in the base 
environment:
 - Iris
 - virtualenv
 - nose


It will create a virtualenv inheriting the base environment's site-packages.
It will then copy Iris from the base environment into the virtualenv so that
the unit tests can write to the test directory.  It also monkey_patches
certain test files to ensure tests that are not appropriate are skipped.

"""

import virtualenv

hooks_file = './venv_bootstrap_hooks.py'
hooks_source = open(hooks_file).read()

output = virtualenv.create_bootstrap_script(hooks_source)
f = open('venv_bootstrap.py', 'w').write(output)
