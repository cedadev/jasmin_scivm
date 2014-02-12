from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='jasmin_scivm',
      version=version,
      description="JASMIN Scientific Analysis Build Test Suite",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Stephen Pascoe',
      author_email='Stephen.Pascoe@stfc.ac.uk',
      url='http://proj.badc.rl.ac.uk/cedaservices/wiki/JASMIN',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'nose>=1.0',
      ],
      test_suite = 'nose.collector',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
