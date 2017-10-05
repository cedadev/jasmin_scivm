%define python_version 2.7
%define python_package python27
%define libs_name cmor-libs

%define python_command python%{python_version}

Name: %{python_package}-cmor
Version: 3.2.7
Release: 1.ceda%{?dist}
License: unknown
Group: Scientific support	
Source: cmor-%{version}.tar.gz	
Patch1: cmor-uuid-327.patch
Patch2: cmor-makefile-destdir-327.patch
URL: http://cmor.llnl.gov/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: autoconf, gcc, hdf5, netcdf, uuid-devel, zlib-devel, udunits
Requires: %{python_package}
BuildRequires: %{python_package}
Requires: hdf5, netcdf, uuid
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Summary:  a library to produce CMOR-compliant netCDF files (for Python %{python_version})
Prefix: /usr

%description					
The "Climate Model Output Rewriter" (CMOR, pronounced "Seymour") comprises a set of C-based functions, with bindings to both Python and FORTRAN 90, that can be used to produce CF-compliant netCDF files that fulfill the requirements of many of the climate community's standard model experiments. These experiments are collectively referred to as MIP's and include, for example, AMIP, CMIP, CFMIP, PMIP, APE, and IPCC scenario runs. The output resulting from CMOR is "self-describing" and facilitates analysis of results across models.

Much of the metadata written to the output files is defined in MIP-specific tables, typically made available from each MIP's web site. CMOR relies on these tables to provide much of the metadata that is needed in the MIP context, thereby reducing the programming effort required of the individual MIP contributors.

%package -n %{libs_name}
Group: Development/Libraries
Summary: Development libraries for CMOR
Obsoletes: cmor-devel
%description -n %{libs_name}
This package contains the static libraries and headers needed to build 
code requiring CMOR.
For further information see the description for the %{name} package.

%prep				
%setup -n cmor-cmor-%{version}
#%setup -n cmor
%patch1 -p1
%patch2 -p1

%build				
autoconf
%configure

make				
env CFLAGS="$RPM_OPT_FLAGS" %{python_command} setup.py build

%install			
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT

%{python_command} setup.py install -O1 --root=$RPM_BUILD_ROOT --record=PYTHON_INSTALLED_FILES1
%define cmor_lib /usr/lib/libcmor.a

egrep -v '^(%{_includedir}|%{cmor_lib})' PYTHON_INSTALLED_FILES1 > PYTHON_INSTALLED_FILES


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

%files -f PYTHON_INSTALLED_FILES

%files -n %{libs_name}

%{cmor_lib}
%{_includedir}/cdTime/cdunifpp/*.h
%{_includedir}/cdTime/*.h
%{_includedir}/cmor*.h
%{_includedir}/cmor*.mod
%{_includedir}/json-c/*.h

%changelog
* Thu Sep 28 2017  <builderdev@builder.jc.rl.ac.uk> - 3.2.7-1.ceda
- bump version and update patches and URL

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 2.9.2-3.ceda
- rename -devel to -libs (because -devel with no base package is confusing)

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 2.9.2-1.ceda
- rebuild against netcdf 4.4.0

* Fri Dec  4 2015  <builderdev@builder.jc.rl.ac.uk> - 2.9.2-1.ceda
- bump version; update cmor-makefile-destdir.patch (needed to apply cleanly
against later version, although new lines introduced by patch are unchanged)

* Thu Jan 24 2013  <builderdev@builder.jc.rl.ac.uk> - 2.8.2-2.ceda
- separate devel into another package (NB this is not python-version dependent)
			
* Tue Oct 16 2012 Alan Iwi alan.iwi@stfc.ac.uk 2.7.1
- Created initial RPM for CMOR 2.7.1 (modelled on RPM for HDF5 1.8.9)
