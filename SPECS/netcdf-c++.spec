%global netcdf_version 4.4.1

Name: netcdf-c++
# patch0 is for issue fixed in 4.3 - remove patch when upgrading
Version: 4.2
Release: 6pre1.ceda%{?dist}
License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
Group: Scientific support	
Source: netcdf-cxx4-%{version}.tar.gz	
Patch0: netcdf-cxx4-libpath.patch
URL: http://www.unidata.ucar.edu/software/netcdf/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, hdf5-devel, zlib-devel, openssl-devel, netcdf, gcc-c++, libstdc++-devel
BuildRequires: netcdf-devel = %{netcdf_version}

Requires: hdf5, zlib, openssl, libstdc++ 
Requires: netcdf = %{netcdf_version}, netcdf-devel = %{netcdf_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  C++ bindings for netCDF

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
Summary: C++ development libraries for netCDF.
Requires: zlib-devel, hdf5-devel, openssl-devel
Requires: netcdf-c++ = %{version}
Requires: netcdf-devel = %{netcdf_version}
%description devel
This package contains the libraries needed to build other code requiring netCDF.
For further information see the description for the netcdf (non-devel) package.



%prep				
%setup -n netcdf-cxx4-%{version}
%patch0 -p1

%build				
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
%{_bindir}/ncxx4-config
%defattr(0644,root,root)			
%{_libdir}/libnetcdf_c++4.so
%{_libdir}/libnetcdf_c++4.so.1
%{_libdir}/libnetcdf_c++4.so.1.0.2
%{_libdir}/pkgconfig/netcdf-cxx4.pc

%files devel
%defattr(0644,root,root)			
%{_libdir}/libnetcdf_c++4.a
%{_libdir}/libnetcdf_c++4.la
%{_includedir}/*


%changelog
* Sun Sep 17 2017  <builderdev@builder.jc.rl.ac.uk> - 4.2-6pre1.ceda
- update netcdf version to 4.4.1

* Thu Jul  6 2017  <builderdev@builder.jc.rl.ac.uk> - 4.2-5.ceda
- patching to fix libdir reported by ncxx-config

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 4.2-4.ceda
- update netcdf version to 4.4.0
* Thu Jan 23 2014  <builderdev@builder.jc.rl.ac.uk> - 4.2-2.ceda
- update netcdf_version to 4.3.1
* Fri Jun 21 2013 Alan Iwi
alan.iwi@stfc.ac.uk 4.2
- Created initial RPM for netCDF-c++ 4.2 modelled on netcdf-fortran RPM
