%define pname rpy2
Name: python-%{pname}
Version: 2.2.6
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: AGPLv3.0 (except rpy2.rinterface: LGPL)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Laurent Gautier <lgautier@gmail.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://rpy.sourceforge.net
Summary: Rpy2 is a Python interface to the R language.
Requires: R
BuildRequires: R

%description
About rpy2
==========

Rpy2 is a Python interface to the R language, mainly constitutued
of a low-level interface (rpy2.rinterface) close to R's C-level API
and a high-level interface with convenience classes and features
(rpy2.robjects).

The high-level interface is implemented using the low-level interface
and other high-level interfaces are possible. The original rpy interface
can be implemented with the low-level interface (rpy2.rpy_classic) 



%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
