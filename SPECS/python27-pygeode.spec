%define pname pygeode
Summary: Gridded data manipulator for Python
Name: python27-%{pname}
Version: 1.0.4a
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GPL-3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Peter Hitchcock, Andre Erler, Mike Neish <pygeode-users@googlegroups.com>
Url: http://pygeode.github.io
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-netCDF4 python27-numpy python27-basemap
BuildRequires: python27 python27-netCDF4 python27-numpy python27-basemap

%description

PyGeode is a software library intended to simplify the management, analysis,
and visualization of gridded geophysical datasets such as those generated by
climate models. The library provides three main advantages. Firstly, it can
define a geophysical coordinate system for any given dataset, and allows
operations to be carried conceptually in this physical coordinate system, in
a way that is independent of the native coordinate system of a particular
dataset. This greatly simplifies working with datasets from different
sources. Secondly, the library allows mathematical operations to be performed
on datasets which fit on disk but not in memory; this is useful for dealing
with the extremely large datasets generated by climate models, and permits
operations to be performed over networks. Finally, the library provides tools
for visualizing these datasets in a scientifically useful way. The library is
written in Python, and makes use of a number of existing packages to perform
the underlying computations and to create plots.


%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
