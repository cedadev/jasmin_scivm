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
    'pyhdf',
    'rpy2',
    'gribapi',
    ]


def check_import(imp):
    try:
        import_module(imp)
    except ImportError:
        raise AssertionError("Cannot import %s" % imp)

def test_imports():
    for imp in IMPORTS:
        yield check_import, imp
        
