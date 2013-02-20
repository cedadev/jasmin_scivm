"""
Test basic python imports.

These are trivial tests to make sure libraries are installed.

Packages that have their own test module don't need listing here

"""

from importlib import import_module

IMPORTS = [
    'pydap',
    'pygments',
    'shapely',
    'mpl_toolkits.basemap',
    'cartopy',
    'matplotlib',
    'mpi4py',
    'pyhdf',
    'rpy2',
    ]


def test_imports():
    for imp in IMPORTS:
        yield import_module, imp

