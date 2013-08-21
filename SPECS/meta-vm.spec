Summary: Meta-RPMs for JASMIN science VM and for Lotus VM
Name: jasmin-meta-vm
Version: 1.1
Release: 2.ceda
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
Requires: arpack >= 3.0.1
Requires: atlas >= 3.8.4
Requires: atlas-devel >= 3.8.4
Requires: blas >= 3.2.1
Requires: cdo >= 1.5.6.1
Requires: cmor-devel >= 2.8.2
Requires: ddd >= 3.3.12
Requires: emacs >= 23.1
Requires: emacs-gnuplot >= 4.2.6
Requires: fftw >= 3.2.1
Requires: fftw-devel >= 3.2.1
Requires: firefox >= 17.0.3
Requires: gcc-gfortran >= 4.4.7
Requires: gdal >= 1.9.2
Requires: gdal-devel >= 1.9.2
Requires: gdal-doc >= 1.9.2
Requires: gdal-java >= 1.9.2
Requires: gdal-javadoc >= 1.9.2
Requires: gdal-perl >= 1.9.2
Requires: gdal-python27 >= 1.9.2
Requires: gdal-ruby >= 1.9.2
Requires: geany >= 0.21
Requires: gedit >= 2.28.4
Requires: geos >= 3.3.6
Requires: geos-devel >= 3.3.6
Requires: git >= 1.7.1
Requires: gnuplot >= 4.2.6
Requires: grib_api >= 1.10.0
Requires: grib_api-devel >= 1.10.0
Requires: grib_api-fortran >= 1.10.0
Requires: grib_api-python27 >= 1.10.0
Requires: gv >= 3.7.1
Requires: hdf >= 4.2.9
Requires: hdf5 >= 1.8.9
Requires: hdf5-devel >= 1.8.9
Requires: hdf-devel >= 4.2.9
Requires: ImageMagick >= 6.5.4.7
Requires: ksh >= 20100621
Requires: libuuid >= 2.17.2
Requires: libuuid >= 2.17.2
Requires: ncBrowse >= 1.6.5
Requires: nco >= 4.3.4
Requires: nco-devel >= 4.3.4
Requires: ncview >= 2.1.2
Requires: nedit >= 5.5
Requires: netcdf >= 4.2.1
Requires: netcdf-c++ >= 4.2
Requires: netcdf-c++-devel >= 4.2
Requires: netcdf-devel >= 4.2.1
Requires: netcdf-fortran >= 4.2
Requires: netcdf-fortran-devel >= 4.2
Requires: octave >= 3.6.4
Requires: octave-devel >= 3.6.4
Requires: octave-doc >= 3.6.4
Requires: octave-octcdf >= 1.1.5
Requires: perl-devel >= 5.10.1
Requires: python27 >= 2.7.3
Requires: python27-basemap >= 1.0.5
Requires: python27-cartopy >= 0.7.0
Requires: python27-cdat_lite >= 6.0rc2
Requires: python27-cf >= 0.9.7.1
Requires: python27-cmor >= 2.8.2
Requires: python27-Cython >= 0.17.3
Requires: python27-ipython >= 0.14_dev_ceda.1
Requires: python27-iris >= 1.3.0
Requires: python27-jasmin_cis >= 0.6
Requires: python27-Jug >= 0.9.3
Requires: python27-matplotlib >= 1.2.0
Requires: python27-netCDF4 >= 1.0
Requires: python27-nose >= 1.2.0
Requires: python27-numpy >= 1.7.0
Requires: python27-Pydap >= 3.1.RC1
Requires: python27-Pygments >= 1.5
Requires: python27-pyhdf >= 0.8_1
Requires: python27-pyke >= 1.1.1
Requires: python27-pyzmq >= 2.2.0.1
Requires: python27-rpy2 >= 2.2.6
Requires: python27-scipy >= 0.12.0
Requires: python27-setuptools >= 0.6c12dev_r88846
Requires: python27-shapefile >= 1.1.4
Requires: python27-Shapely >= 1.2.16
Requires: python27-tornado >= 2.4
Requires: python27-virtualenv >= 1.8.2
Requires: R >= 2.10.0
Requires: R-devel >= 2.10.0
Requires: subversion >= 1.6.11
Requires: tcl >= 8.5.7
Requires: tcl-devel >= 8.5.7
Requires: tcsh >= 6.17
Requires: tk >= 8.5.7
Requires: tk-devel >= 8.5.7
Requires: tkdiff >= 4.2
Requires: udunits >= 2.1.24
Requires: udunits-devel >= 2.1.24
Requires: umutil >= 20130102
Requires: uuid >= 1.6.1
Requires: uuid-devel >= 1.6.1
Requires: vim-enhanced >= 7.2.411
Requires: xconv >= 1.91
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
