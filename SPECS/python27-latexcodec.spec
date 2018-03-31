%define pname latexcodec
Summary: A lexer and codec to work with LaTeX code in Python.
Name: python27-%{pname}
Version: 1.0.5
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Matthias C. M. Troffaes <matthias.troffaes@gmail.com>
Url: https://github.com/mcmtroffaes/latexcodec
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-six >= 1.4.1
BuildRequires: python27
BuildArch: noarch

%description

A lexer and codec to work with LaTeX code in Python.

* Documentation: http://latexcodec.readthedocs.org/

* Development: http://github.com/mcmtroffaes/latexcodec/

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
