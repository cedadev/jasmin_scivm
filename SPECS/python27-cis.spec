%define pname cis
Summary: Community Intercomparison Suite
Name: python27-%{pname}
Version: 1.3.4
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPL 3+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Philip Kershaw <Philip.Kershaw@stfc.ac.uk>
Url: http://www.cistools.net/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-iris
BuildRequires: python27 python27-iris
BuildArch: noarch
Obsoletes: python27-jasmin_cis

%description

CIS is an open source command-line tool for easy collocation,
visualization, analysis, and comparison of diverse gridded and
ungridded datasets used in the atmospheric sciences. Visit our
homepage at www.cistools.net.

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build
python2.7 setup.py test

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.3.4-1.ceda
- update to 1.3.4


* Sat Nov  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.2.1-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
