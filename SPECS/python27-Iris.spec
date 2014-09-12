%define pname iris
%define version 1.7.1
%define release 1.ceda%{?dist}

Summary: A powerful, easy to use, and community-driven Python library for analysing and visualising meteorological and oceanographic data sets
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-v%{version}.tar.gz
License: GPL v3
Group: Scientific support
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UK Met Office
Url: http://scitools.github.com/iris
%define prereq gdal-python27 >= 1.9.1, graphviz-python27 >= 2.18, grib_api-python27 >= 1.9.16, python27-PIL >= 1.1.7, python27-Shapely >= 1.2.14, python27-cartopy >= 0.8.0, python27-matplotlib >= 1.2.0, python27-mock >= 1.0.1, python27-netCDF4 >= 0.9.9, python27-nose >= 1.1.2, python27-numpy >= 1.6, python27-pandas >= 0.11.0, python27-pyke >= 1.1.1, python27-scipy >= 0.10, python27-setuptools >= 0.6c11, udunits >= 2.1.24, python27, python27-Cython, mo_unpack, python27-shapefile python27-biggus >= 0.7.0
Requires: %{prereq}
BuildRequires: %{prereq}


%description
Iris is a powerful, easy to use, community-driven Python library for analysing and visualising meteorological and oceanographic data sets.

The full documentation for Iris, including a user guide, example code, and gallery, is online at:

    * http://scitools.github.com/iris/

# where to put a few changes/copying files
# nothing is really python2.7 specific, but avoid conflict with 
# possible iris package for system python
%define docdir %{_datadir}/iris-py2.7

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py --with-unpack install -O1 --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/usr/iris $RPM_BUILD_ROOT/%{docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 1.6.1-1.ceda%{?dist}
- upgrade to 1.6.1, adding a number of dependencies

* Thu Oct 31 2013  <builderdev@builder.jc.rl.ac.uk> - 1.5.1-2.ceda%{?dist}
- include --with-unpack option

* Thu Oct 17 2013  <builderdev@builder.jc.rl.ac.uk> - 1.5.1-1.ceda%{?dist}
- change to 1.5.1

* Mon Feb 11 2013  <builderdev@builder.jc.rl.ac.uk> - 1.1.0rc1-2.ceda%{?dist}
- add dependencies for python27-scipy, python27-netCDF4

* Mon Dec 17 2012  <builderdev@builder.jc.rl.ac.uk> - 1.1.0rc1-1.ceda{?dist}
- initial version

%files
%defattr(-,root,root)
/usr/lib/python2.7/site-packages/iris
/usr/lib/python2.7/site-packages/Iris-%{version}-py2.7.egg-info
%dir %{docdir}
%doc %{docdir}/CHANGES
%doc %{docdir}/COPYING
%doc %{docdir}/COPYING.LESSER
