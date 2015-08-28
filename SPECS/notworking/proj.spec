Name:           proj
Version:        4.8.0
Release:        1.ceda%{?dist}
Summary:        Cartographic projection software (PROJ.4)

Group:          Applications/Engineering
License:        MIT
URL:            http://proj.osgeo.org
Source0:        http://download.osgeo.org/proj/proj-%{version}.tar.gz
Source1:        http://download.osgeo.org/proj/proj-datumgrid-1.5.zip
Patch0:		proj-4.8.0-removeinclude.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libtool


%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions.


%package devel
Summary:        Development files for PROJ.4
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains libproj and the appropriate header files and man pages.


%package static
Summary:        Development files for PROJ.4
Group:          Development/Libraries

%description static
This package contains libproj static library.


%package nad
Summary:        US and Canadian datum shift grids for PROJ.4
Group:          Applications/Engineering
Requires:       %{name} = %{version}-%{release}

%description nad
This package contains additional US and Canadian datum shift grids.


%package epsg
Summary:        EPSG dataset for PROJ.4
Group:          Applications/Engineering
Requires:       %{name} = %{version}-%{release}

%description epsg
This package contains additional EPSG dataset.

%prep
%setup -q
%patch0 -p0

# disable internal libtool to avoid hardcoded r-path
for makefile in `find . -type f -name 'Makefile.in'`; do
sed -i 's|@LIBTOOL@|%{_bindir}/libtool|g' $makefile
done

# Prepare nad
cd nad
unzip %{SOURCE1}
cd ..
# fix shebag header of scripts
for script in `find nad/ -type f -perm -a+x`; do
sed -i -e '1,1s|:|#!/bin/bash|' $script
done

%build

# fix version info to respect new ABI
sed -i -e 's|5\:4\:5|6\:4\:6|' src/Makefile*

%configure
make OPTIMIZE="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -p -m 0644 nad/pj_out27.dist nad/pj_out83.dist nad/td_out.dist $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 0755 nad/test27 nad/test83 nad/testvarious $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 0644 nad/epsg $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install projects.h manually, per #830496:
install -p -m 0644 src/projects.h $RPM_BUILD_ROOT%{_includedir}/

%check
pushd nad
# set test enviroment for porj
export PROJ_LIB=$RPM_BUILD_ROOT%{_datadir}/%{name}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH%{buildroot}%{_libdir}
# run tests for proj
./test27      $RPM_BUILD_ROOT%{_bindir}/%{name} || exit 0
./test83      $RPM_BUILD_ROOT%{_bindir}/%{name} || exit 0
./testIGNF    $RPM_BUILD_ROOT%{_bindir}/%{name} || exit 0
./testntv2    $RPM_BUILD_ROOT%{_bindir}/%{name} || exit 0
./testvarious $RPM_BUILD_ROOT%{_bindir}/%{name} || exit 0
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_mandir}/man3/*.3*
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/libproj.la

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_libdir}/libproj.la


%files nad
%defattr(-,root,root,-)
%doc nad/README
%attr(0755,root,root) %{_datadir}/%{name}/test27
%attr(0755,root,root) %{_datadir}/%{name}/test83
%attr(0755,root,root) %{_datadir}/%{name}/testvarious
%attr(0755,root,root) %{_libdir}/pkgconfig/%{name}.pc
%exclude %{_datadir}/%{name}/epsg
%{_datadir}/%{name}

%files epsg
%defattr(-,root,root,-)
%doc nad/README
%attr(0644,root,root) %{_datadir}/%{name}/epsg

%changelog
* Mon Jul 13 2015  <builderdev@builder.jc.rl.ac.uk> - 4.8.0-1.ceda
- rebuild of Fedora RPM on JASMIN

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Devrim GÜNDÜZ <devrim@gunduz.org> 4.8.0-3
- Install projects.h manually, per #830496.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Devrim GÜNDÜZ <devrim@gunduz.org> 4.8.0-1
- Update to 4.8.0, per bz #814851

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-3
- fix for bz#562671

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-2
- fix for bz#556091

* Fri Dec 4 2009 Devrim GÜNDÜZ <devrim@gunduz.org> 4.7.0-1
- Update to 4.7.0
- Update to new datumgrid (1.5)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.1-1
- new stable upstream
- new nad datumgrids
- drop debian license patch
- change homepage URLs

* Sun Apr 20 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.0-1
- new branch

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-4
- BuildRequire: libtool

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-3
- enable EPSG dataset to be packed GRASS really needs it
- no more license issue over epsg dataset, proj didnt altered
  EPSG dataset in any way, so its fully EPSG license compliant
- add support for tests during buildtime
- disable hardcoded r-path from libs
- fix shebag for nad scripts

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.5.0-2
- Autorebuild for GCC 4.3

* Tue Jan   2 2007 Shawn McCann <mccann0011@hotmail.com> - 4.5.0-1
- Updated to proj-4.5.0 and datumgrid-1.3

* Sat Sep  16 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-4
- Rebuild for Fedora Extras 6

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-3
- Rebuild for Fedora Extras 5

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-2
- Rebuild for Fedora Extras 5

* Thu Jul  7 2005 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-1
- Updated to proj-4.4.9 and to fix bugzilla reports 150013 and 161726. Patch2 can be removed once this package is upgraded to the next release of the source.

* Sun May 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-6
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-5
- rebuilt

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-4
- Added testvarious to nad distribution

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.3
- Added patch for test scripts so that they will work in installed rpm

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.2
- Fixed permissions on nad27 and nad83
- Included test27 and test83 in the nad rpm and made them executable

* Fri Aug 13 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.8-0.fdr.1
- Updated to version 4.4.8 of library.
- Changed license file so that it agrees with Debian version.
- Updated web addresses of packages.

* Wed Aug 11 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.3
- Removed the "Requires(post,postun)"

* Tue Dec 30 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.2
- proj-nad now owns %{_datadir}/%{name}

* Wed Oct 29 2003 Steve Arnold <sarnold@arnolds.dhs.org>
- Basically re-wrote previous spec file from scratch so as
- to comply with both Fedora and RedHat 9 packaging guidelines.
- Split files into proj, proj-devel, and proj-nad (additional grids)
- and adjusted the EXE path in the test scripts.
