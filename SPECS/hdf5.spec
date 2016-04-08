# The name of the package.
Name: hdf5
Version: 1.8.12
Release: 2.ceda%{?dist}
License: BSD-style		
Group: Development/Libraries	
Source: hdf5-%{version}.tar.gz	
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
%{_bindir}/h52gif
%{_bindir}/h5cc
%{_bindir}/h5c++
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5dump
%{_bindir}/h5fc
%{_bindir}/h5import
%{_bindir}/h5jam
%{_bindir}/h5ls
%{_bindir}/h5mkgrp
%{_bindir}/h5perf_serial
%{_bindir}/h5redeploy
%{_bindir}/h5repack
%{_bindir}/h5repart
%{_bindir}/h5stat
%{_bindir}/h5unjam
%{_datadir}/hdf5_examples/*.sh
%{_datadir}/hdf5_examples/*/*.sh
%{_datadir}/hdf5_examples/*/*/*.sh
%{_libdir}/libhdf5.so*
%{_libdir}/libhdf5_cpp.so*
%{_libdir}/libhdf5_fortran.so*
%{_libdir}/libhdf5_hl.so*
%{_libdir}/libhdf5_hl_cpp.so*
%{_libdir}/libhdf5hl_fortran.so*
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
%{_libdir}/libhdf5.*a
%{_libdir}/libhdf5.settings
%{_libdir}/libhdf5_cpp.*a
%{_libdir}/libhdf5_fortran.*a
%{_libdir}/libhdf5_hl.*a
%{_libdir}/libhdf5_hl_cpp.*a
%{_libdir}/libhdf5hl_fortran.*a
%{_includedir}/H5ACpublic.h
%{_includedir}/H5Apublic.h
%{_includedir}/H5Cpublic.h
%{_includedir}/H5DSpublic.h
%{_includedir}/H5Dpublic.h
%{_includedir}/H5Epubgen.h
%{_includedir}/H5Epublic.h
%{_includedir}/H5FDcore.h
%{_includedir}/H5FDdirect.h
%{_includedir}/H5FDfamily.h
%{_includedir}/H5FDlog.h
%{_includedir}/H5FDmpi.h
%{_includedir}/H5FDmpio.h
%{_includedir}/H5FDmpiposix.h
%{_includedir}/H5FDmulti.h
%{_includedir}/H5FDpublic.h
%{_includedir}/H5FDsec2.h
%{_includedir}/H5FDstdio.h
%{_includedir}/H5Fpublic.h
%{_includedir}/H5f90i.h
%{_includedir}/H5f90i_gen.h
%{_includedir}/H5Gpublic.h
%{_includedir}/H5IMpublic.h
%{_includedir}/H5Ipublic.h
%{_includedir}/H5LTpublic.h
%{_includedir}/H5Lpublic.h
%{_includedir}/H5MMpublic.h
%{_includedir}/H5Opublic.h
%{_includedir}/H5PTpublic.h
%{_includedir}/H5Ppublic.h
%{_includedir}/H5Rpublic.h
%{_includedir}/H5Spublic.h
%{_includedir}/H5TBpublic.h
%{_includedir}/H5Tpublic.h
%{_includedir}/H5Zpublic.h
%{_includedir}/H5api_adpt.h
%{_includedir}/H5overflow.h
%{_includedir}/H5pubconf.h
%{_includedir}/H5public.h
%{_includedir}/H5version.h
%{_includedir}/hdf5.h
%{_includedir}/hdf5_hl.h
%{_includedir}/H5AbstractDs.h
%{_includedir}/H5ArrayType.h
%{_includedir}/H5AtomType.h
%{_includedir}/H5Attribute.h
%{_includedir}/H5Classes.h
%{_includedir}/H5CommonFG.h
%{_includedir}/H5CompType.h
%{_includedir}/H5Cpp.h
%{_includedir}/H5CppDoc.h
%{_includedir}/H5DataSet.h
%{_includedir}/H5DataSpace.h
%{_includedir}/H5DataType.h
%{_includedir}/H5DcreatProp.h
%{_includedir}/H5DxferProp.h
%{_includedir}/H5EnumType.h
%{_includedir}/H5Exception.h
%{_includedir}/H5FaccProp.h
%{_includedir}/H5FcreatProp.h
%{_includedir}/H5File.h
%{_includedir}/H5FloatType.h
%{_includedir}/H5Group.h
%{_includedir}/H5IdComponent.h
%{_includedir}/H5Include.h
%{_includedir}/H5IntType.h
%{_includedir}/H5Library.h
%{_includedir}/H5Object.h
%{_includedir}/H5PacketTable.h
%{_includedir}/H5PredType.h
%{_includedir}/H5PropList.h
%{_includedir}/H5StrType.h
%{_includedir}/H5VarLenType.h
%{_includedir}/h5_dble_interface.mod
%{_includedir}/h5a.mod
%{_includedir}/h5a_provisional.mod
%{_includedir}/h5d.mod
%{_includedir}/h5d_provisional.mod
%{_includedir}/h5ds.mod
%{_includedir}/h5e.mod
%{_includedir}/h5e_provisional.mod
%{_includedir}/h5f.mod
%{_includedir}/h5fortran_types.mod
%{_includedir}/h5g.mod
%{_includedir}/h5global.mod
%{_includedir}/h5i.mod
%{_includedir}/h5im.mod
%{_includedir}/h5l.mod
%{_includedir}/h5l_provisional.mod
%{_includedir}/h5lib.mod
%{_includedir}/h5lib_provisional.mod
%{_includedir}/h5lt.mod
%{_includedir}/h5o.mod
%{_includedir}/h5o_provisional.mod
%{_includedir}/h5p.mod
%{_includedir}/h5p_provisional.mod
%{_includedir}/h5r.mod
%{_includedir}/h5r_provisional.mod
%{_includedir}/h5s.mod
%{_includedir}/h5t.mod
%{_includedir}/h5t_provisional.mod
%{_includedir}/h5tb.mod
%{_includedir}/h5z.mod
%{_includedir}/hdf5.mod

# files new in 1.8.12 since 1.8.9
%{_includedir}/H5DOpublic.h
%{_includedir}/H5Location.h
%{_includedir}/H5PLextern.h
%{_includedir}/h5f_provisional.mod


#list of changes to this spec file since last version.
%changelog
* Mon Dec  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.8.12-2.ceda
- make devel package depend on exact version of base package

* Sat Nov  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.8.12-1.ceda
- update to 1.8.12.  BuildRequires zlib-static
			
* Sat May 12 2012 Larry Knox
lrknox@hdfgroup.org 1.8.9-1
- Created initial RPM for HDF5 1.8.9 release.
