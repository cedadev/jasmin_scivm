Name: umutil
Version: 20130102
Release: 2.ceda%{?dist}
License: NCAS
Group: Scientific support	
Source0: umutil-20130102-pruned.tar.gz
Source1: umutil-Makefile_Linux_x86_64
Patch1: umutil-pp2drs-col72.patch
Patch2: umutil-check-types.patch
Patch3: umutil-lsm-icopy.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
			#used with non-root builds of RPM files
BuildRequires: gcc, gcc-gfortran,zlib-devel,netcdf-fortran-devel,hdf5-devel,emos,libdrs,libcrayutil
Requires: emos, libgfortran, netcdf-fortran


Summary: Various utilities related to the Unified Model
Prefix: /usr

%description					
Various utilities related to the Unified Model

This package is compiled from a snapshot of the source code taken from
Jeff Cole's directory (~jeff/um/umutil) on the Reading Meteorology 
systems.

%package lib
Group: Development/Libraries
Summary: Development libraries for compiling UM utilities
Requires: libcrayutil
%description lib
This package contains the libraries needed to build UM utilities such as xconv.

%define mymakefile Makefile_Linux_x86_64_new

%prep

%setup0 -n %{name}-%{version}
cp %{SOURCE1} %{mymakefile}
%patch1 -p1
%patch2 -p1
%patch3 -p1
perl -p -i -e 's/#include "util.h"/#include "crayutil.h"/' *.c
mv umtrunc.f umtrunc.F

%build

make -f Makefile_lib_linux_x86_64 UMUTILLIB=libumutil.a
make -f %{mymakefile}
make -f %{mymakefile} test

%install			

rm -rf $RPM_BUILD_ROOT		

dir=$RPM_BUILD_ROOT/%{_libdir}
mkdir -p $dir
install -m 644 libumutil.a $dir

make -f %{mymakefile} install INSTALLDIR=$RPM_BUILD_ROOT/%{_bindir}

%clean				
rm -rf $RPM_BUILD_ROOT

%files				
%{_bindir}/*

%defattr(-,root,root)

%files lib
%{_libdir}/libumutil.a

%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 20130102-1.ceda
- rebuild against later netcdf

* Tue Jan 13 2013 Alan Iwi
alan.iwi@stfc.ac.uk 20130102
- Created initial RPM
