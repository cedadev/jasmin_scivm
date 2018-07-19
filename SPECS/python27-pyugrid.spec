%define pname pyugrid
Summary: A package for working with triangular unstructured grids, and the data on them
Name: python27-%{pname}
Version: 0.3.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Chris Barker, Chris Calloway, Rich Signell <Chris.Barker@noaa.gov>
Url: https://github.com/pyugrid/pyugrid
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy >= 1.11 python27-scipy python27-netCDF4 >= 1.2
BuildRequires: python27
BuildArch: noarch

%description

A Python API to utilize data written using the netCDF unstructured
grid conventions:
[(UGRID)](https://github.com/ugrid-conventions/ugrid-conventions).


Background
----------

For many years, folks in the met-ocean community have been able to exchange data,
model results, etc using the [CF Conventions](http://cfconventions.org/).

However, the Convention does not specify standard ways to work with results
from unstructured grid models.  The UGRID effort is an attempt to remedy that.

This package is a Python implementation of the data model specified by the UGRID project.

It provides code that reads and writes UGRID-compliant netCDF files, a start on
code to read/write other formats, and code to work with unstructured grids.


Status
------

**NOTE:** This may be the last release of pyugrid -- continued development will be taking place as part of the "gridded" project:  https://github.com/NOAA-ORR-ERD/gridded

The package currently covers triangular mesh grids, quad grids, and mixed traingle/quad grids.

It provides some limited functionality for manipulating and visualizing the data.

It provides functionality for accessing and interpolating fields on the Grid.

It also provides the ability to read and write netCDF files, and provides a basic
structure an API for adding capability.

Development is managed on GitHub:

https://github.com/pyugrid/pyugrid/






%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
