%define pname pyzmq
Summary: Python bindings for 0MQ.
Name: python27-%{pname}
Version: 2.2.0.1
Release: 3.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPL+BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Brian E. Granger, Min Ragan-Kelley <zeromq-dev@lists.zeromq.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://github.com/zeromq/pyzmq
Requires: python27
BuildRequires: python27

%description

PyZMQ is the official Python bindings for the lightweight and super-fast messaging
library ZeroMQ (http://www.zeromq.org).


%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build --zmq=bundled

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Jan 21 2013  <builderdev@builder.jc.rl.ac.uk> - 2.2.0.1-3.ceda
- no real difference - just testing package building

%files -f INSTALLED_FILES
%defattr(-,root,root)
