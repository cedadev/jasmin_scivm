%define pname sympy
Summary: Computer algebra system (CAS) in Python
Name: python27-%{pname}
Version: 1.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: SymPy development team <sympy@googlegroups.com>
Url: http://sympy.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-mpmath
BuildRequires: python27
BuildArch: noarch

%description


SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as simple
as possible in order to be comprehensible and easily extensible.  SymPy is
written entirely in Python. It depends on mpmath, and other external libraries
may be optionally for things like plotting support.

See the webpage for more information and documentation:

    http://sympy.org

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
perl -p -i -e 's,^/usr/man/,/usr/share/man/,; s/$/.gz/ if m{^/usr/share/man/man(.*?)/.*\.\1$}' INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 1.2-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
