# The name of the package.
Name: hdf5
Version: 1.10.1
Release: 1pre1.ceda%{?dist}
License: BSD-style		
Group: Development/Libraries	
Source: hdf5-%{version}.tar.bz2	
URL: http://www.hdfgroup.org/HDF5		
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc-c++, gcc-gfortran, zlib-devel zlib-static

Requires: zlib
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections.

Prefix: /usr

%description					

The HDF5 technology suite includes:

    * A versatile data model that can represent very complex data objects and a wide variety of metadata.

    * A completely portable file format with no limit on the number or size of data objects in the collection.

    * A software library that runs on a range of computational platforms, from laptops to massively parallel systems, and implements a high-level API with C, C++, Fortran 90, and Java interfaces.

    * A rich set of integrated performance features that allow for access time and storage space optimizations.

    * Tools and applications for managing, manipulating, viewing, and analyzing the data in the collection.

The HDF5 data model, file format, API, library, and tools are open and distributed without charge.


%package devel
Group: Development/Libraries	
Summary: Development libraries for HDF5.
Requires: hdf5 = %{version}, zlib-devel
%description devel
This package contains the libraries needed to build other code requiring HDF5.
For further information see the description for the hdf5 (non-devel) package.


%prep				
%setup -n hdf5-%{version}

%build				
%configure --enable-fortran --enable-cxx --enable-static-exec --with-zlib=/usr
make				

%install			
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT	

#
#  Post-install-Script
#
%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi
#%if $RPM_INSTALL_PREFIX != "/usr"
(cd $RPM_INSTALL_PREFIX/bin
  ./h5redeploy -force)
#%endif


%clean				
rm -rf $RPM_BUILD_ROOT		

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%files				
%defattr(0755,root,root)			
%{_bindir}/gif2h5
%{_bindir}/h5*
%{_datadir}/hdf5_examples/*.sh
%{_datadir}/hdf5_examples/*/*.sh
%{_datadir}/hdf5_examples/*/*/*.sh
%{_libdir}/lib*.so*
%defattr(0644,root,root,0755)			
%doc ./COPYING
%doc ./release_docs/RELEASE.txt
%dir %{_datadir}/hdf5_examples
%{_datadir}/hdf5_examples/README
%{_datadir}/hdf5_examples/*/*.c
%{_datadir}/hdf5_examples/*/*.f90
%{_datadir}/hdf5_examples/*/*.cpp
%{_datadir}/hdf5_examples/*/*/*.c
%{_datadir}/hdf5_examples/*/*/*.h
%{_datadir}/hdf5_examples/*/*/*.txt
%{_datadir}/hdf5_examples/*/*/*.f90
%{_datadir}/hdf5_examples/*/*/*.cpp

%files devel
%defattr(0644,root,root)			
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/libhdf5.settings
%{_includedir}/*.h
%{_includedir}/*.mod


#list of changes to this spec file since last version.
%changelog
* Sun Sep 17 2017  <builderdev@builder.jc.rl.ac.uk> - 1.10.1-1.ceda
- bump to 1.10.1
- use more wildcards in file lists above, rather than explicit lists of files

* Mon Dec  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.8.12-2.ceda
- make devel package depend on exact version of base package

* Sat Nov  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.8.12-1.ceda
- update to 1.8.12.  BuildRequires zlib-static
			
* Sat May 12 2012 Larry Knox
lrknox@hdfgroup.org 1.8.9-1
- Created initial RPM for HDF5 1.8.9 release.
