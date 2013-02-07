%define pname Shapely
%define version 1.2.16
%define release 2.ceda%{?dist}

Summary: Geometric objects, predicates, and operations
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Sean Gillies <sean.gillies@gmail.com>
Url: https://github.com/Toblerity/Shapely
Requires: python27, geos >= 3.3.6
BuildRequires: python27, geos-devel >= 3.3.6


%description

======
README
======

PostGIS-ish operations outside a database context for Pythoneers and
Pythonistas.

.. image:: images/4511827859_b5822043b7_o.png
   :width: 800
   :height: 400

Shapely is a BSD-licensed Python package for manipulation and analysis of
planar geometric objects. It is based on the widely deployed GEOS_ (the engine
of PostGIS_) and JTS_ (from which GEOS is ported) libraries. This C dependency
is traded for the ability to execute with blazing speed. Shapely is not
concerned with data formats or coordinate systems, but can be readily
integrated with packages that are. For more details, see:

* Shapely wiki_
* Shapely manual_
* Shapely `example apps`_

Dependencies
============

Shapely 1.2 depends on:

* Python >=2.5,<3
* libgeos_c >=3.1 (3.0 and below have not been tested, YMMV)

Installation
============

Windows users should use the executable installer, which contains the required
GEOS DLL. Other users should acquire libgeos_c by any means, make sure that it
is on the system library path, and install from the Python package index::

  $ pip install Shapely

or from a source distribution with the setup script::

  $ python setup.py install

Usage
=====

Here is the canonical example of building an approximately circular patch by
buffering a point::

  >>> from shapely.geometry import Point
  >>> patch = Point(0.0, 0.0).buffer(10.0)
  >>> patch
  <shapely.geometry.polygon.Polygon object at 0x...>
  >>> patch.area
  313.65484905459385

See the manual_ for comprehensive usage snippets and the dissolve.py and
intersect.py `example apps`_.

Integration 
===========

Shapely does not read or write data files, but it can serialize and deserialize
using several well known formats and protocols. The shapely.wkb and shapely.wkt
modules provide dumpers and loaders inspired by Python's pickle module.::

  >>> from shapely.wkt import dumps, loads
  >>> dumps(loads('POINT (0 0)'))
  'POINT (0.0000000000000000 0.0000000000000000)'

All linear objects, such as the rings of a polygon (like ``patch`` above),
provide the Numpy array interface.::

  >>> from numpy import asarray
  >>> ag = asarray(patch.exterior)
  >>> ag
  array([[  1.00000000e+01,   0.00000000e+00],
         [  9.95184727e+00,  -9.80171403e-01],
         [  9.80785280e+00,  -1.95090322e+00],
         ...
         [  1.00000000e+01,   0.00000000e+00]])

That yields a numpy array of [x, y] arrays. This is not always exactly what one
wants for plotting shapes with Matplotlib (for example), so Shapely 1.2 adds
a `xy` property for obtaining separate arrays of coordinate x and y values.::

  >>> x, y = patch.exterior.xy
  >>> ax = asarray(x)
  >>> ax
  array([  1.00000000e+01,   9.95184727e+00,   9.80785280e+00,  ...])

Numpy arrays can also be adapted to Shapely linestrings::

  >>> from shapely.geometry import asLineString
  >>> asLineString(ag).length
  62.806623139095073
  >>> asLineString(ag).wkt
  'LINESTRING (10.0000000000000000 0.0000000000000000, ...)'

Testing
=======

Shapely uses a Zope-stye suite of unittests and doctests, exercised via
setup.py.::

  $ python setup.py test

Nosetests won't run the tests properly; Zope doctest suites are not currently
supported well by nose.

Support
=======

Bugs may be reported and questions asked via https://github.com/Toblerity/Shapely.



.. _JTS: http://www.vividsolutions.com/jts/jtshome.htm
.. _PostGIS: http://postgis.org
.. _GEOS: http://trac.osgeo.org/geos/
.. _example apps: http://trac.gispython.org/lab/wiki/Examples
.. _wiki: http://trac.gispython.org/lab/wiki/Shapely
.. _manual: http://toblerity.github.com/shapely/manual.html
.. _Pleiades: http://pleiades.stoa.org


Credits
=======

Shapely is written by:

* Sean Gillies
* Aron Bierbaum
* Kai Lautaportti
* Oliver Tonnhofer

Patches contributed by:

* Howard Butler
* Fr |eaigue| d |eaigue| ric Junod
* Eric Lemoine
* Jonathan Tartley
* Kristian Thy
* Mike Toews (https://github.com/mwtoews)

Additional help from:

* Justin Bronn (GeoDjango) for ctypes inspiration
* Martin Davis (JTS)
* Jaakko Salli for the Windows distributions
* Sandro Santilli, Mateusz Loskot, Paul Ramsey, et al (GEOS Project)

Major portions of this work were supported by a grant (for Pleiades_) from the
U.S. National Endowment for the Humanities (http://www.neh.gov).

.. |eaigue| unicode:: U+00E9
   :trim:
.. _Pleiades: http://pleiades.stoa.org

Changes
=======

1.2.16 (2012-09-18)
-------------------
- Add ops.unary_union function.
- Alias ops.cascaded_union to ops.unary_union when GEOS CAPI >= (1,7,0).
- Add geos_version_string attribute to shapely.geos.
- Ensure parent is set when child geometry is accessed.
- Generate _speedups.c using Cython when building from repo when missing,
  stale, or the build target is "sdist".
- The is_simple predicate of invalid, self-intersecting linear rings now
  returns ``False``.
- Remove VERSION.txt from repo, it's now written by the distutils setup script
  with value of shapely.__version__.

1.2.15 (2012-06-27)
-------------------
- Eliminate numerical sensitivity in a method chaining test (Debian bug
  #663210).
- Account for cascaded union of random buffered test points being a polygon
  or multipolygon (Debian bug #666655).
- Use Cython to build speedups if it is installed.
- Avoid stumbling over SVN revision numbers in GEOS C API version strings.

1.2.14 (2012-01-23)
-------------------
- A geometry's coords property is now sliceable, yielding a list of coordinate
  values.
- Homogeneous collections are now sliceable, yielding a new collection of the
  same type.

1.2.13 (2011-09-16)
-------------------
- Fixed errors in speedups on 32bit systems when GEOS references memory above
  2GB.
- Add shapely.__version__ attribute.
- Update the manual.

1.2.12 (2011-08-15)
-------------------
- Build Windows distributions with VC7 or VC9 as appropriate.
- More verbose report on failure to speed up.
- Fix for prepared geometries broken in 1.2.11.
- DO NOT INSTALL 1.2.11

1.2.11 (2011-08-04)
-------------------
- Ignore AttributeError during exit.
- PyPy 1.5 support.
- Prevent operation on prepared geometry crasher (#12).
- Optional Cython speedups for Windows.
- Linux 3 platform support.

1.2.10 (2011-05-09)
-------------------
- Add optional Cython speedups.
- Add is_cww predicate to LinearRing.
- Add function that forces orientation of Polygons.
- Disable build of speedups on Windows pending packaging work.

1.2.9 (2011-03-31)
------------------
- Remove extra glob import.
- Move examples to shapely.examples.
- Add box() constructor for rectangular polygons.
- Fix extraneous imports.

1.2.8 (2011-12-03)
------------------
- New parallel_offset method (#6).
- Support for Python 2.4.

1.2.7 (2010-11-05)
------------------
- Support for Windows eggs.

1.2.6 (2010-10-21)
------------------
- The geoms property of an empty collection yields [] instead of a ValueError
  (#3).
- The coords and geometry type sproperties have the same behavior as above.
- Ensure that z values carry through into products of operations (#4).

1.2.5 (2010-09-19)
------------------
- Stop distributing docs/_build.
- Include library fallbacks in test_dlls.py for linux platform.

1.2.4 (2010-09-09)
------------------
- Raise AttributeError when there's no backend support for a method.
- Raise OSError if libgeos_c.so (or variants) can't be found and loaded.
- Add geos_c DLL loading support for linux platforms where find_library doesn't
  work.

1.2.3 (2010-08-17)
------------------
- Add mapping function.
- Fix problem with GEOSisValidReason symbol for GEOS < 3.1.

1.2.2 (2010-07-23)
------------------
- Add representative_point method.

1.2.1 (2010-06-23)
------------------
- Fixed bounds of singular polygons.
- Added shapely.validation.explain_validity function (#226).

1.2 (2010-05-27)
----------------
- Final release.

1.2rc2 (2010-05-26)
-------------------
- Add examples and tests to MANIFEST.in.
- Release candidate 2.

1.2rc1 (2010-05-25)
-------------------
- Release candidate.

1.2b7 (2010-04-22)
------------------
- Memory leak associated with new empty geometry state fixed.

1.2b6 (2010-04-13)
------------------
- Broken GeometryCollection fixed.

1.2b5 (2010-04-09)
------------------
- Objects can be constructed from others of the same type, thereby making
  copies. Collections can be constructed from sequences of objects, also making
  copies.
- Collections are now iterators over their component objects.
- New code for manual figures, using the descartes package.

1.2b4 (2010-03-19)
------------------
- Adds support for the "sunos5" platform.

1.2b3 (2010-02-28)
------------------
- Only provide simplification implementations for GEOS C API >= 1.5.

1.2b2 (2010-02-19)
------------------
- Fix cascaded_union bug introduced in 1.2b1 (#212).

1.2b1 (2010-02-18)
------------------
- Update the README. Remove cruft from setup.py. Add some version 1.2 metadata
  regarding required Python version (>=2.5,<3) and external dependency
  (libgeos_c >= 3.1).

1.2a6 (2010-02-09)
------------------
- Add accessor for separate arrays of X and Y values (#210).

TODO: fill gap here

1.2a1 (2010-01-20)
------------------
- Proper prototyping of WKB writer, and avoidance of errors on 64-bit systems
  (#191).
- Prototype libgeos_c functions in a way that lets py2exe apps import shapely
  (#189).

1.2 Branched (2009-09-19)

1.0.12 (2009-04-09)
-------------------
- Fix for references held by topology and predicate descriptors.

1.0.11 (2008-11-20)
-------------------
- Work around bug in GEOS 2.2.3, GEOSCoordSeq_getOrdinate not exported properly
  (#178).

1.0.10 (2008-11-17)
-------------------
- Fixed compatibility with GEOS 2.2.3 that was broken in 1.0.8 release (#176).

1.0.9 (2008-11-16)
------------------
- Find and load MacPorts libgeos.

1.0.8 (2008-11-01)
------------------
- Fill out GEOS function result and argument types to prevent faults on a
  64-bit arch.

1.0.7 (2008-08-22)
------------------
- Polygon rings now have the same dimensions as parent (#168).
- Eliminated reference cycles in polygons (#169).

1.0.6 (2008-07-10)
------------------
- Fixed adaptation of multi polygon data.
- Raise exceptions earlier from binary predicates.
- Beginning distributing new windows DLLs (#166).

1.0.5 (2008-05-20)
------------------
- Added access to GEOS polygonizer function.
- Raise exception when insufficient coordinate tuples are passed to LinearRing
  constructor (#164).

1.0.4 (2008-05-01)
------------------
- Disentangle Python and topological equality (#163).
- Add shape(), a factory that copies coordinates from a geo interface provider.
  To be used instead of asShape() unless you really need to store coordinates
  outside shapely for efficient use in other code.
- Cache GEOS geometries in adapters (#163).

1.0.3 (2008-04-09)
------------------
- Do not release GIL when calling GEOS functions (#158).
- Prevent faults when chaining multiple GEOS operators (#159).

1.0.2 (2008-02-26)
------------------
- Fix loss of dimensionality in polygon rings (#155).

1.0.1 (2008-02-08)
------------------
- Allow chaining expressions involving coordinate sequences and geometry parts
  (#151).
- Protect against abnormal use of coordinate accessors (#152).
- Coordinate sequences now implement the numpy array protocol (#153).

1.0 (2008-01-18)
----------------
- Final release.

1.0 RC2 (2008-01-16)
--------------------
- Added temporary solution for #149.

1.0 RC1 (2008-01-14)
--------------------
- First release candidate

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Wed Jan 23 2013  <builderdev@builder.jc.rl.ac.uk> - 1.2.16-2.ceda%{?dist}
- require geos 3.3.6 (in order to use version built on JASMIN instead of one taken from Fedora)

* Mon Dec 17 2012  <builderdev@builder.jc.rl.ac.uk> - 1.1.0rc1-1.ceda{?dist}
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
