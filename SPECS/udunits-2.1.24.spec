Name: udunits
Version: 2.1.24
Release: 3.ceda%{?dist}
License: http://www.unidata.ucar.edu/software/netcdf/copyright.html
Group: Scientific support	
Source: udunits-2.1.24.tar.gz	
URL: http://www.unidata.ucar.edu/software/udunits/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, expat, expat-devel

#Requires: hdf5
Requires: expat
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  UDUNITS provides support for units of physical quantities. 

Prefix: /usr

%description					
UDUNITS supports conversion of unit specifications between formatted and binary forms, arithmetic manipulation of units, and conversion of values between compatible scales of measurement.

%package devel
Group: Development/Libraries	
Summary: Development libraries for udunits
Requires: udunits = %{version}, expat-devel
%description devel
This package contains the libraries needed to build other code requiring udunits.
For further information see the description for the udunits (non-devel) package.


%prep				
%setup -n udunits-2.1.24

%build				
%configure

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
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 2.1.24-3.ceda
- make -devel depend on exact base version
			
* Mon Aug 13 2012 Alan Iwi
alan.iwi@stfc.ac.uk 2.1.24
- Created initial RPM for udunits 2.1.24 (modelled on RPM for HDF5 1.8.9)
