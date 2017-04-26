%define __python python2.7
%define python_version 2.7

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           gdl
Version:        0.9.5
Release:        1.ceda%{?dist}
Summary:        GNU Data Language

Group:          Applications/Engineering
License:        GPLv2+
URL:            http://gnudatalanguage.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gnudatalanguage/%{name}-%{version}.tar.gz
Source1:        gdl.csh
Source2:        gdl.sh
Source3:        makecvstarball
# Build with system antlr library.  Request for upstream change here:
# https://sourceforge.net/tracker/index.php?func=detail&aid=2685215&group_id=97659&atid=618686
Patch1:         gdl-0.9-antlr-cmake.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#RHEL5 doesn't have the needed antlr version/headers, has old plplot
%if 0%{?rhel} == 5
%global plplot_config --enable-oldplplot
%else
%global plplot_config %{nil}
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  antlr-C++
BuildRequires:  antlr-tool
%endif
%if 0%{?rhel} == 6
BuildRequires:  antlr
BuildRequires:  java
%endif
BuildRequires:  readline-devel, ncurses-devel
BuildRequires:  gsl-devel, plplot-devel, GraphicsMagick-c++-devel
BuildRequires:  netcdf-devel, hdf5-devel, libjpeg-devel
BuildRequires:  python27, python27-numpy, python27-matplotlib
BuildRequires:  fftw-devel, hdf-static
#%if 0%{?fedora} >= 21
BuildRequires:  grib_api-devel
#%else
# %if 0%{?fedora} || 0%{?rhel} >= 6
# BuildRequires:  grib_api-static
# %endif
#%endif
BuildRequires:  eigen3-static
#TODO - Build with mpi support
#BuildRequires:  mpich2-devel
BuildRequires:  pslib-devel
BuildRequires:  udunits2-devel
BuildRequires:  wxGTK-devel
BuildRequires:  cmake
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
# Need to match hdf5 compile time version
Requires:       hdf5 = %{_hdf5_version}


%description
A free IDL (Interactive Data Language) compatible incremental compiler
(i.e. runs IDL programs). IDL is a registered trademark of Research
Systems Inc.


%package        common
Summary:        Common files for GDL
Group:          Applications/Engineering
Requires:       %{name}-runtime = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildArch:      noarch
%endif

%description    common
Common files for GDL


%package        python27
Summary:        GDL python module
Group:          Applications/Engineering
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description    python27
%{summary}.


%prep
%setup -q
rm -rf src/antlr
%patch1 -p1 -b .antlr
pushd src
for f in *.g
do
  antlr $f
done
popd

%global cmake_opts \\\
   -DWXWIDGETS=ON \\\
   -DUDUNITS=ON \\\
   -DUDUNITS_INCLUDE_DIR=%{_includedir}/udunits2 \\\
   -DGRIB=ON \\\
   -DOPENMP=ON \\\
%{nil}
# TODO - build an mpi version
#           INCLUDES="-I/usr/include/mpich2" \
#           --with-mpich=%{_libdir}/mpich2 \

%build
export CPPFLAGS="-DH5_USE_16_API"
# Build convenience .a libraries with -fPIC
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
# Need to find numpy include files as well
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I%{python_sitearch}/numpy/core/include"
mkdir build build-python
#Build the standalone executable
pushd build
%{cmake} %{cmake_opts} ..
make %{?_smp_mflags}
popd
#Build the python module
pushd build-python
%{cmake} %{cmake_opts} -DPYTHON_MODULE=ON -DPYTHON_VERSION=%{python_version} ..
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd
pushd build-python
make install DESTDIR=$RPM_BUILD_ROOT
# Install the python module
install -d -m 0755 $RPM_BUILD_ROOT/%{python_sitearch}
cp -p src/libgdl.so \
      $RPM_BUILD_ROOT/%{python_sitearch}/GDL.so
popd

# Install the profile file to set GDL_PATH
install -d -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d


%check
cd build
# It takes more stack to compile gdlffdicom__dictionary.pro
# https://sourceforge.net/p/gnudatalanguage/discussion/338693/thread/6c1015e9/
ulimit -s 16384
# test_execute expects to use DISPLAY
# test_bug_3147146 failure
# https://sourceforge.net/p/gnudatalanguage/bugs/619/
# test_zip - https://sourceforge.net/p/gnudatalanguage/bugs/632/
%ifarch %{arm} aarch64 ppc64
# test_fix fails currently on arm
# https://sourceforge.net/p/gnudatalanguage/bugs/622/
# https://bugzilla.redhat.com/show_bug.cgi?id=990749
make check ARGS="-V -E 'test_execute|test_bug_3147146|test_fix|test_zip'"
%else
make check ARGS="-V -E 'test_execute|test_bug_3147146|test_zip'"
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING HACKING NEWS README TODO
%config(noreplace) %{_sysconfdir}/profile.d/gdl.*sh
%{_bindir}/gdl
%{_mandir}/man1/gdl.1*

%files common
%{_datadir}/gnudatalanguage/

%files python27
%{python_sitearch}/GDL.so


%changelog
* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 0.9.5-1.ceda
- rebuild with netcdf 4.4.0 and python 2.7
- force grib_api-devel instead of grib_api-static dependency

* Fri Feb 12 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9.5-4
- rebuild (GraphicsMagick)

* Tue Nov 18 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-3
- Exclude test_zip

* Fri Oct 31 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-2
- No longer need cmake28 on RHEL6

* Wed Oct 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-1
- Update to 0.9.5
- Disable tests which fail on aarch64 (#990749)
- Add patch to support new width() method in plplot
- Build with shared grib_api
- Switch to GraphicsMagick
- BR netcdf-devel instead of netcdf-cxx-devel
- Change to use cmake
- Build with eigen3

* Thu Dec 27 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-1
- Update to 0.9.3
- Rebase antlr-auto patch
- Drop env patch fixed upstream

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-6.cvs20120515
- Update to current cvs
- Add patch for testsuite make check to work in build directory
- Add patch to fix pythongdl.c compile
- Run the testsuite properly with make check

* Wed Mar 21 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-5
- Rebuild antlr generated files
- Rebuild for ImageMagick

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for c++ ABI breakage

* Wed Jan 11 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-3.1
- Rebuild with proper hdf5

* Sat Jan 7 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-3
- Build with pslib

* Fri Nov 11 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-1
- Update to 0.9.2
- Drop upstreamed patches
- Drop hdf support from python module, add patch to force building of python
  shared library

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for glibc bug#747377

* Thu Aug 18 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-4
- Rebuild for plplot 5.9.8
- Add upstream patch to fix strsplit and str_sep
- Add patch to fix compile issues with string
- Add patch to change plplot SetOpt to setopt

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-3
- Rebuild for hdf5 1.8.7

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-2
- Rebuild for netcdf 4.1.2

* Tue Mar 29 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-1
- Update to 0.9.1
- Drop numpy and wx patches fixed upstream

* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-6
- Add include path to numpy (needed on EL6)

* Mon Oct 11 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-5
- Rebuild for plplot 5.9.7

* Wed Sep 29 2010 jkeating - 0.9-4
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-3
- Fix GDL_PATH in profile scripts (bug #634351)

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-2
- Rebuild for new ImageMagick

* Mon Aug 30 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-1
- Update to 0.9 final

* Thu Aug 26 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.17.rc4
- Add initial patch to build the python module with numpy rather than
  numarray.  Doesn't work yet, but the python module is mostly dead anyway

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-0.16.rc4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9-0.15.rc4
- rebuilt against wxGTK-2.8.11-2

* Wed Jul 7 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.14.rc4
- Update to today's cvs
- Drop wx-config patch
- Re-instate wx patch to avoid segfault on test exit

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.13.rc4
- Update to today's cvs
- Drop GLDLexer and python patches
- BR antlr-C++ on Fedora 14+

* Mon Mar 22 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.12.rc4
- Drop unused BR on proj-devel (bug #572616)

* Mon Mar 8 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.11.rc4
- Rebuild for new ImageMagick

* Wed Feb 17 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.10.rc4
- Update to 0.9rc4
- Enable grib, udunits2, and wxWidgets support
- Build python module and add sub-package for it
- Use %%global instead of %%define

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9-0.9.rc3
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Wed Nov 11 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.8.rc3
- Rebuild for netcdf-4.1.0

* Thu Oct 15 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.7.rc3
- Update to 0.9rc3
- Drop gcc43, ppc64, friend patches fixed upstream
- Add source for makecvstarball
- Rebase antlr patch, add automake source version
- Add conditionals for EPEL builds
- Add %%check section

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.rc2.20090312
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.5.rc2.20090312
- Back off building python module until configure macro is updated

* Thu Mar 12 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.4.rc2.20090312
- Update to 0.9rc2 cvs 20090312
- Rebase antlr patch
- Rebuild for new ImageMagick

* Thu Feb 26 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.3.rc2.20090224
- Build python module
- Move common code to noarch common sub-package

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.2.rc2.20090224
- Update to 0.9rc2 cvs 20090224
- Fix release tag
- Drop ImageMagick patch fixed upstream
- Add patch to compile with gcc 4.4.0 - needs new friend statement
- Don't build included copy of antlr, use system version

* Fri Jan 23 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc2.1
- Update to 0.9rc2 based cvs

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9-0.rc1.4.1
- Rebuild for Python 2.6

* Fri Sep  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.4
- Add a requires on plplot to pull in drivers (bug#458277)

* Fri May 16 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.3
- Update to latest cvs
- Add patch to handle new ImageMagick
- Update netcdf locations

* Mon Apr 28 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.2
- Rebuild for new ImageMagick

* Sat Apr  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.1
- Update to 0.9rc1

* Mon Mar 17 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.2
- Update cvs patch to latest cvs

* Tue Mar 4 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.1
- Rebuild for gcc 4.3, and add patch for gcc 4.3 support
- Add patch to build against plplot 5.9.0
- Add cvs patch to update to latest cvs

* Fri Nov  2 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6
- Update to 0.9pre6

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.2
- Add patch to fix build on ppc64

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.1
- Update license tag to GPLv2+
- Rebuild for BuildID

* Mon Jul  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5
- Update to 0.9pre5

* Tue May 22 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.2
- Rebuild for netcdf 3.6.2 with shared libraries

* Tue Jan  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.1
- Package the library routines and point to them by default

* Fri Jan  5 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4
- Update to 0.9pre4

* Mon Dec 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.4
- Add patch for configure to handle python 2.5

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 0.9-0.pre3.3
- Bump and build for python 2.5

* Wed Nov 22 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.2
- Update to 0.9pre3

* Wed Oct  4 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.1
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3
- Rebuild for FC6
- Add patch for specialization error caught by gcc 4.1.1

* Thu Jun 29 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre2
- Update to 0.9pre2

* Sun Jun 11 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre.1
- Rebuild for ImageMagick so bump

* Mon Apr  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre
- Update to 0.9pre

* Fri Feb 24 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-4
- Add --with-fftw to configure

* Thu Feb  2 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-3
- Enable hdf for ppc
- Change fftw3 to fftw

* Tue Jan  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-2
- Rebuild

* Mon Nov 21 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-1
- Upstream 0.8.11
- Remove hdf patch fixed upstream
- Remove X11R6 lib path - not needed with modular X

* Wed Nov 16 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-4
- Update for new ImageMagick version

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-3
- Disable hdf with configure on ppc

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-2
- Don't include hdf support on ppc

* Fri Aug 19 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-1
- Initial Fedora Extras version
