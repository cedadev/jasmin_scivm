%define pname ecmwf-api-client
Summary: Python client for ECMWF web services API.
Name: python27-%{pname}
Version: 1.4.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: ECMWF <software.support@ecmwf.int>
Url: https://software.ecmwf.int/stash/projects/PRDEL/repos/ecmwf-api-client/browse
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Python client for ECMWF web services API.

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
