Name: cdo
Version: 1.6.9
Release: 1.ceda%{?dist}
License: GPL v2
Group: Scientific support	
Source: cdo-%{version}.tar.gz	
URL: https://code.zmaw.de/projects/cdo/wiki
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, gcc-c++, netcdf-devel
Requires: netcdf
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

%build				
%configure --with-netcdf=/usr
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
* Fri May 22 2015  <builderdev@builder.jc.rl.ac.uk> - 1.6.9-1.ceda
- version upgrade

* Tue Jan 22 2013  <builderdev@builder.jc.rl.ac.uk> - 1.5.6.1-3.ceda
- add --with-netcdf as not picking it up otherwise
			
* Mon Aug 24 2012 Alan Iwi
alan.iwi@stfc.ac.uk 1.5.6.1
- Created initial RPM for netCDF 4.2.1 (modelled on RPM for HDF5 1.8.9)
