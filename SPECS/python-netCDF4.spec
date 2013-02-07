%define pname netCDF4-python
Summary: Provides an object-oriented python interface to the netCDF version 4 library.
Name: python-netCDF4
Version: 1.0
Release: 2.ceda%{?dist}
Source0: netCDF4-1.0fix1.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html
Requires: python-numpy
BuildRequires: python-numpy

%description
netCDF version 4 has many features not found in earlier versions of the library, such as hierarchical groups, zlib compression, multiple unlimited dimensions, and new data types.  It is implemented on top of HDF5.  This module implements most of the new features, and can read and write netCDF files compatible with older versions of the library.  The API is modelled after Scientific.IO.NetCDF, and should be familiar to users of that module.

This project has a `Subversion repository <http://code.google.com/p/netcdf4-python/source>`_ where you may access the most up-to-date source.

%prep
%setup -n netCDF4-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
