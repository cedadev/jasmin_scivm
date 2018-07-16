%define pname iris-grib
Summary: GRIB loading for Iris
Name: python27-%{pname}
Version: 0.13.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UK Met Office <scitools-iris@googlegroups.com>
Url: https://github.com/SciTools/iris-grib
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Iris loading of GRIB files
==========================

With this package, iris is able to load GRIB files:

```
my_data = iris.load(path_to_grib_file)
```

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

* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 0.13.0-1.ceda
- bump version

%files -f INSTALLED_FILES
%defattr(-,root,root)
