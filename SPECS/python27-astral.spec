%define pname astral
Summary: Calculations for the position of the sun and moon.
Name: python27-%{pname}
Version: 1.4
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.zip
License: Apache-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Simon Kennedy <sffjunkie+code@gmail.com>
Url: https://github.com/sffjunkie/astral
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Calculations for the position of the sun and moon.

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
