Name: nco
Version: 4.3.4
Release: 2.ceda%{?dist}
License: GPL v3
Group: Scientific support	
Source: nco-%{version}.tar.gz	
URL: http://nco.sourceforge.net/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
BuildRequires: gcc, gcc-c++, netcdf-devel, udunits-devel, antlr, libcurl-devel, bison, byacc, flex, gsl-devel

Requires: netcdf, udunits
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Summary:  The netCDF Operators (NCO) perform a range of operations using netCDF files as input

Prefix: /usr

%description					

The netCDF Operators (NCO) comprise a dozen standalone, command-line programs that take netCDF files as input, then operate (e.g., derive new data, average, print, hyperslab, manipulate metadata) and output the results to screen or files in text, binary, or netCDF formats. NCO aids manipulation and analysis of gridded scientific data. The shell-command style of NCO allows users to manipulate and analyze files interactively, or with simple scripts that avoid some overhead (and power) of higher level programming environments. See the NCO User's Guide (http://nco.sourceforge.net/nco.html) for examples of their use with climate data analysis:

    * ncap2 netCDF Arithmetic Processor
    * ncatted netCDF ATTribute EDitor
    * ncbo netCDF Binary Operator (includes ncadd, ncsubtract, ncmultiply, ncdivide)
    * ncea netCDF Ensemble Averager
    * ncecat netCDF Ensemble conCATenator
    * ncflint netCDF FiLe INTerpolator
    * ncks netCDF Kitchen Sink
    * ncpdq netCDF Permute Dimensions Quickly, Pack Data Quietly
    * ncra netCDF Record Averager
    * ncrcat netCDF Record conCATenator
    * ncrename netCDF RENAMEer
    * ncwa netCDF Weighted Averager

Note that the ~averagers~ (ncea and ncra) are misnamed because they perform many non-linear operations as well, e.g., total, minimum, maximum, RMS. Moreover, ncap2 implements a powerful domain language which handles arbitrarily complex operations. The operators are as general as netCDF itself: there are no restrictions on the contents of the netCDF file(s) used as input. NCO's internal routines are completely dynamic and impose no limit on the number or sizes of dimensions, variables, and files. NCO is designed to be used both interactively and with large batch jobs. The default operator behavior is often sufficient for everyday needs, and there are numerous command line (i.e., run-time) options, for special cases. NCO works well and is used on most modern operating systems. 

%package devel
Group: Development/Libraries	
Summary: Development libraries for NCO
Requires: nco = %{version}, udunits, netcdf
%description devel
This package contains the libraries needed to build other code requiring 
the library that comes with the netCDF operators (NCO).
For further information see the description for the nco (non-devel) package.



%prep				
%setup -n nco-%{version}

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
%{_bindir}/ncap
%{_bindir}/ncap2
%{_bindir}/ncatted
%{_bindir}/ncbo
%{_bindir}/ncdiff
%{_bindir}/ncea
%{_bindir}/ncecat
%{_bindir}/ncflint
%{_bindir}/ncks
%{_bindir}/ncpdq
%{_bindir}/ncra
%{_bindir}/ncrcat
%{_bindir}/ncrename
%{_bindir}/ncwa
%defattr(0644,root,root)			
%{_libdir}/libnco-%{version}.so
%{_libdir}/libnco_c++-%{version}.so
%{_libdir}/libnco_c++.so
%{_libdir}/libnco.so
%doc %{_datadir}/info/nco.info.gz
%exclude %{_datadir}/info/dir
%doc %{_mandir}/man1/ncap.1.gz
%doc %{_mandir}/man1/ncap2.1.gz
%doc %{_mandir}/man1/ncatted.1.gz
%doc %{_mandir}/man1/ncbo.1.gz
%doc %{_mandir}/man1/ncdiff.1.gz
%doc %{_mandir}/man1/ncea.1.gz
%doc %{_mandir}/man1/ncecat.1.gz
%doc %{_mandir}/man1/ncflint.1.gz
%doc %{_mandir}/man1/ncks.1.gz
%doc %{_mandir}/man1/nco.1.gz
%doc %{_mandir}/man1/ncpdq.1.gz
%doc %{_mandir}/man1/ncra.1.gz
%doc %{_mandir}/man1/ncrcat.1.gz
%doc %{_mandir}/man1/ncrename.1.gz
%doc %{_mandir}/man1/ncwa.1.gz

%files devel
%defattr(0644,root,root)			
%{_includedir}/libnco_c++.hh
%{_includedir}/nco_att.hh
%{_includedir}/nco_dmn.hh
%{_includedir}/nco_fl.hh
%{_includedir}/nco_hgh.hh
%{_includedir}/nco_utl.hh
%{_includedir}/nco_var.hh
%{_libdir}/libnco.a
%{_libdir}/libnco_c++.a
%{_libdir}/libnco_c++.la
%{_libdir}/libnco.la

%changelog
* Tue Aug 20 2013  <builderdev@builder.jc.rl.ac.uk> - 4.3.4-2.ceda
- devel depends on explicit version of nco

* Tue Aug 20 2013  <builderdev@builder.jc.rl.ac.uk> - 4.3.4-1.ceda
- migrate to 4.3.4, tidy spec file, add gsl dependency
			
* Mon Aug 13 2012 Alan Iwi
alan.iwi@stfc.ac.uk 4.2.1
- Created initial RPM for netCDF 4.2.1 (modelled on RPM for HDF5 1.8.9)
