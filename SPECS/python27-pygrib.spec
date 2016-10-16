%define pname pygrib
Summary: Python module for reading/writing GRIB files
Name: python27-%{pname}
Version: 2.0.1
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Url: https://pypi.python.org/pypi/pygrib
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

GRIB is the the World Meterological Organization (WMO) standard for
distributing gridded data. This module contains a python programmer
interface for reading and writing GRIB grids (editions 1 and 2) using
the ECWMF GRIB API C library.

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

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 2.0.1-2.ceda
- rebuild against grib_api 1.17.0

%files -f INSTALLED_FILES
%defattr(-,root,root)
