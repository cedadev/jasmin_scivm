%define pname geopandas
Summary: Geographic pandas extensions
Name: python27-%{pname}
Version: 0.3.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: GeoPandas contributors <kjordahl@alum.mit.edu>
Url: http://geopandas.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-pandas python27-Shapely python27-Fiona python27-descartes python27-pyproj python27-six >= 1.11.0
BuildRequires: python27
BuildArch: noarch

%description

GeoPandas is a project to add support for geographic data to
`pandas`_ objects.

The goal of GeoPandas is to make working with geospatial data in
python easier. It combines the capabilities of `pandas`_ and `shapely`_,
providing geospatial operations in pandas and a high-level interface
to multiple geometries to shapely. GeoPandas enables you to easily do
operations in python that would otherwise require a spatial database
such as PostGIS.

.. _pandas: http://pandas.pydata.org
.. _shapely: http://toblerity.github.io/shapely




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
