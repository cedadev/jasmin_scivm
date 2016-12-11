%define pname eofs
Summary: EOF analysis in Python
Name: python27-%{pname}
Version: 1.2.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andrew Dawson <dawson@atm.ox.ac.uk>
Url: https://ajdawson.github.com/eofs
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy
BuildRequires: python27 python27-numpy
BuildArch: noarch

%description

eofs is a package for performing EOF analysis on spatial-temporal
data sets, aimed at meteorology, oceanography and climate sciences

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
