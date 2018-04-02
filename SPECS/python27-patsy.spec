%define pname patsy
Summary: A Python package for describing statistical models and for building design matrices.
Name: python27-%{pname}
Version: 0.5.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: 2-clause BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Nathaniel J. Smith <njs@pobox.com>
Url: https://github.com/pydata/patsy
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy python27-six
BuildRequires: python27
BuildArch: noarch

%description

Patsy is a Python library for describing statistical models
(especially linear models, or models that have a linear component) and
building design matrices. Patsy brings the convenience of `R
<http://www.r-project.org/>`_ "formulas" to Python.

Documentation:
  https://patsy.readthedocs.io/

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
