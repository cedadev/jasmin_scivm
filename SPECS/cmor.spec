# The name of the package.
Name: cmor


Version: 2.8.2
			# Version of the package contained in the RPM.


Release: 1.ceda
			# Version of the RPM.


License: unknown
			# Licensing Terms


Group: Scientific support	
			# Group, identifies types of software. Used by users to manage multiple RPMs.


Source: cmor-%{version}.tar.gz	
Patch1: cmor-uuid.patch
Patch2: cmor-makefile-destdir.patch


			#Source tar ball name
URL: http://www2-pcmdi.llnl.gov/cmor/


			# URL to find package
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	


			#used with non-root builds of RPM files
BuildRequires: autoconf, gcc, hdf5, netcdf, uuid-devel, zlib-devel, udunits

Requires: hdf5, netcdf, uuid
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  a library to produce CMOR-compliant netCDF files
			# One line summary of package

Prefix: /usr

%description					

			# Full description. Can be multiple lines.
The "Climate Model Output Rewriter" (CMOR, pronounced "Seymour") comprises a set of C-based functions, with bindings to both Python and FORTRAN 90, that can be used to produce CF-compliant netCDF files that fulfill the requirements of many of the climate community's standard model experiments. These experiments are collectively referred to as MIP's and include, for example, AMIP, CMIP, CFMIP, PMIP, APE, and IPCC scenario runs. The output resulting from CMOR is "self-describing" and facilitates analysis of results across models.

Much of the metadata written to the output files is defined in MIP-specific tables, typically made available from each MIP's web site. CMOR relies on these tables to provide much of the metadata that is needed in the MIP context, thereby reducing the programming effort required of the individual MIP contributors.

%prep				
			#prep: list steps after this to unpack the package.			
#%setup -n cmor-%{version}
%setup -n cmor
%patch1 -p1
%patch2 -p1
			# setup is a macro used to unpack the package with default settings (i.e., gunzip, untar)

%build				
			#build: steps after this should compile the package
			#macro used to configure the package with standard ./configure command
autoconf
%configure

make				
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

			#this is a direct command-line option, which just runs .make.: compiles the package.

%install			
			#install: steps after this will install the package.

rm -rf $RPM_BUILD_ROOT		
			#used with non-root builds of RPM files.

make install DESTDIR=$RPM_BUILD_ROOT	
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=PYTHON_INSTALLED_FILES
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

%files -f PYTHON_INSTALLED_FILES			
%defattr(0644,root,root)			
%{_libdir}/libcmor.a
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


#list of changes to this spec file since last version.
%changelog			
* Tue Oct 16 2012 Alan Iwi
alan.iwi@stfc.ac.uk 2.7.1
- Created initial RPM for CMOR 2.7.1 (modelled on RPM for HDF5 1.8.9)
