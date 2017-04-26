Name: ncview
Version: 2.1.7
Release: 1.ceda%{?dist}
License: http://www.gnu.org/licenses/gpl-1.0.html
Group: Scientific support	
Source: %{name}-%{version}.tar.gz	
URL: http://meteora.ucsd.edu/~pierce/ncview_home_page.html
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, libXaw-devel
Summary:  a netCDF visual browser
Prefix: /usr

%description					
Ncview is a visual browser for netCDF format files. Typically you would use ncview to get a quick and easy, push-button look at your netCDF files. You can view simple movies of the data, view along various dimensions, take a look at the actual data values, change color maps, invert the data, etc. 

%prep				
%setup
%build				
%configure
make				

%install			
rm -rf $RPM_BUILD_ROOT		
make install DESTDIR=$RPM_BUILD_ROOT	

%clean				
rm -rf $RPM_BUILD_ROOT		

%files				
%defattr(0755,root,root)
%{_bindir}/ncview

%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 2.1.7-1.ceda
- update to 2.1.7

* Mon Dec 17 2012  <alan.iwi@stfc.ac.uk> - 2.1.2-1.ceda
- initial version

