%define pname packaging
Summary: Core utilities for Python packages
Name: python27-%{pname}
Version: 17.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD or Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Donald Stufft and individual contributors <donald@stufft.io>
Url: https://github.com/pypa/packaging
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

Core utilities for Python packages


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
