%define vmaj 18
%define vmin 1.00

Summary: HDF-EOS2 libraries
Name: hdfeos2
Version: %{vmaj}.%{vmin}
Source0: HDF-EOS2.%{vmaj}v%{vmin}.tar.Z
Release: 1.ceda%{dist}
License: UNKNOWN
Group: Scientific support
URL: http://hdfeos.org/software
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
BuildRequires: ncompress hdf-devel
Requires: hdf-devel

%description

Description: The HDF-EOS2 is a software library designed built on
HDF4* to support EOS-specific data structures, namely Grid, Point, and
Swath. The new data structures are constructed from standard HDF data
objects, using EOS conventions, through the use of a software
library. A key feature of HDF-EOS files is that instrument-independent
services, such as subsetting by geolocation, can be applied to the
files across a wide variety of data products.

%prep
rm -fr hdfeos
tar xvfZ %{SOURCE0}

%build
cd hdfeos
export CFLAGS="-I/usr/include/hdf"
export LDFLAGS="-L/usr/lib64/hdf" 
%configure --with-pic --enable-install-include
make

%install
cd hdfeos
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
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Tue Jan 27 2015  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.

