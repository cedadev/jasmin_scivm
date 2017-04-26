%define python_version 2.7
%define python_package python27
%define libs_name cmor-libs

%define python_command python%{python_version}

Name: %{python_package}-cmor
Version: 2.9.2
Release: 3.ceda%{?dist}
License: unknown
Group: Scientific support	
Source: cmor-%{version}.tar.gz	
Patch1: cmor-uuid.patch
Patch2: cmor-makefile-destdir-292.patch
URL: http://www2-pcmdi.llnl.gov/cmor/
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
%setup -n cmor-%{version}
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
%defattr(0644,root,root)

%files -n %{libs_name}

%defattr(-,root,root)
%{cmor_lib}
%{_includedir}/cdTime/cdunifpp/cdunifpp_frename.h
%{_includedir}/cdTime/cdunifpp/cdunifpp.h
%{_includedir}/cdTime/cdunifpp/crayio.h
%{_includedir}/cdTime/cdunifpp/util.h
%{_includedir}/cdTime/cdunifpp/vardef.h
%{_includedir}/cdTime/cddrs.h
%{_includedir}/cdTime/cddrsint.h
%{_includedir}/cdTime/cdms.h
%{_includedir}/cdTime/cdmsint.h
%{_includedir}/cdTime/cdmsint_new.h
%{_includedir}/cdTime/cdrra.h
%{_includedir}/cdTime/cdunif.h
%{_includedir}/cdTime/cdunifint.h
%{_includedir}/cdTime/cfortran.h
%{_includedir}/cdTime/drscdf.h
%{_includedir}/cdTime/drsdef.h
%{_includedir}/cdTime/fcddrs.h
%{_includedir}/cdTime/gaussLats.h
%{_includedir}/cdTime/grads.h
%{_includedir}/cdTime/gx.h
%{_includedir}/cdTime/isdb.h
%{_includedir}/cmor_func_def.h
%{_includedir}/cmor.h
%{_includedir}/cmor_locale.h
%{_includedir}/cmor_md5.h
%{_includedir}/cmor_users_functions.mod

%changelog
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
