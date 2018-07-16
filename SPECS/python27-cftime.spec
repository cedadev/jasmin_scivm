%define pname cftime
Summary: Time-handling functionality from netcdf4-python
Name: python27-%{pname}
Version: 1.0.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Url: https://github.com/Unidata/cftime
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy python27-Cython
BuildRequires: python27

%description

Python library for decoding time units and variable values in a netCDF
file conforming to the Climate and Forecasting (CF) netCDF
conventions.

See https://unidata.github.io/cft

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

* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 1.0.0-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
