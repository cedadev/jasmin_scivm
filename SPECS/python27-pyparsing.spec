%define pname pyparsing
Summary: Python parsing module
Name: python27-%{pname}
Version: 2.0.3
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT License0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Paul McGuire <ptmcg@users.sourceforge.net>
Url: http://pyparsing.wikispaces.com/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

@DESCRIPTION@

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

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 2.0.3-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
