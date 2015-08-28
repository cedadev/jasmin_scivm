%define pname dateutil
%define tarname python-%{pname}
Summary: Extensions to the standard Python datetime module
Name: python27-%{pname}
Version: 2.4.2
Release: 1.ceda%{?dist}
Source0: %{tarname}-%{version}.tar.gz
License: Simplified BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Yaron de Leeuw <me@jarondl.net>
Url: https://dateutil.readthedocs.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

The dateutil module provides powerful extensions to the
datetime module available in the Python standard library.

%prep
%setup -n %{tarname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 2.4.2-1.ceda
- init version

%files -f INSTALLED_FILES
%defattr(-,root,root)
