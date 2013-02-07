%global netcdf_version 4.2.1

# The name of the package.
Name: netcdf-fortran


Version: 4.2
			# Version of the package contained in the RPM.


Release: 1.ceda%{?dist}
			# Version of the RPM.


License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
			# Licensing Terms


Group: Scientific support	
			# Group, identifies types of software. Used by users to manage multiple RPMs.


Source: netcdf-fortran-%{version}.tar.gz	


			#Source tar ball name
URL: http://www.unidata.ucar.edu/software/netcdf/


			# URL to find package
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	


			#used with non-root builds of RPM files
BuildRequires: gcc, hdf5-devel, zlib-devel, openssl-devel, netcdf, gcc-gfortran, libgfortran
BuildRequires: netcdf-devel = %{netcdf_version}

Requires: hdf5, zlib, openssl, libgfortran
Requires: netcdf = %{netcdf_version}, netcdf-devel = %{netcdf_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  Fortran bindings for netCDF
			# One line summary of package

Prefix: /usr

%description					

			# Full description. Can be multiple lines.
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
			#prep: list steps after this to unpack the package.			
%setup
			# setup is a macro used to unpack the package with default settings (i.e., gunzip, untar)

%build				
			#build: steps after this should compile the package
			#macro used to configure the package with standard ./configure command

export FC=gfortran
export F77=gfortran
%configure --with-pic

make				
			#this is a direct command-line option, which just runs .make.: compiles the package.

%install			
			#install: steps after this will install the package.

rm -rf $RPM_BUILD_ROOT		
			#used with non-root builds of RPM files.

make install DESTDIR=$RPM_BUILD_ROOT	
			#performs a make install

#
#  Post-install-Script
#
%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi


%clean				
			#performs a make clean after the install
rm -rf $RPM_BUILD_ROOT		

			#used with non-root builds of RPM files.

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%files				
			#files should be followed by a list of all files that get installed.

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


#list of changes to this spec file since last version.

%changelog
* Fri Dec 14 2012 Alan Iwi
alan.iwi@stfc.ac.uk 4.2
- Created initial RPM for netCDF-fortran 4.2
