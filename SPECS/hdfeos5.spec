Summary: HDF-EOS5 libraries
Name: hdfeos5
Version: 1.15
Source0: HDF-EOS5.1.15.tar.Z
Release: 1.ceda%{dist}
License: UNKNOWN
Group: Scientific support
URL: http://hdfeos.org/software
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
BuildRequires: ncompress hdf5-devel
Requires: hdf5

%description

HDF-EOS is a software library designed to support NASA Earth Observing
System (EOS) science data. HDF is the Hierarchical Data Format
developed by the National Center for Supercomputing
Applications. Specific data structures which are containers for
science data are: Grid, Point, Zonal Average and Swath. These data
structures are constructed from standard HDF data objects, using EOS
conventions, through the use of a software library. A key feature of
HDF-EOS is a standard prescription for associating geolocation data
with science data through internal structural metadata. The
relationship between geolocation and science data is transparent to
the end-user. Instrument and data typeindependent services, such as
subsetting by geolocation, can be applied to files across a wide
variety of data products through the same library interface. The
library is extensible and new data structures can be added.  This
document describes a proposed standard for HDF-EOS5 Grid and Swath
structures, which is based on the HDF5 data model and file format,
provided by the HDF Group. The HDF Group was part of the National
Center for Supercomputing Applications (NCSA) until July 2006, at
which time it began full operations as a non-profit 501(c)(3) company.


%prep
rm -fr hdfeos5
tar xvfZ %{SOURCE0}

# per https://github.com/cedadev/jasmin_scivm/issues/44
find hdfeos5 -type f -not -name '*.doc' | xargs perl -p -i -e 's/((-l|lib)Gctp)/${1}5/'

%build
cd hdfeos5
export CFLAGS="-Df2cFortran"
export LDFLAGS="-L/usr/lib64/ -lhdf5" 
export F77=gfortran
export FC=gfortran
%configure --with-pic --enable-install-include
make

%install
cd hdfeos5
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT	
pushd $RPM_BUILD_ROOT/%{_includedir}
mkdir he5
mv *.h he5/
popd

%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%clean				
#rm -rf $RPM_BUILD_ROOT		

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%files
%defattr(-,root,root,-)
%{_includedir}/he5/*.h
%{_libdir}/*.a
%{_libdir}/*.la

%changelog

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.15-1.ceda
- initial build for hdf5 adapting hdfeos(2) RPM 

* Mon Jul 13 2015  <builderdev@builder.jc.rl.ac.uk> - 19.1.00-1.ceda
- update to v19 and compile with Fortran support

* Tue Jan 27 2015  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.

