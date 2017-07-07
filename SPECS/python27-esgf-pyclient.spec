%define pname esgf-pyclient
Summary: A library interacting with ESGF services within Python
Name: python27-%{pname}
Version: 0.1.8
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Ag Stephens <Ag.Stephens@stfc.ac.uk>
Url: http://esgf-pyclient.readthedocs.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Top-level package for Python interface to ESGF services.

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
