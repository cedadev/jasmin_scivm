%define pname cdat_lite
Summary: Core components of the Climate Data Analysis tools.  This software is based on CDAT-6.0.alpha-ge3b1a45 and cdunfpp0.13.
Name: python27-%{pname}
Version: 6.0rc2
%define git_sha 5b1b1dd
Release: 7.ceda%{?dist}
#Source0: %{pname}-%{version}.tar.gz
Source0: %{pname}-%{git_sha}.tar.gz
License: http://www-pcmdi.llnl.gov/software-portal/cdat/docs/cdat-license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Stephen Pascoe <Stephen.Pascoe@stfc.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://proj.badc.rl.ac.uk/ndg/wiki/CdatLite
Requires: python27
BuildRequires: python27
BuildRequires: python27-setuptools

%description
=========
cdat-lite
=========

.. contents::

.. sectnum::

Cdat-lite is a Python package for managing and analysing climate
science data.  It is a subset of the Climate Data Analysis Tools
(CDAT_) developed by PCMDI_ at Lawrence Livermore National Laboratory.

Cdat-lite aims to complement CDAT by focusing on its core data
management and analysis components and by offering a radically
different installation system to CDAT.  As a result it is much more
lightweight (hence the name): CDAT's source distribution is the order
of 1Gb whereas cdat-lite is under 5Mb.

Cdat-lite is designed to work with the `CF checker`_ package.

.. _CDAT: http://www2-pcmdi.llnl.gov/cdat
.. _PCMDI: http://www2-pcmdi.llnl.gov/
.. _`CF checker`: http://pypi.python.org/pypi/cfchecker


cdat-lite versioning
====================

Cdat-lite is a project that tracks versions of 2 other projects (CDAT
and cdunifpp).  From version 6.0rc1 the cdat-lite version will not be
based directly on the CDAT version.  This is because CDAT updates its
version very seldom and stays as an "alpha" distribution for long
periods when the parts included in cdat-lite are generally stable.

Full details of which versions of CDAT and cdunifpp a cdat-lite
distribution includes is available in the setup.py file and the
PKG_INFO metadata.

Installing cdat-lite
====================

cdat-lite is distributed as a tarball available from the `cdat-lite
homepage`_ on the `NERC Data Grid wiki` .  It is also installable
using the ``easy_install`` tool.  If you are familiar with
``easy_install`` try this super-quick installation recipe::

  $ export NETCDF_HOME=/usr/local/netcdf
  # Required if using a NetCDF4 compiled with HDF5
  $ export HDF5_HOME=/usr/local/hdf5
  $ easy_install cdat_lite 


Dependencies
------------

To install cdat-lite you will need:

 1. `Python 2.5.x`_.  cdat-lite has not been tested on 2.6 but may
 work (feedback would be gratefully received).  It is unlikely to work on 3.0.

 2. `setuptools`_.  cdat-lite will attempt to download and install
 setuptools if it is missing but it is safer to install it first.

 3. `NetCDF-3.x`_ or greater.  cdat-lite should work with any
 relatively modern NetCDF3 installation on your system provided it is
 compiled as a shared library.  It will also work with NetCDF4
 configured in various different ways, including embedded OPeNDAP
 mode.

 4. If you want to run the short test suite you will need nose_

.. _`Python 2.5.x`: http://www.python.org/download/releases/2.5.4
.. _`setuptools`: http://pypi.python/org/setuptools
.. _`NetCDF-3.x`: http://www.unidata.ucar.edu/software/netcdf/
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/

Selecting your NetCDF installation
----------------------------------

cdat-lite will work with NetCDF3 or NetCDF4 but because it is
referenced by shared libraries (the python C extension modules) it
must be compiled as position independent code.  If you have a NetCDF4
installation you almost certainly are using shared libraries and even
if you wish to use NetCDF3 it is probably easiest to install NetCDF as
a shared library (use ``--enable-shared`` in the NetCDF ``configure``
script).  Alternatively, you can configure NetCDF with::

  $ ./configure --with-pic ...

If you are using NetCDF4 you will also need to configure HDF5 with ``--enable-shared`` or ``--with-pic``.

If you have the command ``nc-config`` in your path cdat-lite will
detect all library and include dependencies.  Otherwise cdat-lite will
look for a NetCDF installation in several places.

If your NetCDF is installed somewhere unusual, or if you want to
select a specific installation, set the NETCDF_HOME variable.  E.g.::

  # sh users
  $ export NETCDF_HOME=/usr/local/netcdf
  # csh users
  $ setenv NETCDF_HOME /usr/local/netcdf

If you are using NetCDF4 cdat-lite will also look for your HDF5
installation which you can configure in a similar way::

  # sh users
  $ export HDF5_HOME=/usr/local/hdf5
  # csh users
  $ setenv HDF5_HOME /usr/local/hdf5

For compatibility with the ``netcdf4-python`` package cdat-lite also accepts ``NETCDF4_DIR`` AND ``HDF5_DIR`` as synonims for these environment variables.

Note, you don't need these environment variables set to run cdat_lite,
although the libraries must be findable by your system's dynamic
linker.  This can be configured by setting ``LD_LIBRARY_PATH`` or using ``ldconfig``.

Running the installer
---------------------

If you have all the dependencies in place you can try using
``easy_install`` to automatically download and install cdat_lite.  Make sure you have access to the internet, with the appropriate HTTP proxy settings, and do::

  $ easy_install cdat-lite

Alternatively you might want to see what you are installing :-).  In
this case either download the tarball__ or use ``easy_install`` to do it for you::

  $ easy_install -eb . cdat-lite
  # The cdat-lite tarball will be downloaded unpacked into you current directory

Now from the distribution directory run the build and install steps separately::

  $ python2.7 setup.py bdist_egg
  $ easy_install dist/cdat-lite*.egg

__ `cdat-lite homepage`_


.. _`installing locally`:

Installing as an unprivileged user
----------------------------------

If you don't have write access to your python distribution you can use
the tool virtualenv_ to create a local python environment with
its own ``easy_install`` executable which you can then use to install
cdat-lite.  In combination with ``NETCDF_HOME``, ``HDF5_HOME`` and
``LD_LIBRARY_PATH`` it should be possible to install all dependencies
of cdat-lite locally.  See the virtualenv_ for details on
installation or try this recipe after downloading the virtualenv::

  # From virtualenv distribution directory
  $ ./virtualenv.py <virtualenv-path>
  $ cd <virtualenv-path>
  $ source bin/activate
  (venv)$ easy_install cdat-lite

.. _virtualenv: http://pypi.python.org/pypi/virtualenv


Platform-specific installation notes
------------------------------------

OS X
''''

Christopher Lee contributed the following experiences installing on OS X 10.6.7.

My particular Macbook has an Intel CPU, and the default on the Mac is
to compile for the architecture x86_64. In order to override this
(because python is 32 bit, and the netcdf libraries I use are also 32
bit) I needed to pass in "-arch i386" to the compiler. I also needed
the little endian flag '-DBYTESWAP' when compiling the netcdf
interface (inside libcdms). The -DBYTESWAP flag should be included by
the libcdms configure script, where there is a section for 'darwin'
(OS X), but it's currently configured without BYTESWAP (line
6182). The problem here is that OS X used to run on PowerPC CPUs,
which don't need the BYTESWAP flag. I'm not sure if this is your
configure script or if it's from the cdat package.

I included the -arch i386 and -DBYTESWAP in the setup.py in the
libcdms section, and the setup works fine.

After running python2.7 setup.py build ; python setup.py install ; I
still get an error when importing cdms2. This problem is caused by the
way that libcdms is linked to the netcdf libraries. The 'normal' Mac
method is to link with absolute paths, but libcdms is linked with
relative paths (the libraries are references with @rpath). The result
is that LD_LIBRARY_PATH environment variable is often empty. I'm not
sure how to fix this in the 'Mac' way with absolute paths, but I added
my $NETCDF_HOME/lib directory to the variable and cdms2 now imports
without error.


Testing the installation
========================

cdat-lite ships with a small set of tests designed to verify that it
has been built successfuly.  These tests require the testing framework
nose_.  Once cdat-lite is installed just run::

  $ nosetests cdat_lite

When run from cdat-lite's distribution directory nosetests will run
slightly differently, running some tests that are known to fail at the
moment.  To disable this behaviour do:

  $ nosetests --config=''

.. _`cdat-lite homepage`: http://proj.badc.rl.ac.uk/ndg/wiki/CdatLite
.. _`NERC Data Grid wiki`: http://proj.badc.rl.ac.uk/ndg/wiki



FAQ
===

What is CDAT?
-------------

CDAT_ is a large suite of open source tools distributed by PCMDI_ for
the management and analysis of climate data.  It includes several
visualisation components and the graphical user interface VCDAT.

What is the difference between CDAT and cdat-lite?
--------------------------------------------------

Differences between CDAT and cdat-lite can be classified as
differences in scope, i.e. which packages are included, and installation system.

cdat-lite contains the 'cdms2' package and a few related
packages.  It does not include the 'vcs' visualisation package or the
VCDAT graphical user interface.  As of v5.1.1-0.3pre3 the included
packages are:

 * cdms2

 * cdtime

 * cdutil

 * genutil

 * ncml

 * Properties

 * regrid2

 * unidataa

 * xmgrace

CDAT bundles virtually all dependencies together in its source
distribution -- even Python itself.  This has its advantages as it
simplifies satisfying dependencies and avoids version conflicts
between dependencies.  However, if you want to integrate CDAT's data
management components into your existing Python architecture CDAT can
be overkill.


What has changed between cdat-lite-4.x and cdat-lite-5.x?
---------------------------------------------------------

If you are a cdat-lite-4 user (or a CDAT 4 user) you have a big
migration job on your hands.  CDAT-4 uses the ``Numeric`` package for
arrays which has been out of date and unmaintained for a long time
now.  It is known to have problems on 64bit architectures.

How does cdat-lite track changes to CDAT?
-----------------------------------------

cdat-lite tries to release major new versions shortly after new
versions of CDAT.  Sometimes CDAT-trunk contains important fixes that
should be applied so that the latest cdat_lite can run ahead of
official CDAT releases (although sometimes CDAT recommends you build
from trunk anyway).

The one exception is the UK Met. Office PP file support which is
usually updated in cdat_lite before CDAT.  In all cases the exact
build versions of CDAT and cdunifpp will be stated in the
distribution's ``setup.py`` file.

How can I use CMOR2 with cdat-lite?
-----------------------------------

We are interested to hear any with experience of using CMOR2 with
cdat-lite but it should be as simple as downloading the distribution
and installing it in parallel with::

  # From the CMOR install directory
  $ python2.7 setup.py install

How can I use OPeNDAP with cdat-lite?
-------------------------------------

OPeNDAP support is an experimental feature of cdat-lite at the moment.
Unlike CDAT you don't select OPeNDAP explicitly during installation
but cdat-lite will inherit any OPeNDAP support embedded into the
NetCDF4 library.  Recent beta releases of NetCDF4 provides a switch to
transparently use OPeNDAP.

How do I install cdat-lite as an unprivileged user?
---------------------------------------------------

See `installing locally`_

Which versions of NetCDF does cdat-lite support?
------------------------------------------------

TODO


%package -n libcdms
Group: Development/Libraries	
Summary: libcdms library from CDAT
%description -n libcdms
This package contains the libcdms library from CDAT. cdat_lite will work without it, but it can be used in conjuction with CMOR.


%prep
%setup -n %{pname}

# use separate copy of sources for standalone libcdms build so that make does not 
# interfere with later 'make install' of the python package
cp -r libcdms libcdms_copy

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

# build libcdms
pushd libcdms_copy

# Use temporary install directory in prefix. Fortunately this works (no hard-coded
# paths to this directory get made inside the package), and gets around the fact that
# DESTDIR is not supported on make install.
./configure --prefix=$RPM_BUILD_ROOT/usr --with-pic
make
popd

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# install standalone libcdms
pushd libcdms_copy
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
mkdir -p `dirname $RPM_BUILD_ROOT/%{_mandir}`
# mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/usr/man/man3

# exclude cddump - keep the copy from the python package
%define cddump $RPM_BUILD_ROOT/%{_bindir}/cddump
mv %{cddump} %{cddump}.orig
make install
mv %{cddump}.orig %{cddump}

# rename dirs to standard locations
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%{_mandir}
mv $RPM_BUILD_ROOT/usr/lib/libcdms.a $RPM_BUILD_ROOT/%{_libdir}/

# add cdmsint.h because CMOR wants it
cp include/cdmsint.h $RPM_BUILD_ROOT/%{_includedir}

popd


%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%files -n libcdms
%{_includedir}/cddrs.h
%{_includedir}/drscdf.h
%{_includedir}/cdunif.h
%{_includedir}/cdms.inc
%{_includedir}/cdms.h
%{_includedir}/cdmsint.h
%{_includedir}/fcddrs.h
%{_libdir}/libcdms.a
%{_bindir}/cudump
%{_bindir}/cdfile
%{_bindir}/cdimport
%{_bindir}/cuget
%doc %{_mandir}/man3/cddrs.3.gz
%doc %{_mandir}/man3/cdms.3.gz
%doc %{_mandir}/man3/cdtime.3.gz
%doc %{_mandir}/man3/fcddrs.3.gz
%doc %{_mandir}/man3/cdunif.3.gz


%changelog
* Mon Sep 25 2017  <builderdev@builder.jc.rl.ac.uk> - 6.0rc2-7.ceda
- compile against later hdf5

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 6.0rc2-5.ceda
- rebuild against netcdf 4.4.0
- add standalone libcdms package

* Mon Feb 10 2014  <builderdev@builder.jc.rl.ac.uk> - 6.0rc2-4.ceda
- update to git tag 5b1b1dd - uses 64-bit data types to cope with some large files

* Wed Feb  5 2014  <builderdev@builder.jc.rl.ac.uk> - 6.0rc2-3.ceda
- update to git tag 9c049bd; this contains bug fixes to cdunifpp although not yet tagged as new cdat_lite version
