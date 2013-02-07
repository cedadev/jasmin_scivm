Name: python27-shapefile
Version: 1.1.4
Release: 1.ceda%{?dist}
Source0: shapefile.py
License: http://opensource.org/licenses/mit-license.php
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: jlawhead<at>geospatialpython.com
Url: http://code.google.com/p/pyshp/
Summary: reads and writes ESRI Shapefiles in pure Python

%description

This library reads and writes ESRI Shapefiles in pure Python. You can read and write shp, shx, and dbf files with all types of geometry. Everything in the public ESRI shapefile specification is implemented. This library is compatible with Python versions 2.4 to 3.x.

%define packdir /usr/lib/python2.7/site-packages

%prep

%build

%install
dir=$RPM_BUILD_ROOT%{packdir}
mkdir -p $dir
cp %{SOURCE0} $dir/
python2.7 <<EOF
import sys
sys.path.insert(0, "$dir")
import shapefile
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%{packdir}/shapefile.py
%{packdir}/shapefile.pyc
