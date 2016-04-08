Name: geos
Version: 3.5.0
Release: 2.ceda%{?dist}
License: LGPL v2.1
Group: Development/Libraries
Source: %{name}-%{version}.tar.bz2
URL: http://trac.osgeo.org/geos/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Summary:  Geometry Engine, Open Source
Prefix: /usr

%description					
GEOS - Geometry Engine, Open Source[edit] ¶

GEOS (Geometry Engine - Open Source) is a C++ port of the  Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the  OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.

GEOS is available under the terms of  GNU Lesser General Public License (LGPL), and is a project of  OSGeo.
Capabilities Include

    Geometries: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection
    Predicates: Intersects, Touches, Disjoint, Crosses, Within, Contains, Overlaps, Equals, Covers
    Operations: Union, Distance, Intersection, Symmetric Difference, Convex Hull, Envelope, Buffer, Simplify, Polygon Assembly, Valid, Area, Length,
    Prepared geometries (pre-spatially indexed)
    STR spatial index
    OGC Well Known Text (WKT) and Well Known Binary (WKB) encoders and decoders.
    C and C++ API (C API gives long term ABI stability)
    Thread safe (using the reentrant API) 

%package devel
Group: Development/Libraries	
Summary: Development libraries for GEOS
Requires: geos = %{version}
%description devel
This package contains the libraries needed to build other code requiring 
the library that comes with GEOS...
For further information see the description for the geos (non-devel) package.

%prep
%setup

%build
export CFLAGS="-O1" CXXFLAGS="-O1"
%configure
make				

%install
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT	

%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi


%clean				
rm -rf $RPM_BUILD_ROOT		

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%files				
%defattr(-,root,root)
%{_libdir}/libgeos_c.so.*
%{_libdir}/libgeos-*.so

%files devel
%defattr(-,root,root)
%{_libdir}/libgeos.so
%{_libdir}/libgeos_c.so
%{_libdir}/libgeos.a
%{_libdir}/libgeos_c.a
%{_libdir}/libgeos_c.la
%{_libdir}/libgeos.la
%{_bindir}/geos-config
%{_includedir}/geos
%{_includedir}/geos*.h


%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 3.5.0-2.ceda
- make -devel depend on exact base version

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 3.5.0-1.ceda
- upgrade to 3.5.0

* Tue Jan 22 2013  <builderdev@builder.jc.rl.ac.uk> - 3.3.6-1.ceda
- initial version

