%define pname pyproj
Summary: Python interface to PROJ.4 library
Name: python27-%{pname}
Version: 1.9.5.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Url: https://github.com/jswhit/pyproj
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

Performs cartographic transformations between geographic (lat/lon)
and map projection (x/y) coordinates. Can also transform directly
from one map projection coordinate system to another.
Coordinates can be given as numpy arrays, python arrays, lists or scalars.
Optimized for numpy arrays.

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
