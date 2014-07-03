%define pname PIL
Summary: Python Imaging Library
Name: python27-%{pname}
Version: 1.1.7
Release: 2.ceda%{?dist}
%define tarname Imaging-%{version}
Source0: %{tarname}.tar.gz
Patch0: Imaging-lib64.patch
License: Python (MIT style)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Secret Labs AB (PythonWare) <info@pythonware.com>
Url: http://www.pythonware.com/products/pil
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 libjpeg-turbo
BuildRequires: python27 libjpeg-turbo-devel

%description
Python Imaging Library

%prep
%setup -n %{tarname}
%patch0 -p1

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Apr 28 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1.7-2.ceda
- patch to find libs in /usr/lib64 and add libjpeg dependency

%files -f INSTALLED_FILES
%defattr(-,root,root)
