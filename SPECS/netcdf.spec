Name: netcdf
Version: 4.3.2
Release: 2.ceda%{?dist}
License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
Group: Scientific support	
Source: netcdf-%{version}.tar.gz	
URL: http://www.unidata.ucar.edu/software/netcdf/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, hdf5-devel, zlib-devel, openssl-devel

Requires: hdf5, zlib, openssl
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  NetCDF is a set of libraries and related data formats for array-oriented scientific data.

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
Summary: Development libraries for netCDF.
Requires: zlib-devel, hdf5-devel, openssl-devel
Requires: netcdf = %{version}
%description devel
This package contains the libraries needed to build other code requiring netCDF.
For further information see the description for the netcdf (non-devel) package.

%prep				
%setup -n netcdf-%{version}

%build				
%configure --enable-netcdf-4 --with-pic --enable-pnetcdf
make				

%install			
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT	

# fix nc-config to report lib64 path
if echo %{_libdir} | grep -q lib64
then
  perl -p -i -e 's,^(libdir=.*)/lib$,$1/lib64,' $RPM_BUILD_ROOT%{_bindir}/nc-config
fi

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
%{_bindir}/nc-config
%{_bindir}/nccopy
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_bindir}/ncgen3
%defattr(0644,root,root)			
%{_libdir}/libnetcdf.so.7.2.0
%{_libdir}/pkgconfig/netcdf.pc
%{_libdir}/libnetcdf.so
%{_libdir}/libnetcdf.so.7
%doc %{_mandir}/man1/nccopy.1.gz
%doc %{_mandir}/man1/ncdump.1.gz
%doc %{_mandir}/man1/ncgen.1.gz
%doc %{_mandir}/man1/ncgen3.1.gz
%doc %{_mandir}/man3/netcdf.3.gz

%files devel
%defattr(0644,root,root)			
%{_libdir}/libnetcdf.a
%{_libdir}/libnetcdf.la
%{_includedir}/netcdf.h

%changelog
* Tue Sep 30 2014  <builderdev@builder.jc.rl.ac.uk> - 4.3.2-1.ceda
- --enable-pnetcdf
* Thu Sep 11 2014 Alan Iwi - 4.3.1-2.ceda
- update to 4.3.2
* Thu Jan 23 2014 Alan Iwi - 4.3.1-1.ceda
- update to 4.3.1
* Fri Dec 14 2012 Alan Iwi
alan.iwi@stfc.ac.uk 3.ceda
- devel package depends on main package
* Mon Aug 13 2012 Alan Iwi
alan.iwi@stfc.ac.uk 4.2.1
- Created initial RPM for netCDF 4.2.1 (modelled on RPM for HDF5 1.8.9)
