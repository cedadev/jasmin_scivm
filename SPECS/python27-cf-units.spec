%define pname cf-units
Summary: Python interface to Unidata/UCAR UDUNITS-2 and netcdftime
Name: python27-%{pname}
Version: 2.0.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UK Met Office
Url: https://github.com/SciTools/cf_units
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 udunits python27-six python27-netCDF4 python27-cftime
BuildRequires: python27
Provides: python27-cf_units
Obsoletes: python27-cf_units

%description

Units of measure as required by the Climate and Forecast (CF) metadata
conventions.

Provision of a wrapper class to support Unidata/UCAR UDUNITS-2, and
the netcdftime calendar functionality.

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
* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 2.0.2-1.ceda
- bump version
- change name to python27-cf-units but for compatibility add 
  provides and obsoletes python27-cf_units
- also now no longer 'noarch'
- add cftime dependency

* Thu Jul  6 2017  <builderdev@builder.jc.rl.ac.uk> - 1.1.3-2.ceda
- adding dependencies (six and netCDF4)

* Sun Dec 11 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1.3-1.ceda
- bump version and add udunits dependency

%files -f INSTALLED_FILES
%defattr(-,root,root)
