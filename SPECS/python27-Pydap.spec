%define pname Pydap
Summary: Pure Python Opendap/DODS client and server.
Name: python27-%{pname}
Version: 3.2.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Roberto De Almeida <rob@pydap.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://pydap.org/
Requires: python27-httplib2 python27-singledispatch python27-WebOb

%description

Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array
and iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.
        

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

* Thu Jul  6 2017  <builderdev@builder.jc.rl.ac.uk> - 3.2.2-1.ceda
- bump version and add dependencies httplib2, singledispatch, WebOb

%files -f INSTALLED_FILES
%defattr(-,root,root)
