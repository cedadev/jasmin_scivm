%define pname cartopy
%define version 0.14.2
%define release 1.ceda%{?dist}

Summary: a cartographic python library with matplotlib support
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-v%{version}.tar.gz
License: LGPL v3
Group: Scientific support
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UK Met Office
Url: https://github.com/SciTools/cartopy
Requires: python27, python27-matplotlib >= 1.2, proj, python27-Cython
Requires: python27-numpy >= 1.7.0, proj >= 4.9.0
BuildRequires: python27, python27-matplotlib >= 1.2, python27-Cython
BuildRequires: python27-numpy >= 1.7.0, proj-devel >= 4.9.0
BuildRequires: python27-setuptools >= 18.2

%description
A library providing cartographic tools for python.

Some of the key features of cartopy are:

    * object oriented projection definitions
    * point, line, polygon and image transformations between projections
    * integration to expose advanced mapping in matplotlib with a simple and intuitive interface
    * work-in-progress mechanisms for accessing specialist data such as those from the "Shuttle Radar Topography Mission" (SRTM) and the "Global Self-consistent, Hierarchical, High-resolution Shoreline" database (GSHHS).

The latest release documentation for cartopy can be found at here, for other versions see the documentation page.

Cartopy is published under an LGPLv3 licence.

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
* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 0.14.2-1.ceda%{?dist}
- update to 0.14.2, with proj dependency now 4.9.0

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 0.13.0-1.ceda%{?dist}
- update to 0.13

* Thu Jun 20 2013  <builderdev@builder.jc.rl.ac.uk> - 0.7.0-2.ceda%{?dist}
- add numpy >= 1.7.0 dependency

* Thu Dec 20 2012  <builderdev@builder.jc.rl.ac.uk> - 0.5.x-2.ceda%{?dist}
- require matplotlib 1.2


* Mon Dec 17 2012  <builderdev@builder.jc.rl.ac.uk> - 1.1.0rc1-1.ceda{?dist}
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
