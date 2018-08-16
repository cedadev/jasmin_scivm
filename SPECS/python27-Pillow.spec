%define pname Pillow
Summary: Python Imaging Library (Fork)
Name: python27-%{pname}
Version: 5.2.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Standard PIL License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Alex Clark (Fork Author) <aclark@aclark.net>
Url: http://python-pillow.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
Provides: python27-PIL
Obsoletes: python27-PIL

%description

Pillow
======

Python Imaging Library (Fork)
-----------------------------

Pillow is the friendly PIL fork by `Alex Clark and Contributors 
<https://github.com/python-pillow/Pillow/graphs/contributors>`_.

PIL is the Python Imaging Library by Fredrik Lundh and Contributors.


More Information
----------------

https://pillow.readthedocs.io/


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

* Thu Aug 16 2018  <builderdev@builder.jc.rl.ac.uk> - 5.2.0-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
