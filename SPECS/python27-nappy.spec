%define pname nappy
Summary: NASA Ames Processing in Python
Name: python27-%{pname}
Version: 1.1.2
%define svnrel r3637
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}-%{svnrel}.tar.gz
License: BSD
Group: Scientific Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ag Stephens <ag.stephens@stfc.ac.uk>
Url: http://proj.badc.rl.ac.uk/cows/wiki/CowsSupport/Nappy
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27-cdat_lite
BuildRequires: python27 python27-cdat_lite

%description
A python package for reading/writing NASA Ames files, 
writing NASA Ames-style CSV files and converting to/from NetCDF
(if CDMS enabled).

%prep
%setup -n %{pname}-%{version}-%{svnrel}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1.2-2.ceda
- recompile against netcdf 4.4.0


* Thu Feb 13 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1.1-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
