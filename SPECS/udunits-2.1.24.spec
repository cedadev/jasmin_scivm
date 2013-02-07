# The name of the package.
Name: udunits


Version: 2.1.24
			# Version of the package contained in the RPM.


Release: 2.ceda%{?dist}
			# Version of the RPM.


License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
			# Licensing Terms


Group: Scientific support	
			# Group, identifies types of software. Used by users to manage multiple RPMs.


Source: udunits-2.1.24.tar.gz	


			#Source tar ball name
URL: http://www.unidata.ucar.edu/software/udunits/


			# URL to find package
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	


			#used with non-root builds of RPM files
BuildRequires: gcc, expat, expat-devel

#Requires: hdf5
Requires: expat
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  UDUNITS provides support for units of physical quantities. 
			# One line summary of package

Prefix: /usr

%description					

			# Full description. Can be multiple lines.
UDUNITS supports conversion of unit specifications between formatted and binary forms, arithmetic manipulation of units, and conversion of values between compatible scales of measurement.

%package devel
Group: Development/Libraries	
Summary: Development libraries for udunits
Requires: udunits, expat-devel
%description devel
This package contains the libraries needed to build other code requiring udunits.
For further information see the description for the udunits (non-devel) package.


%prep				
			#prep: list steps after this to unpack the package.			
%setup -n udunits-2.1.24
			# setup is a macro used to unpack the package with default settings (i.e., gunzip, untar)

%build				
			#build: steps after this should compile the package
			#macro used to configure the package with standard ./configure command
%configure

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
%{_bindir}/udunits2
%defattr(0644,root,root)			
# %{_libdir}/libexpat.so
# %{_libdir}/libexpat.so.0
# %{_libdir}/libexpat.so.0.0.0
%{_libdir}/libudunits2.so
%{_libdir}/libudunits2.so.0
%{_libdir}/libudunits2.so.0.1.0
%doc %{_datadir}/doc/udunits/udunits2-accepted.xml
%doc %{_datadir}/doc/udunits/udunits2-base.xml
%doc %{_datadir}/doc/udunits/udunits2-common.xml
%doc %{_datadir}/doc/udunits/udunits2-derived.xml
%doc %{_datadir}/doc/udunits/udunits2-prefixes.xml
%doc %{_datadir}/doc/udunits/udunits2.xml
%exclude %{_datadir}/info/dir
%doc %{_datadir}/info/udunits2.info.gz
%doc %{_datadir}/info/udunits2lib.info.gz
%doc %{_datadir}/info/udunits2prog.info.gz
%{_datadir}/udunits/udunits2-accepted.xml
%{_datadir}/udunits/udunits2-base.xml
%{_datadir}/udunits/udunits2-common.xml
%{_datadir}/udunits/udunits2-derived.xml
%{_datadir}/udunits/udunits2-prefixes.xml
%{_datadir}/udunits/udunits2.xml

%files devel
%defattr(0644,root,root)			
%{_includedir}/converter.h
%{_includedir}/udunits2.h
%{_includedir}/udunits.h
# %{_libdir}/libexpat.a
# %{_libdir}/libexpat.la
%{_libdir}/libudunits2.a
%{_libdir}/libudunits2.la


#list of changes to this spec file since last version.
%changelog			
* Mon Aug 13 2012 Alan Iwi
alan.iwi@stfc.ac.uk 2.1.24
- Created initial RPM for udunits 2.1.24 (modelled on RPM for HDF5 1.8.9)
