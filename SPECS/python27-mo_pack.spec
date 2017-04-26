%define pname mo_pack
Summary: Python wrapper to libmo_unpack
Name: python27-%{pname}
Version: 0.2.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Met Office
Url: https://github.com/SciTools/mo_pack
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 mo_unpack
BuildRequires: python27

%description

A python module containing packing methods used to encode and decode the data payloads of UM "fields".

Supports WGDOS and RLE encoding methods.

This is a wrapper to the C library "libmo_unpack", which must also be installed.
See at : https://github.com/SciTools/libmo_unpack

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
