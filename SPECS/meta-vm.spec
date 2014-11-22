Summary: Meta-RPMs for JASMIN science VM and for Lotus VM
Name: jasmin-meta-vm
Version: 1.1
Release: 23.ceda
Group: Utilities/Configuration
License: Copyright STFC
BuildRoot: %{_builddir}/%{name}-root
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
BuildArch: noarch
#
# Top-level package only used for SRPM (as no corresponding %files section).
# This gives the SPRM a more generic name than common/sci/lotus.
#
%description
Source RPM for meta-RPMs for JASMIN science VM and for Lotus VM

%package -n jasmin-common-vm
Summary: Adds common configuration for JASMIN science VM and for Lotus VM
Requires: ImageMagick >= 6.5.4.7
Requires: R >= 2.10.0
Requires: R-devel >= 2.10.0
Requires: arpack >= 3.0.1
Requires: atlas >= 3.8.4
Requires: atlas-devel >= 3.8.4
Requires: bbcp >= 140414.00.1-1.ceda
Requires: bbcp-config >= 1-1.ceda
Requires: blas >= 3.2.1
Requires: cdo >= 1.5.6.1-3.ceda
Requires: cmor-devel >= 2.8.2-2.ceda
Requires: ddd >= 3.3.12
Requires: emacs >= 23.1
Requires: emacs-gnuplot >= 4.2.6
Requires: fftw >= 3.2.1
Requires: fftw-devel >= 3.2.1
Requires: firefox >= 17.0.3
Requires: gcc-gfortran >= 4.4.7
Requires: gdal >= 1.9.2-1.ceda
Requires: gdal-devel >= 1.9.2-1.ceda
Requires: gdal-doc >= 1.9.2-1.ceda
Requires: gdal-java >= 1.9.2-1.ceda
Requires: gdal-javadoc >= 1.9.2-1.ceda
Requires: gdal-perl >= 1.9.2-1.ceda
Requires: gdal-python27 >= 1.9.2-1.ceda
Requires: gdal-ruby >= 1.9.2-1.ceda
Requires: geany >= 0.21
Requires: geos >= 3.3.6-2.ceda
Requires: geos-devel >= 3.3.6-2.ceda
Requires: git >= 1.7.1
Requires: gitk >= 1.7.1
Requires: gnuplot >= 4.2.6
Requires: grib_api >= 1.12.1-1.ceda
Requires: grib_api-devel >= 1.12.1-1.ceda
Requires: grib_api-fortran >= 1.12.1-1.ceda
Requires: grib_api-python27 >= 1.12.1-1.ceda
Requires: gsl-devel >= 1.13
Requires: gsl-static >= 1.13
Requires: gv >= 3.7.1
Requires: hdf >= 4.2.9-1.ceda
Requires: hdf-devel >= 4.2.9-1.ceda
Requires: hdf-devel >= 4.2.9-1.ceda
Requires: hdf5 >= 1.8.9-2.ceda
Requires: hdf5-devel >= 1.8.9-2.ceda
Requires: ksh >= 20100621
Requires: lapack >= 3.2.1
Requires: lapack-devel >= 3.2.1
Requires: leafpad >= 0.8.18
Requires: libuuid >= 2.17.2
Requires: libuuid >= 2.17.2
Requires: mo_unpack >= 2.0.1-1.ceda
Requires: ncBrowse >= 1.6.5
Requires: ncl >= 6.1.2-1.ceda
Requires: nco >= 4.4.2-1.ceda
Requires: nco-devel >= 4.4.2-1.ceda
Requires: ncview >= 2.1.2-1.ceda
Requires: nedit >= 5.5
Requires: netcdf >= 4.3.2-1.ceda
Requires: netcdf-c++ >= 4.2-3.ceda
Requires: netcdf-c++-devel >= 4.2-3.ceda
Requires: netcdf-devel >= 4.3.2-1.ceda
Requires: netcdf-fortran >= 4.2-3.ceda
Requires: netcdf-fortran-devel >= 4.2-3.ceda
Requires: octave >= 3.6.4-1.ceda
Requires: octave-devel >= 3.6.4-1.ceda
Requires: octave-doc >= 3.6.4-1.ceda
Requires: octave-octcdf >= 1.1.5-1.ceda
Requires: perl-core >= 5.10.1
Requires: perl-devel >= 5.10.1
Requires: python27 >= 2.7.3-3.ceda
Requires: python27-Cython >= 0.17.3-1.ceda
Requires: python27-Jug >= 0.9.6-1.ceda
Requires: python27-PIL >= 1.1.7-2.ceda
Requires: python27-Pydap >= 3.1.RC1-2.ceda
Requires: python27-Pygments >= 1.5-3.ceda
Requires: python27-Shapely >= 1.2.16-2.ceda
Requires: python27-basemap >= 1.0.5-4.ceda
Requires: python27-cartopy >= 0.7.0-2.ceda
Requires: python27-cdat_lite >= 6.0rc2-4.ceda
Requires: python27-cf >= 0.9.8.1-1.ceda
Requires: python27-cf-checker >= 2.0.5-4.ceda
Requires: python27-cfplot >= 1.2-1.ceda
Requires: python27-cmor >= 2.8.2-2.ceda
Requires: python27-ipython >= 2.0.0-1.ceda
Requires: python27-iris >= 1.7.1-1.ceda
Requires: python27-jasmin_cis >= 0.7-1.ceda
Requires: python27-matplotlib >= 1.2.0-1.ceda
Requires: python27-nappy >= 1.1.2-1.ceda
Requires: python27-netCDF4 >= 1.0.7-2.ceda
Requires: python27-nose >= 1.3.4-1.ceda
Requires: python27-numpy >= 1.7.0-3.ceda
Requires: python27-pandas >= 0.12.0-1.ceda
Requires: python27-pycairo >= 1.8.6-1.ceda
Requires: python27-pygobject2 >= 2.20.0-1.ceda
Requires: python27-pygtk2 >= 2.16.0-1.ceda
Requires: python27-pygtk2-libglade >= 2.16.0-1.ceda
Requires: python27-pyhdf >= 0.8_1-2.ceda
Requires: python27-pyke >= 1.1.1-1.ceda
Requires: python27-pyspharm >= 1.0.8-1.ceda
Requires: python27-pyzmq >= 2.2.0.1-3.ceda
Requires: python27-rpy2 >= 2.3.9-1.ceda
Requires: python27-scipy >= 0.13.1-1.ceda
Requires: python27-setuptools >= 0.6c12dev_r88846-2.ceda
Requires: python27-shapefile >= 1.1.4-1.ceda
Requires: python27-six >= 1.5.2-1.ceda
Requires: python27-tornado >= 3.2-1.ceda
Requires: python27-virtualenv >= 1.8.2-2.ceda
Requires: python27-windspharm >= 1.3.1-1.ceda
Requires: subversion >= 1.6.11
Requires: tcl >= 8.5.7
Requires: tcl-devel >= 8.5.7
Requires: tcsh >= 6.17
Requires: thea >= 0.1
Requires: tk >= 8.5.7
Requires: tk-devel >= 8.5.7
Requires: tkdiff >= 4.2
Requires: udunits >= 2.1.24
Requires: udunits-devel >= 2.1.24
Requires: umutil >= 20130102-1.ceda
Requires: uuid >= 1.6.1
Requires: uuid-devel >= 1.6.1
Requires: vim-enhanced >= 7.2.411
Requires: xconv >= 1.92dev-1.ceda
Requires: xemacs >= 21.5.31
Requires: xpdf >= 3.02


%description -n jasmin-common-vm
Adds common configuration for JASMIN science VM and for Lotus VMs.
You should install either jasmin-sci-vm or jasmin-lotus-vm, which depend on this.

%package -n jasmin-sci-vm
Summary: Adds configuration for JASMIN science VM
Requires: jasmin-common-vm = %{version}-%{release}
Requires: mpich2 >= 1.2.1
Requires: python27-mpi4py-mpich2 >= 1.3
%description -n jasmin-sci-vm
Adds configuration for JASMIN science VM

%package -n lotus-vm
Summary: Adds configuration for Lotus VM
Requires: jasmin-common-vm = %{version}-%{release}
Requires: python27-mpi4py-platform_mpi >= 1.3-1
%description -n lotus-vm
Adds configuration for Lotus VM

%prep
%build
%clean
%install
%files -n jasmin-common-vm
%files -n jasmin-sci-vm
%files -n lotus-vm

%changelog
* Fri Sep 12 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-23.ceda
-        bbcp >= 140414.00.1-1.ceda
-        bbcp-config >= 1-1.ceda
-        netcdf >= 4.3.2-1.ceda
-        netcdf-c++ >= 4.2-3.ceda
-        netcdf-c++-devel >= 4.2-3.ceda
-        netcdf-devel >= 4.3.2-1.ceda
-        netcdf-fortran >= 4.2-3.ceda
-        netcdf-fortran-devel >= 4.2-3.ceda
-        python27-cf-checker >= 2.0.5-4.ceda
-        python27-iris >= 1.7.1-1.ceda
-        python27-nose >= 1.3.4-1.ceda
-        python27-pyspharm >= 1.0.8-1.ceda
-        python27-windspharm >= 1.3.1-1.ceda
-    gitk >= 1.7.1
* Fri Jul 11 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-22.ceda
- deprecate gedit
- add gsl-devel and gsl-static

* Fri Jun 27 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-21.ceda
-     grib_api >= 1.12.1-1.ceda
-     grib_api-devel >= 1.12.1-1.ceda
-     grib_api-fortran >= 1.12.1-1.ceda
-     grib_api-python27 >= 1.12.1-1.ceda
-     ncl >= 6.1.2-1.ceda
-     python27-PIL >= 1.1.7-2.ceda
-     python27-ipython >= 2.0.0-1.ceda
-     python27-jasmin_cis >= 0.7-1.ceda
         (implies python27-backports-ssl_match_hostname)
-     python27-pycairo >= 1.8.6-1.ceda
-     python27-pygobject2 >= 2.20.0-1.ceda
-     python27-pygtk2 >= 2.16.0-1.ceda
-     python27-pygtk2-libglade >= 2.16.0-1.ceda
-     python27-tornado >= 3.2-1.ceda
- leafpad >= 0.8.18
- perl-core >= 5.10.1

* Fri Feb 21 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-20.ceda
- python27-2.7.3-3.ceda, python27-rpy2-2.3.9-1.ceda

* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-19.ceda
- python27-iris 1.6.1

* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-18.ceda
- insert cfplot

* Mon Feb 17 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-16.ceda
- NCO to 4.4.2, fixes issues in 4.4.1

* Tue Feb 11 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-13.ceda
- downgrade NCO to 4.3.4

* Thu Feb  6 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-11.ceda
- various upgrades:
-       nco-4.4.1-1.ceda
-       python27-Jug-0.9.6-1.ceda
-       python27-cdat_lite-6.0rc2-3.ceda
-       python27-cf-0.9.8.1-1.ceda
-       python27-netCDF4-1.0.7-2.ceda
-       python27-nose-1.2.0-3.ceda
-       python27-setuptools-0.6c12dev_r88846-2.ceda
-       python27-six-1.5.2-1.ceda
-       python27-virtualenv-1.10.1-2.ceda
-       xconv-1.92dev-1.ceda
- add release numbers for most CEDA packages

* Thu Jan 23 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-10.ceda
- netCDF 4.3.1 and rebuilt c++/fortran bindings, python27-netCDF 1.0.7

* Thu Dec 12 2013  <builderdev@builder.jc.rl.ac.uk> - 1.1-8.ceda
- python27-cf 0.9.8

* Thu Nov 28 2013  <builderdev@builder.jc.rl.ac.uk> - 1.1-6.ceda
- upgrade ipython (to 1.1.0); add lapack and lapack-devel

* Fri Aug 30 2013  <builderdev@builder.jc.rl.ac.uk> - 1.1-3.ceda
- + pandas

* Wed Jul 31 2013  <builderdev@builder.jc.rl.ac.uk> - 1.1
- move to common / jasmin / lotus layout
- add explicit version numbers for all packages

* Wed Jul 10 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-6.ceda
- add grib_api*, jasmin_cis, Jug, umutil

* Fri Jun 21 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-4.ceda
- include netCDF c++ (and devel)

* Mon Jun  3 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-4.ceda
- remove mpich2 stuff

* Thu May 30 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-3.ceda
- add perl-devel

* Fri Apr 26 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-2.ceda
- add gdal stuff

* Fri Feb 22 2013 Alan Iwi <alan.iwi@stfc.ac.uk> 1.0
Auto-generated spec from package list by rpm_tools.py
