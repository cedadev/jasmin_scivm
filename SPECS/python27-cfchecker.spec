%define pname cfchecker
Summary: The NetCDF Climate Forcast Conventions compliance checker
Name: python27-%{pname}
Version: 2.0.5
Release: 1.ceda%{?dist}
Source0: %{pname}-3c3031d.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rosalyn Hatcher <r.s.hatcher@reading.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://cf-pcmdi.llnl.gov/conformance/compliance-checker/
Requires: python27-cdat_lite
BuildRequires: python27-cdat_lite
Requires: python27
BuildRequires: python27

%description

The NetCDF Climate Forcast Conventions compliance checker

%prep
%setup -n cf-checker

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog

* Thu Nov 14 2013  <builderdev@builder.jc.rl.ac.uk> - 2.0.5-1.ceda
- initial build
