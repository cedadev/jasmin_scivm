Summary: Meta-RPMs for JASMIN science VM and for Lotus VM
Name: jasmin-meta-vm
Version: 1.1
Release: 32.ceda
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

Obsoletes: gdal-ruby
Obsoletes: python-nose

# Requires: jasper-devel >= 1.900

Requires: ImageMagick >= 6.5.4.7
Requires: JAGS >= 4.2.0-1.ceda
Requires: R >= 3.3.1
Requires: R-devel >= 3.3.1
Requires: R-ncdf >= 1.6.8-2.ceda
Requires: arpack >= 3.0.1
Requires: atlas >= 3.8.4
Requires: atlas-devel >= 3.8.4
Requires: bbcp >= 140414.00.1-1.ceda
Requires: bbcp-config >= 1-1.ceda
Requires: blas >= 3.2.1
Requires: cdo >= 1.7.2-1.ceda
Requires: cmor-libs >= 2.9.2-3.ceda
Requires: coda >= 0.18.1-1.ceda
Requires: ddd >= 3.3.12
Requires: diffuse >= 0.4.3-1
Requires: dvipng >= 1.11
Requires: eccodes-devel >= 2.4.0-1.ceda
Requires: eccodes-fortran >= 2.4.0-1.ceda
Requires: eccodes >= 2.4.0-1.ceda
Requires: eccodes-python27 >= 2.4.0-1.ceda
Requires: emacs >= 23.1
Requires: emacs-common-ess >= 15.03.1-1.ceda
Requires: emacs-ess >= 15.03.1-1.ceda
Requires: emacs-ess-el >= 15.03.1-1.ceda
Requires: emacs-gnuplot >= 4.2.6
Requires: ferret >= 6.93-1.ceda
Requires: flex-devel
Requires: fftw >= 3.2.1
Requires: fftw-devel >= 3.2.1
Requires: firefox >= 17.0.3
Requires: gcc-gfortran >= 4.4.7
Requires: gdal >= 2.1.1-1.ceda 
Requires: gdal-devel >= 2.1.1-1.ceda
Requires: gdal >= 2.1.1-1.ceda
Requires: gdal-perl >= 2.1.1-1.ceda
Requires: gdal-libs >= 2.1.1-1.ceda
Requires: gdal-java >= 2.1.1-1.ceda
Requires: gdal-python27 >= 2.1.1-1.ceda
Requires: geany >= 0.21
Requires: geos >= 3.5.0-2.ceda
Requires: geos-devel >= 3.5.0-2.ceda
Requires: git >= 1.7.1
Requires: gitk >= 1.7.1
Requires: glibc-static >= 2.12
Requires: gnuplot >= 4.2.6

# force GraphicsMagick version for Octave
Requires: GraphicsMagick-c++ = 1.3.20-3.el6

# grass: force exact versions to avoid having to put epel in 
# excludes
Requires: grass = 6.4.4-3.ceda.el6
Requires: grass-devel = 6.4.4-3.ceda.el6
Requires: grass-libs = 6.4.4-3.ceda.el6

# and likewise
Requires: grib_api = 1.17.0-1.ceda.el6
Requires: grib_api-devel = 1.17.0-1.ceda.el6
Requires: grib_api-fortran = 1.17.0-1.ceda.el6
Requires: grib_api-python27 = 1.17.0-1.ceda.el6

Requires: gsl-devel >= 1.13
Requires: gsl-static >= 1.13
Requires: gtk2-devel
Requires: gv >= 3.7.1
Requires: hdf >= 4.2.9-1.ceda
Requires: hdf-devel >= 4.2.9-1.ceda
Requires: hdf5 >= 1.8.12-2.ceda
Requires: hdf5-devel >= 1.8.12-2.ceda
Requires: hdfeos2 >= 19.1.00-1.ceda
Requires: hdfeos5 >= 1.15-1.ceda
Requires: jasper-devel >= 1.900.1-16
Requires: ksh >= 20100621
Requires: lapack >= 3.2.1
Requires: lapack-devel >= 3.2.1
Requires: leafpad >= 0.8.18
Requires: libcdms >= 6.0rc2-6.ceda
Requires: libdrs >= 20130102-3.ceda
Requires: libuuid >= 2.17.2
Requires: llvm-devel >= 3.4.2-4
Requires: lxterminal >= 0.1.9-1.ceda
Requires: mo_unpack >= 3.1.2-1.ceda
Requires: mtk >= 1.4.3-1.ceda
Requires: mtk-devel >= 1.4.3-1.ceda
Requires: mtk-python27 >= 1.4.3-1.ceda
Requires: ncBrowse >= 1.6.5
Requires: nccmp >= 1.7.5.1-2.ceda
Requires: ncl >= 6.3.0-3.ceda
Requires: nco >= 4.5.5-1.ceda
Requires: nco-devel >= 4.5.5-1.ceda
Requires: ncview >= 2.1.7-1.ceda
Requires: nedit >= 5.5
Requires: netcdf >= 4.4.0-1.ceda
Requires: netcdf-c++ >= 4.2-4.ceda
Requires: netcdf-c++-devel >= 4.2-4.ceda
Requires: netcdf-devel >= 4.4.0-1.ceda
Requires: netcdf-fortran >= 4.4.3-2.ceda
Requires: netcdf-fortran-devel >= 4.4.3-2.ceda
Requires: octave >= 4.0.0-2.ceda
Requires: octave-devel >= 4.0.0-2.ceda
Requires: octave-doc >= 4.0.0-2.ceda
Requires: octave-netcdf >= 1.0.7-2.ceda
Requires: octave-octcdf >= 1.1.8-3.ceda
Requires: parallel >= 20160822-1.ceda
Requires: p7zip
Requires: pdftk >= 2.02-1
Requires: perl-Image-ExifTool >= 9.98-1.ceda
Requires: perl-XML-Parser >= 2.36
Requires: perl-core >= 5.10.1
Requires: perl-devel >= 5.10.1
Requires: postgresql-devel
Requires: proj >= 4.9.0-1.ceda
Requires: proj-devel >= 4.9.0-1.ceda
Requires: proj-epsg >= 4.9.0-1.ceda
Requires: proj-nad >= 4.9.0-1.ceda
Requires: proj-static >= 4.9.0-1.ceda
Requires: python27 >= 2.7.3-3.ceda
Requires: python27-Cython >= 0.24-1.ceda
Requires: python27-Jug >= 0.9.6-1.ceda
Requires: python27-PIL >= 1.1.7-2.ceda
Requires: python27-Pydap >= 3.1.RC1-2.ceda
Requires: python27-Pygments >= 1.5-3.ceda
Requires: python27-ScientificPython >= 2.9.4-2.ceda
Requires: python27-Shapely >= 1.5.17-1.ceda
Requires: python27-astral >= 1.4-1.ceda.el6
Requires: python27-basemap >= 1.0.5-4.ceda
Requires: python27-biggus >= 0.15.0-1.ceda
Requires: python27-cartopy >= 0.14.2-2.ceda
Requires: python27-cdat_lite >= 6.0rc2-6.ceda
Requires: python27-cf >= 1.5.4.post1-1.ceda
Requires: python27-cf-checker >= 3.0.5-1.ceda
Requires: python27-cf_units >= 1.1.3-1.ceda
Requires: python27-cf-plot >= 2.1.35-1.ceda
Requires: python27-cf-view >= 1.0.4-1.ceda
Requires: python27-cis >= 1.5.4-1.ceda
Requires: python27-cmor >= 2.9.2-3.ceda
Requires: python27-cycler >= 0.10.0-1.ceda
Requires: python27-ecmwf-api-client >= 1.4.2-1.ceda
Requires: python27-eofs >= 1.2.0-1.ceda
Requires: python27-esgf-pyclient >= 0.1.8-1.ceda
Requires: python27-h5py >= 2.6.0-1.ceda
Requires: python27-ipython >= 2.0.0-1.ceda
Requires: python27-iris >= 1.10.0-2.ceda
Requires: python27-iris-grib >= 0.9.0-1.ceda
Requires: python27-iris_sample_data >= 2.0.0-1.ceda
Requires: python27-matplotlib >= 1.5.3-1.ceda
Requires: python27-mo_pack >= 0.2.0-1.ceda
Requires: python27-nappy >= 1.1.2-2.ceda
Requires: python27-nc-time-axis >= 1.0.0-1.ceda
Requires: python27-netCDF4 >= 1.2.9-1.ceda
Requires: python27-nose >= 1.3.4-1.ceda
Requires: python27-numpy >= 1.13.0-1.ceda
Requires: python27-pandas >= 0.19.1-1.ceda
Requires: python27-pycairo >= 1.8.6-1.ceda
Requires: python27-psycopg2 >= 2.6.2-1.ceda
Requires: python27-pygeode >= 1.0.4a-1.ceda
Requires: python27-pygobject2 >= 2.20.0-1.ceda
Requires: python27-pygrib >= 2.0.1-2.ceda
Requires: python27-pygtk2 >= 2.16.0-1.ceda
Requires: python27-pygtk2-libglade >= 2.16.0-1.ceda
Requires: python27-pyhdf >= 0.8_1-2.ceda
Requires: python27-pyke >= 1.1.1-1.ceda
Requires: python27-pyproj >= 1.9.5.1-1.ceda
Requires: python27-pyshp >= 1.2.10-1.ceda
Requires: python27-pyspharm >= 1.0.8-1.ceda
Requires: python27-pyzmq >= 2.2.0.1-3.ceda
Requires: python27-requests >= 2.18.1-1.ceda
Requires: python27-rpy2 >= 2.3.9-1.ceda
Requires: python27-scikit-image >= 0.13.0-1.ceda
Requires: python27-scipy >= 0.19.1-1.ceda
Requires: python27-seaborn >= 0.7.1-1.ceda
Requires: python27-setuptools >= 18.2-1.ceda
Requires: python27-six >= 1.5.2-1.ceda
Requires: python27-scikit-learn >= 0.17b1-1.ceda
Requires: python27-tornado >= 3.2-1.ceda
Requires: python27-virtualenv >= 15.0.3-3.ceda
Requires: python27-windspharm >= 1.3.1-1.ceda
Requires: python27-PyYAML >= 3.12-1.ceda
Requires: python27-Sphinx >= 1.6.3-1.ceda
Requires: redhat-lsb
Requires: rjags >= 4.6-1.ceda
Requires: sqlite-devel
Requires: subversion >= 1.8.17-1
Requires: subversion-devel >= 1.8.17-1
Requires: subversion-tools >= 1.8.17-1
Requires: tcl >= 8.5.7
Requires: tcl-devel >= 8.5.7
Requires: tcsh >= 6.17
Requires: thea >= 0.1
Requires: tk >= 8.5.7
Requires: tk-devel >= 8.5.7
Requires: tkdiff >= 4.2
Requires: tmux >= 1.6-3
Requires: udunits >= 2.1.24-3.ceda
Requires: udunits-devel >= 2.1.24-3.ceda
Requires: umutil >= 20130102-2.ceda
Requires: umutil-lib >= 20130102-2.ceda
Requires: uuid >= 1.6.1
Requires: uuid-devel >= 1.6.1
Requires: valgrind >= 3.8.1-8
Requires: vim-enhanced >= 7.2.411
Requires: wxGTK-devel
Requires: xconv >= 1.93-1.ceda
Requires: xemacs >= 21.5.31
Requires: xorg-x11-util-macros
Requires: xpdf >= 3.02


%description -n jasmin-common-vm
Adds common configuration for JASMIN science VM and for Lotus VMs.
You should install either jasmin-sci-vm or jasmin-lotus-vm, which depend on this.

%package -n jasmin-sci-vm
Summary: Adds configuration for JASMIN science VM
Requires: jasmin-common-vm = %{version}-%{release}
Requires: mpich >= 3.1-4
Requires: python27-mpi4py-mpich >= 1.3-1.ceda
Requires: esmf >= 7.0.0b57-1.ceda
Requires: esmf-doc >= 7.0.0b57-1.ceda
Requires: esmf-python27 >= 7.0.0b57-1.ceda

%description -n jasmin-sci-vm
Adds configuration for JASMIN science VM

%package -n lotus-vm
Summary: Adds configuration for Lotus VM
Requires: jasmin-common-vm = %{version}-%{release}
Requires: python27-mpi4py-platform_mpi >= 1.3-1
%description -n lotus-vm
Adds configuration for Lotus VM
Requires: esmf-lotus >= 7.0.0b57-1.ceda
Requires: esmf-lotus-doc >= 7.0.0b57-1.ceda
Requires: esmf-lotus-python27 >= 7.0.0b57-1.ceda

%prep
%build
%clean
%install
%files -n jasmin-common-vm
%files -n jasmin-sci-vm
%files -n lotus-vm

%changelog
* Mon Dec 12 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-31test.ceda
- - python27-PyYAML >= 3.12-1.ceda

* Sun Dec 11 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-31test.ceda
- python27-pandas >= 0.19.1-1.ceda
- - python27-eofs >= 1.2.0-1.ceda
- - python27-cf_units >= 1.1.3-1.ceda
- - python27-iris_sample_data >= 2.0.0-1.ceda
- - python27-nc-time-axis >= 1.0.0-1.ceda
- - python27-scikit-learn >= 0.17b1-1.ceda

* Thu Dec  8 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-31test.ceda
per issue 100:
- subversion >= 1.8.17-1
- subversion-devel >= 1.8.17-1
- subversion-tools >= 1.8.17-1

* Tue Nov  1 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-31test.ceda
- python27-psycopg2 >= 2.6.2-1.ceda

* Thu Oct 20 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-30.ceda
- python27-Shapely >= 1.5.17-1.ceda
- python27-cartopy >= 0.14.2-2.ceda
- python27-cis >= 1.4.0-1.ceda
- python27-iris >= 1.10.0-2.ceda
- python27-pyshp >= 1.2.10-1.ceda  replacing python27-shapefile

* Mon Oct 17 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-29.ceda
- cdo >= 1.7.1-1.ceda
- gdal >= 2.0.0-5.ceda
- gdal-devel >= 2.0.0-5.ceda
- gdal-doc >= 2.0.0-5.ceda
- gdal-java >= 2.0.0-5.ceda
- gdal-javadoc >= 2.0.0-5.ceda
- gdal-libs >= 2.0.0-5.ceda
- gdal-perl >= 2.0.0-5.ceda
- gdal-python27 >= 2.0.0-5.ceda
- grib_api = 1.12.1-2.ceda.el6
- grib_api-devel = 1.12.1-2.ceda.el6
- grib_api-fortran = 1.12.1-2.ceda.el6
- grib_api-python27 = 1.12.1-2.ceda.el6
- mo_unpack >= 2.0.1-1.ceda
- ncl >= 6.3.0-2.ceda
- python27-Cython >= 0.17.3-1.ceda
- python27-cartopy >= 0.11.2-1.ceda
- python27-cf >= 1.1.5-1.ceda
- python27-iris >= 1.9.2-1.ceda
- python27-matplotlib >= 1.4.3-1.ceda
- python27-pygrib >= 2.0.1-1.ceda
- python27-virtualenv >= 1.8.2-2.ceda

* Wed May 25 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1-28.ceda
- python27-biggus >= 0.13.0-1.ceda

* Fri Apr 8 2016 <alan.iwi@stfc.ac.uk> - 1.1-27.ceda
-  cdo >= 1.7.1-1.ceda
-  cmor-libs >= 2.9.2-3.ceda
-  emacs-common-ess >= 15.03.1-1.ceda
-  emacs-ess >= 15.03.1-1.ceda
-  emacs-ess-el >= 15.03.1-1.ceda
-  esmf >= 7.0.0b57-1.ceda
-  esmf-doc >= 7.0.0b57-1.ceda
-  esmf-lotus >= 7.0.0b57-1.ceda
-  esmf-lotus-doc >= 7.0.0b57-1.ceda
-  esmf-lotus-python27 >= 7.0.0b57-1.ceda
-  esmf-python27 >= 7.0.0b57-1.ceda
-  gdal >= 2.0.0-5.ceda
-  gdal-devel >= 2.0.0-5.ceda
-  gdal-doc >= 2.0.0-5.ceda
-  gdal-java >= 2.0.0-5.ceda
-  gdal-javadoc >= 2.0.0-5.ceda
-  gdal-libs >= 2.0.0-5.ceda
-  gdal-perl >= 2.0.0-5.ceda
-  gdal-python27 >= 2.0.0-5.ceda
-  geos >= 3.5.0-2.ceda
-  geos-devel >= 3.5.0-2.ceda
-  grass = 6.4.4-3.ceda
-  grass-devel = 6.4.4-3.ceda
-  grass-libs = 6.4.4-3.ceda
-  grib_api = 1.12.1-2.ceda
-  grib_api-devel = 1.12.1-2.ceda
-  grib_api-fortran = 1.12.1-2.ceda
-  grib_api-python27 = 1.12.1-2.ceda
-  hdf5 >= 1.8.12-2.ceda
-  hdf5-devel >= 1.8.12-2.ceda
-  hdfeos5 >= 1.15-1.ceda
-  libcdms >= 6.0rc2-6.ceda
-  libdrs >= 20130102-3.ceda
-  nccmp >= 1.7.5.1-2.ceda
-  ncl >= 6.3.0-2.ceda
-  nco >= 4.5.5-1.ceda
-  nco-devel >= 4.5.5-1.ceda
-  ncview >= 2.1.7-1.ceda
-  netcdf >= 4.4.0-1.ceda
-  netcdf-c++ >= 4.2-4.ceda
-  netcdf-c++-devel >= 4.2-4.ceda
-  netcdf-devel >= 4.4.0-1.ceda
-  netcdf-fortran >= 4.4.3-2.ceda
-  netcdf-fortran-devel >= 4.4.3-2.ceda
-  octave >= 4.0.0-2.ceda
-  octave-devel >= 4.0.0-2.ceda
-  octave-doc >= 4.0.0-2.ceda
-  octave-netcdf >= 1.0.7-2.ceda
-  octave-octcdf >= 1.1.8-3.ceda
-  python27-cdat_lite >= 6.0rc2-6.ceda
-  python27-cf >= 1.1.5-1.ceda
-  python27-cf-checker >= 2.0.9-1.ceda
-  python27-cfplot >= 1.9.10-1.ceda
-  python27-cf_units >= 1.0.0-1.ceda
-  python27-cfview >= 0.6.10-1.ceda
-  python27-cis >= 1.3.4-1.ceda
-  python27-cmor >= 2.9.2-3.ceda
-  python27-Cython >= 0.24-1.ceda
-  python27-iris >= 1.9.2-1.ceda
-  python27-nappy >= 1.1.2-2.ceda
-  python27-netCDF4 >= 1.0.7-4.ceda
-  python27-numpy >= 1.11.0-1.ceda
-  python27-pygeode >= 1.0.4a-1.ceda
-  python27-pygrib >= 2.0.1-1.ceda
-  python27-ScientificPython >= 2.9.4-2.ceda
-  python27-scipy >= 0.17.0-1.ceda
-  R-ncdf >= 1.6.8-2.ceda
-  udunits >= 2.1.24-3.ceda
-  udunits-devel >= 2.1.24-3.ceda
-  umutil >= 20130102-2.ceda
-  umutil-lib >= 20130102-2.ceda
-  xconv >= 1.93-1.ceda

and also 
- gtk2-devel
- p7zip
- wxGTK-devel
- xorg-x11-util-macros

- and GraphicsMagick-c++ version

- and removing cmor-devel (obsoleted by cmor-libs)
- and removing python27-jasmin_cis (obsoleted by python27-cis)

* Fri Aug 28 2015  <builderdev@builder.jc.rl.ac.uk> - 1.1-26.ceda
- octave >= 4.0.0-1.ceda
- octave-devel >= 4.0.0-1.ceda
- octave-doc >= 4.0.0-1.ceda
- octave-octcdf >= 1.1.8-1.ceda
- grass >= 6.4.4-1.ceda
- grass-libs >= 6.4.4-1.ceda
- grass-devel >= 6.4.4-1.ceda
- python27-cf >= 1.0.3-1.ceda
- python27-cartopy >= 0.11.2-1.ceda
- python27-matplotlib >= 1.4.3-1.ceda
- python27-setuptools >= 18.2-1.ceda
- python27-biggus >= 0.11.0-1.ceda
- R-ncdf >= 1.6.8-1.ceda
- cdo >= 1.6.9-1.ceda
- hdfeos2 >= 19.1.00-1.ceda
- perl-Image-ExifTool >= 9.98-1.ceda
- python27-jasmin_cis >= 1.0.0-1.ceda
- python27-iris >= 1.8.1-1.ceda
- python27-cf-checker >= 2.0.6-1.ceda
- gdal-devel >= 2.0.0-1.ceda
- gdal >= 2.0.0-1.ceda
- gdal-python27 >= 2.0.0-1.ceda
- gdal-perl >= 2.0.0-1.ceda
- gdal-libs >= 2.0.0-1.ceda
- gdal-java >= 2.0.0-1.ceda
- gdal-javadoc >= 2.0.0-1.ceda
- gdal-doc >= 2.0.0-1.ceda
- geos >= 3.5.0-1.ceda
- geos-devel >= 3.5.0-1.ceda
- llvm-devel >= 3.4.2-4
- valgrind >= 3.8.1-8
- jasper-devel >= 1.900.1-16
- diffuse >= 0.4.3-1
- tmux >= 1.6-3
- pdftk >= 2.02-1

* Tue Jan 27 2015  <builderdev@builder.jc.rl.ac.uk> - 1.1-25.ceda
- perl-XML-Parser >= 2.37
- dvipng >= 1.11
- glibc-static >= 2.12
  # - jasper-devel >= 1.900 - intended but problems so excluded for now
- mtk >= 1.4.3-1.ceda
- mtk-python27 >= 1.4.3-1.ceda
- mtk-devel >= 1.4.3-1.ceda
- ferret >= 6.93-1.ceda
- ncl >= 6.1.2-2.ceda
- python27-iris >= 1.7.3-1.ceda

* Sat Nov 22 2014  <builderdev@builder.jc.rl.ac.uk> - 1.1-24.ceda
-  lxterminal-0.1.9-1.ceda
-  python27-cf-0.9.8.3-1.ceda
-  python27-iris-1.7.2-1.ceda
-  python27-mpi4py-mpich-1.3-1.ceda in jasmin-sci-vm

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

