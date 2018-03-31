%define pname Cython
%define version 0.28.1
%define release 1.ceda%{?dist}

Summary: The Cython compiler for writing C extensions for the Python language.
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{version}.tar.gz
License: Apache License v2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Robert Bradshaw, Stefan Behnel, Dag Seljebotn, Greg Ewing, et al. <cython-devel@python.org>
Url: http://www.cython.org
Requires: python27
BuildRequires: python27

%description

  The Cython language makes writing C extensions for the Python language as
  easy as Python itself.  Cython is a source code translator based on the
  well-known Pyrex_, but supports more cutting edge functionality and
  optimizations.

  The Cython language is very close to the Python language (and most Python
  code is also valid Cython code), but Cython additionally supports calling C
  functions and declaring C types on variables and class attributes. This
  allows the compiler to generate very efficient C code from Cython code.

  This makes Cython the ideal language for writing glue code for external C
  libraries, and for fast C modules that speed up the execution of Python
  code.

  .. _Pyrex: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
  

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
* Sat Mar 31 2018  <builderdev@builder.jc.rl.ac.uk> - 0.28.1-1.ceda%{?dist}
- bump version

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 0.24-1.ceda%{?dist}
- update to 0.24


* Mon Dec 17 2012  <builderdev@builder.jc.rl.ac.uk> - 1.ceda{?dist}
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
