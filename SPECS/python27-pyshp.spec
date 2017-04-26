%define pname pyshp
Summary: Pure Python read/write support for ESRI Shapefile format
Name: python27-%{pname}
Version: 1.2.10
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Joel Lawhead <jlawhead@geospatialpython.com>
Url: https://github.com/GeospatialPython/pyshp
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch
Obsoletes: python27-shapefile

%description

The Python Shapefile Library (pyshp) provides read and write support for the
Esri Shapefile format. The Shapefile format is a popular Geographic
Information System vector data format created by Esri. For more information
about this format please read the well-written "ESRI Shapefile Technical
Description - July 1998" located at 
http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf . 
The Esri document describes the shp and shx file formats. However a
third file format called dbf is also required. This format is
documented on the web as the "XBase File Format Description" and is a
simple file-based database format created in the 1960's. For more on
this specification see:
http://www.clicketyclick.dk/databases/xbase/format/index.html

Both the Esri and XBase file-formats are very simple in design and memory
efficient which is part of the reason the shapefile format remains popular
despite the numerous ways to store and exchange GIS data available today.

Pyshp is compatible with Python 2.4-3.x.


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
