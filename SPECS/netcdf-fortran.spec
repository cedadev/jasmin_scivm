%global netcdf_version 4.3.1

Name: netcdf-fortran
Version: 4.2
Release: 2.ceda%{?dist}
License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
Group: Scientific support	
Source: netcdf-fortran-%{version}.tar.gz	
URL: http://www.unidata.ucar.edu/software/netcdf/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, hdf5-devel, zlib-devel, openssl-devel, netcdf, gcc-gfortran, libgfortran
BuildRequires: netcdf-devel = %{netcdf_version}

Requires: hdf5, zlib, openssl, libgfortran
Requires: netcdf = %{netcdf_version}, netcdf-devel = %{netcdf_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  Fortran bindings for netCDF
Prefix: /usr

%description					

NetCDF (network Common Data Form) is a set of interfaces for array-oriented data access and a freely-distributed collection of data access libraries for C, Fortran, C++, Java, and other languages. The netCDF libraries support a machine-independent format for representing scientific data. Together, the interfaces, libraries, and format support the creation, access, and sharing of scientific data.

NetCDF data is:

    * Self-Describing. A netCDF file includes information about the data it contains.
    * Portable. A netCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.
    * Scalable. A small subset of a large dataset may be accessed efficiently.
    * Appendable. Data may be appended to a properly structured netCDF file without copying the dataset or redefining its structure.
    * Sharable. One writer and multiple readers may simultaneously access the same netCDF file.
    * Archivable. Access to all earlier forms of netCDF data will be supported by current and future versions of the software.

The netCDF software was developed by Glenn Davis, Russ Rew, Ed Hartnett, John Caron, Steve Emmerson, and Harvey Davies at the Unidata Program Center in Boulder, Colorado, with contributions from many other netCDF users.

%package devel
Group: Development/Libraries	
Summary: Fortran development libraries for netCDF.
Requires: zlib-devel, hdf5-devel, openssl-devel
Requires: netcdf-fortran = %{version}
Requires: netcdf-devel = %{netcdf_version}
%description devel
This package contains the libraries needed to build other code requiring netCDF.
For further information see the description for the netcdf (non-devel) package.

%prep				
%setup

%build				
export FC=gfortran
export F77=gfortran
%configure --with-pic
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
%defattr(0755,root,root)
%{_bindir}/nf-config
%defattr(0644,root,root)			
%{_libdir}/pkgconfig/netcdf-fortran.pc
%{_libdir}/libnetcdff.so.5.3.1
%{_libdir}/libnetcdff.so.5
%{_libdir}/libnetcdff.so
%doc %{_infodir}/netcdf-f90.info.gz
%doc %{_infodir}/netcdf-f77.info.gz
%doc %{_infodir}/netcdf-f77.info-1.gz
%doc %{_infodir}/netcdf-f77.info-2.gz
%exclude %{_infodir}/dir
%doc %{_mandir}/man3/netcdf_f77.3.gz
%doc %{_mandir}/man3/netcdf_f90.3.gz

%files devel
%defattr(0644,root,root)			
%{_libdir}/libnetcdff.la
%{_libdir}/libnetcdff.a
%{_includedir}/netcdf.inc
%{_includedir}/typesizes.mod
%{_includedir}/netcdf.mod

%changelog
* Thu Jan 23 2014  <builderdev@builder.jc.rl.ac.uk> - 4.2-1.ceda
- update netcdf_version to 4.3.1
* Fri Dec 14 2012 Alan Iwi
alan.iwi@stfc.ac.uk 4.2
- Created initial RPM for netCDF-fortran 4.2
