%define pname llvmlite
Summary: lightweight wrapper around basic LLVM functionality
Name: python27-%{pname}
Version: 0.6.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Continuum Analytics, Inc. <numba-users@continuum.io>
Url: http://llvmlite.pydata.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 llvm python27-enum34
BuildRequires: python27 llvm-devel python27-enum34
BuildArch: noarch

%description

lightweight wrapper around basic LLVM functionality

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
