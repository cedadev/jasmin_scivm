Name: cdo
Version: 1.9.5
Release: 2.ceda%{?dist}
License: GPL v2
Group: Scientific support	
Source: cdo-%{version}.tar.gz	
#Patch0: cdo-utread.patch
URL: https://code.zmaw.de/projects/cdo/wiki
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, gcc-c++, netcdf-devel, eccodes-devel, fftw-devel, proj-devel, libcurl-devel, udunits-devel, hdf5-devel, uuid-devel, cmor-libs, devtoolset-6-gcc-c++
Requires: netcdf, eccodes, fftw, proj, libcurl, udunits, hdf5, uuid
Summary:  Climate Data Operators is a set of operators for working on climate and NWP model data. 
Prefix: /usr

%description					

CDO is a large tool set for working on climate and NWP model
data. NetCDF 3/4, GRIB 1/2 including SZIP and JPEG compression, EXTRA,
SERVICE and IEG are supported as IO-formats. Apart from that CDO can
be used to analyse any kind gridded data not related to climate
science.  CDO has very small memory requirements and can process files
larger than the physical memory.

CDO is open source and released under the terms of the GNU General
Public License v2 (GPL).

%prep				

%setup
#%patch0 -p1

%build				
export LIBS="-ludunits2 -lnetcdf -lossp-uuid"
. /opt/rh/devtoolset-6/enable
export CFLAGS="-I/usr/include/json-c -I/usr/include/cdTime"
export CXXFLAGS="-std=c++0x -fpermissive $CFLAGS"
%configure --with-netcdf=/usr --with-cmor=/usr --with-eccodes=/usr --with-fftw3 --with-proj=/usr --with-curl=/usr --with-udunits2=/usr
make				

%install			
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT	
docdir=$RPM_BUILD_ROOT/%{_datadir}/%{name}
[ -d $docdir ] || mkdir -p $docdir
cp doc/cdo.pdf $docdir
cp doc/cdo_refcard.pdf $docdir


%clean				
rm -rf $RPM_BUILD_ROOT		

%files				
%defattr(0755,root,root)
%{_bindir}/cdo
%defattr(0644,root,root)			
%doc %{_datadir}/cdo/cdo.pdf
%doc %{_datadir}/cdo/cdo_refcard.pdf


#list of changes to this spec file since last version.
%changelog
* Thu Aug 23 2018  <builderdev@builder.jc.rl.ac.uk> - 1.9.5-2.ceda
- change to using eccodes

* Thu Aug 16 2018  <builderdev@builder.jc.rl.ac.uk> - 1.9.5-1.ceda
- bump version

* Thu Jul 19 2018  <builderdev@builder.jc.rl.ac.uk> - 1.9.4-1.ceda
- bump version

* Sat Mar 31 2018  <builderdev@builder.jc.rl.ac.uk> - 1.9.3-1.ceda
- bump version

* Tue Sep 26 2017  <builderdev@builder.jc.rl.ac.uk> - 1.9.0-1.ceda
- bump version and compile against later hdf5/netcdf

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 1.7.2-1.ceda
- bump version, also rebuilding against grib_api 1.17.0
- "utread" patch no longer needed

* Tue May  3 2016  <builderdev@builder.jc.rl.ac.uk> - 1.7.1-2.ceda
- rebuild against new grib_api

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.7.1-1.ceda
- update to 1.7.1, recompile against netCDF 4.4.0
- patch to fix ut_read issue

* Sun Dec  6 2015  <builderdev@builder.jc.rl.ac.uk> - 1.7.0-2.ceda
- recompile against hdf5-1.8.12

* Fri Dec  4 2015  <builderdev@builder.jc.rl.ac.uk> - 1.7.0-1.ceda
- bump version and add support for grib, cmor, fftw, proj, curl, udunits2

* Fri May 22 2015  <builderdev@builder.jc.rl.ac.uk> - 1.6.9-1.ceda
- version upgrade

* Tue Jan 22 2013  <builderdev@builder.jc.rl.ac.uk> - 1.5.6.1-3.ceda
- add --with-netcdf as not picking it up otherwise
			
* Mon Aug 24 2012 Alan Iwi
alan.iwi@stfc.ac.uk 1.5.6.1
- Created initial RPM for netCDF 4.2.1 (modelled on RPM for HDF5 1.8.9)
