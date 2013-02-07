# The name of the package.
Name: cdo


Version: 1.5.6.1
			# Version of the package contained in the RPM.


Release: 3.ceda%{?dist}
			# Version of the RPM.


License: GPL v2
			# Licensing Terms


Group: Scientific support	
			# Group, identifies types of software. Used by users to manage multiple RPMs.


Source: cdo-1.5.6.1.tar.gz	


			#Source tar ball name
URL: https://code.zmaw.de/projects/cdo/wiki


			# URL to find package
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	


			#used with non-root builds of RPM files
BuildRequires: gcc, gcc-c++, netcdf-devel

Requires: netcdf

Summary:  Climate Data Operators is a set of operators for working on climate and NWP model data. 
			# One line summary of package

Prefix: /usr

%description					

			# Full description. Can be multiple lines.
CDO is a large tool set for working on climate and NWP model
data. NetCDF 3/4, GRIB 1/2 including SZIP and JPEG compression, EXTRA,
SERVICE and IEG are supported as IO-formats. Apart from that CDO can
be used to analyse any kind gridded data not related to climate
science.  CDO has very small memory requirements and can process files
larger than the physical memory.

CDO is open source and released under the terms of the GNU General
Public License v2 (GPL).

%prep				
			#prep: list steps after this to unpack the package.			
%setup -n cdo-1.5.6.1
			# setup is a macro used to unpack the package with default settings (i.e., gunzip, untar)

%build				
			#build: steps after this should compile the package
			#macro used to configure the package with standard ./configure command
%configure --with-netcdf=/usr

make				
			#this is a direct command-line option, which just runs .make.: compiles the package.

%install			
			#install: steps after this will install the package.

rm -rf $RPM_BUILD_ROOT		
			#used with non-root builds of RPM files.

make install DESTDIR=$RPM_BUILD_ROOT	
			#performs a make install
docdir=$RPM_BUILD_ROOT/%{_datadir}/%{name}
[ -d $docdir ] || mkdir -p $docdir
cp doc/cdo.pdf $docdir
cp doc/cdo_refcard.pdf $docdir


%clean				
			#performs a make clean after the install
rm -rf $RPM_BUILD_ROOT		
			#used with non-root builds of RPM files.

%files				
			#files should be followed by a list of all files that get installed.
%defattr(0755,root,root)
%{_bindir}/cdo
%defattr(0644,root,root)			
%doc %{_datadir}/cdo/cdo.pdf
%doc %{_datadir}/cdo/cdo_refcard.pdf


#list of changes to this spec file since last version.
%changelog
* Tue Jan 22 2013  <builderdev@builder.jc.rl.ac.uk> - 1.5.6.1-3.ceda
- add --with-netcdf as not picking it up otherwise
			
* Mon Aug 24 2012 Alan Iwi
alan.iwi@stfc.ac.uk 1.5.6.1
- Created initial RPM for netCDF 4.2.1 (modelled on RPM for HDF5 1.8.9)
