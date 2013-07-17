Summary: Adds configuration to make the system into a JASMIN science VM
Name: jasmin-sci-vm
Version: 1.0
Release: 6.ceda
Group: Utilities/Configuration
License: Copyright STFC
BuildRoot: %{_builddir}/%{name}-root
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
BuildArch: noarch
Requires: arpack atlas atlas-devel blas cdo cmor-devel emacs emacs-gnuplot fftw fftw-devel firefox gcc-gfortran geany gedit geos geos-devel git gnuplot gv hdf5 hdf5-devel ImageMagick ksh libuuid ncBrowse nco nco-devel ncview netcdf netcdf-devel netcdf-fortran netcdf-fortran-devel netcdf-c++ netcdf-c++-devel octave octave-devel octave-doc octave-octcdf perl-devel python27 python27-Cython python27-Pydap python27-Pygments python27-Shapely python27-basemap python27-cartopy python27-cdat_lite python27-cf python27-cmor python27-ipython python27-iris python27-matplotlib python27-netCDF4 python27-nose python27-numpy python27-pyke python27-pyzmq python27-rpy2 python27-scipy python27-setuptools python27-shapefile python27-tornado python27-virtualenv R R-devel subversion tcl tcl-devel tcsh tk tk-devel tkdiff udunits udunits-devel uuid uuid-devel vim-enhanced xconv xemacs xpdf nedit ddd hdf hdf-devel python27-pyhdf python27-jasmin_cis python27-Jug
Requires: gdal gdal-doc gdal-java gdal-javadoc gdal-devel gdal-python27 gdal-perl gdal-ruby
Requires: umutil
Requires: grib_api grib_api-devel grib_api-fortran grib_api-python27
### mpich2 interfering with Lotus - these packages now removed:
### Requires: python27-mpi4py-mpich2 mpich2

%description
Adds configuration to make the system into a JASMIN science VM

%prep
%build
%clean
%install
%files

%changelog
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
