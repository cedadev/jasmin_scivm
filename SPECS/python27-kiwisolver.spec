%define pname kiwisolver
Summary: A fast implementation of the Cassowary constraint solver
Name: python27-%{pname}
Version: 1.0.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: The Nucleic Development Team <sccolbert@gmail.com>
Url: https://github.com/nucleic/kiwi
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27

%description

Kiwi is an efficient C++ implementation of the Cassowary constraint solving
algorithm. Kiwi is an implementation of the algorithm based on the seminal
Cassowary paper. It is *not* a refactoring of the original C++ solver. Kiwi
has been designed from the ground up to be lightweight and fast. Kiwi ranges
from 10x to 500x faster than the original Cassowary solver with typical use
cases gaining a 40x improvement. Memory savings are consistently > 5x.

In addition to the C++ solver, Kiwi ships with hand-rolled Python bindings.


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

* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 1.0.1-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
