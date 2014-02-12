%define pname ocgis
Summary: a Python package for processing climate datasets
Name: python27-%{pname}
Version: 0.07b
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: University of Illinois-NCSA License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: National Oceanic & Atmospheric Administration
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://earthsystemcog.org/projects/openclimategis/
Requires: python27
BuildRequires: python27

%description

OpenClimateGIS Overview

OpenClimateGIS is a Python package designed for geospatial manipulation, subsetting, computation, and translation of climate datasets stored in local NetCDF files or files served through THREDDS data servers. OpenClimateGIS has a straightforward, request-based API that is simple to use yet complex enough to perform a variety of computational tasks. The software is built entirely from open source packages.
OpenClimateGIS is currently in beta and is actively seeking users. (Hurry and get special developer attention!)
 
GIS Capabilities

  *  Subsetting (e.g. intersects and intersection) of climate datasets by bounding box, Shapely geometries, or shapefiles (point or polygon) (e.g. city centroid, a single county or watershed, state boundaries).
  *  Time and level range subsetting.
  *  Single or multi-dataset requests (i.e. concatenation).
  *  Area-weighted aggregation to selection geometries.
  *  Alpha support for projected climate datasets.
  *  Geometry wrapping and unwrapping to maintain logically consistent longitudinal domains.
  *  Polygon and point geometric abstractions.

Data Conversion

  *  Access to local NetCDF data or data hosted remotely on a THREDDS (OPeNDAP protocol) data server. Only the piece of data selected by an area-of-interest is transferred from the remote server.
  *  Stream climate data to multiple formats. Currently supported formats include keyed CSV-shapefile, shapefile, CSV, GeoJSON, NetCDF, and NumPy.
  *  Extensible converter framework to add custom formats.
  *  Automatic generation of request metadata.
  *  Push data to a familiar format to perform analysis or keep the data as NumPy arrays, perform analysis, and dump to a supported format.

Computation

  *  Extensible computational framework for arbitrary inclusion of NumPy-based calculations.
  *  Apply computations to entire data arrays or temporal groups.
  *  Computed data may be streamed to any supported formats.


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

%changelog
* Wed Dec 18 2013  <builderdev@builder.jc.rl.ac.uk> - 0.07b-1.ceda
- initial build
