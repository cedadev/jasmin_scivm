%define pname rpy2
Name: python27-%{pname}
Version: 2.3.9
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: AGPLv3.0 (except rpy2.rinterface: LGPL)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Laurent Gautier <lgautier@gmail.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
#Url: http://rpy.sourceforge.net
Url: https://pypi.python.org/pypi/rpy2/
Summary: Rpy2 is a Python interface to the R language.
Requires: python27
BuildRequires: python27
Requires: R >= 3.0
BuildRequires: R >= 3.0

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
export LDFLAGS="-Wl,-rpath,/usr/lib64/R/lib"
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Fri Feb 21 2014  <builderdev@builder.jc.rl.ac.uk> - 2.3.9-1.ceda
- update to 2.3.9 (fixes problems with R 3.0 in earlier rpy versions) and require R 3.0
- update URL from sourceforge to pypi

%files -f INSTALLED_FILES
%defattr(-,root,root)
