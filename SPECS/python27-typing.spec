%define pname typing
Summary: Type Hints for Python
Name: python27-%{pname}
Version: 3.6.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: PSF
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Guido van Rossum, Jukka Lehtosalo, Łukasz Langa <jukka.lehtosalo@iki.fi>
Url: https://docs.python.org/3/library/typing.html
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.6.

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.


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
