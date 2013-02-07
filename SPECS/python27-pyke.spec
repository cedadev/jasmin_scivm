%define pname pyke
%define version 1.1.1
%define release 1.ceda%{?dist}

Summary: Python Knowledge Engine and Automatic Python Program Generator
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Bruce Frederiksen <dangyogi@gmail.com>
Url: http://sourceforge.net/projects/pyke
Requires: python27
BuildRequires: python27

%description

        Both forward-chaining and backward-chaining rules (which may include
        python code) are compiled into python. Can also automatically assemble
        python programs out of python functions which are attached to
        backward-chaining rules.

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

* Mon Dec 17 2012  <builderdev@builder.jc.rl.ac.uk> - 1.ceda{?dist}
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
