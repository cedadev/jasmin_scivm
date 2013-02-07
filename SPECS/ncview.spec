# The name of the package.
Name: ncview


Version: 2.1.2
			# Version of the package contained in the RPM.


Release: 1.ceda%{?dist}
			# Version of the RPM.


License: http://www.gnu.org/licenses/gpl-1.0.html
			# Licensing Terms


Group: Scientific support	
			# Group, identifies types of software. Used by users to manage multiple RPMs.


Source: %{name}-%{version}.tar.gz	


			#Source tar ball name
URL: http://meteora.ucsd.edu/~pierce/ncview_home_page.html


			# URL to find package
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	


			#used with non-root builds of RPM files
BuildRequires: gcc, libXaw-devel

Summary:  a netCDF visual browser
			# One line summary of package

Prefix: /usr

%description					

			# Full description. Can be multiple lines.
Ncview is a visual browser for netCDF format files. Typically you would use ncview to get a quick and easy, push-button look at your netCDF files. You can view simple movies of the data, view along various dimensions, take a look at the actual data values, change color maps, invert the data, etc. 


%prep				
			#prep: list steps after this to unpack the package.			
%setup
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

%clean				
			#performs a make clean after the install
rm -rf $RPM_BUILD_ROOT		

			#used with non-root builds of RPM files.

%files				
			#files should be followed by a list of all files that get installed.
%defattr(0755,root,root)
%{_bindir}/ncview

#list of changes to this spec file since last version.

%changelog
* Mon Dec 17 2012  <alan.iwi@stfc.ac.uk> - 2.1.2-1.ceda
- initial version

