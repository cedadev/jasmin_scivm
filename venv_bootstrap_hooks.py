# For inclusion in virtualenv bootstrap scripts.

import subprocess as S
import os.path as op
import imp
import shutil

def adjust_options(options, args):
    options.system_site_packages = True

def after_install(options, home_dir):

    pip = op.join(home_dir, 'bin', 'pip')
    S.call([pip, 'install', 'mock'])
    S.call([pip, 'install', '--upgrade', 'nose'])
    S.call([pip, 'install', 'NoseXUnit'])
    iris_dir = unpack_iris(home_dir)
    patch_iris_tests(iris_dir)

def unpack_iris(home_dir):
    """
    Copy iris installation to somewhere where it's writable.

    """
    iris_dir = imp.find_module('iris')[1]

    
    venv_lib = op.join(home_dir, 'lib',
                       'python{0}.{1}'.format(sys.version_info[0],
                                              sys.version_info[1]),
                       'site-packages')

    print 'Copying iris package to %s' % venv_lib

    iris_local = op.join(venv_lib, 'iris')
    shutil.copytree(iris_dir, iris_local)

    return iris_local

def patch_iris_tests(iris_dir):
    """
    Disable tests that look for the iris data repository.

    """
    print 'Patching iris.tests'
    with open(op.join(iris_dir, 'tests', '__init__.py'), 'a') as fh:
        print >>fh, """

##############################################################################
# Monkey patch to disable some tests
#  Applied by jasmin_scivm test framework

import iris.io
from nose.plugins.skip import SkipTest

def select_data_path(resources_subdir, rel_path):
    raise SkipTest("Running without iris DATA_REPOSITORY")

iris.io.select_data_path = select_data_path

##############################################################################
"""
