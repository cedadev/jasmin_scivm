%define pname iris
%define version 1.1.0rc1
%define release 2.ceda%{?dist}

Summary: A powerful, easy to use, and community-driven Python library for analysing and visualising meteorological and oceanographic data sets
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-v%{version}.tar.gz
License: GPL v3
Group: Scientific support
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: UK Met Office
Url: http://scitools.github.com/iris
Requires: python27, python27-pyke, python27-Cython, python27-cartopy, python27-Shapely, python27-shapefile, python27-scipy, python27-netCDF4
BuildRequires: python27, python27-pyke, python27-Cython, python27-cartopy, python27-Shapely, python27-shapefile, python27-scipy, python27-netCDF4


%description
Iris is a powerful, easy to use, community-driven Python library for analysing and visualising meteorological and oceanographic data sets.

The full documentation for Iris, including a user guide, example code, and gallery, is online at:

    * http://scitools.github.com/iris/

# where to put a few changes/copying files
# nothing is really python2.7 specific, but avoid conflict with 
# possible iris package for system python
%define docdir %{_datadir}/iris-py2.7

%prep
%setup -n %{pname}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/usr/iris $RPM_BUILD_ROOT/%{docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
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
