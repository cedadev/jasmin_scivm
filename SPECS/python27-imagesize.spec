%define pname imagesize
Summary: Getting image size from png/jpeg/jpeg2000/gif file
Name: python27-%{pname}
Version: 0.7.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Yoshiki Shibukawa <yoshiki at shibu.jp>
Url: https://github.com/shibukawa/imagesize_py
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

It parses image files' header and return image size.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.


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
