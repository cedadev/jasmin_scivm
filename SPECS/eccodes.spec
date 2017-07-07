%define vers 2.4.0
%define source_dir eccodes-%{vers}-Source
%define build_dir eccodes-build
%define python /usr/bin/python2.7
%define python_pack python27

Name:    eccodes
Version: %{vers}
Release: 1.ceda%{?dist}
Summary: API and tools for encoding/decoding WMO GRIB, BUFR and GTS
Group:	 Scientific support
License: http://www.apache.org/licenses/LICENSE-2.0	
URL:     https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home
Source0: %{source_dir}.tar.gz
Packager: alan.iwi@stfc.ac.uk
BuildRequires: cmake gcc-gfortran %{python_pack}
Conflicts: grib_api <= 1.17.0-1.ceda.el6.x86_64
# uncomment for optional packages support
BuildRequires: jasper-devel libpng-devel zlib-devel hdf5-devel netcdf-devel openjpeg2-devel %{python_pack}-numpy git
Requires: jasper-libs libpng zlib hdf5 netcdf openjpeg2

%description

A useful set of command line tools provide quick access to the messages. C, Fortran 90 and Python interfaces provide access to the main ecCodes functionality.
ecCodes is an evolution of GRIB-API.  It is designed to provide the user with a simple set of functions to access data from several formats with a key/value approach.
For GRIB encoding and decoding, the GRIB-API functionality is provided fully in ecCodes with only minor interface and behaviour changes. Interfaces for C, Fortran 90 and Python are all maintained as in GRIB-API.  However, the GRIB-API Fortran 77 interface is no longer available.
In addition, a new set of functions with the prefix "codes_" is provided to operate on all the supported message formats. These functions have the same interface and behaviour as the "grib_" functions. 
A selection of GRIB-API tools has been included in ecCodes (ecCodes GRIB tools), while new tools are available for the BUFR (ecCodes BUFR tools) and GTS formats. The new tools have been developed to be as similar as possible to the existing GRIB-API tools maintaining, where possible, the same options and behaviour. A significant difference compared with GRIB-API tools is that bufr_dump produces output in JSON format suitable for many web based applications.

%package devel
Summary: Development package for eccodes
Requires: eccodes = %{version}
Requires: glibc-devel cmake

%description devel
This is the development package for eccodes, including the header files and sample files.

%package fortran
Summary: Fortran bindings for eccodes
Requires: eccodes = %{version}
Requires: gcc-gfortran 

%description fortran
This package contains the Fortran eccodes_f90 library

%package %{python_pack}
Summary: %{python_pack} bindings for eccodes
Requires: eccodes = %{version}
Requires: %{python_pack}
# optional
Requires: %{python_pack}-numpy

%description %{python_pack}
This package contains the %{python_pack} eccodes and gribapi modules

%prep
rm -fr %{build_dir} eccodes-%{vers}-Source
tar xvfz %{SOURCE0}

#
# remove code which overrides python libdir, so that python installs into its 
# usual site packages directory even though we specify INSTALL_LIB_DIR option
#
perl -p -i -e 's/\$\{__install_lib\}//g' %{source_dir}/python/CMakeLists.txt

mkdir %{build_dir}  # outside source tree

%build
cd %{build_dir}
cmake \
       -DCMAKE_INSTALL_PREFIX=/usr -DENABLE_NETCDF=ON -DENABLE_JPG=ON -DENABLE_PNG=ON \
       -DENABLE_PYTHON=ON ENABLE_FORTRAN=ON -DPYTHON_EXECUTABLE=%{python} \
       -DINSTALL_LIB_DIR=%(basename %{_libdir}) \
       -DBUILD_SHARED_LIBS=BOTH \
       ../%{source_dir}

%install
cd %{build_dir}
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install

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
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/libeccodes.so
%{_datadir}/eccodes/definitions

%files fortran
%{_includedir}/*.mod
%{_libdir}/libeccodes_f90.a
%{_libdir}/libeccodes_f90.so
%{_libdir}/pkgconfig/eccodes_f90.pc

%files devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/eccodes.pc
%{_libdir}/libeccodes.a
%{_datadir}/eccodes/cmake
%{_datadir}/eccodes/ifs_samples
%{_datadir}/eccodes/samples

%define site_packages_dir %(%python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%files %{python_pack}
%{site_packages_dir}/eccodes*
%{site_packages_dir}/gribapi


%changelog

* Mon Jul  3 2017  <builderdev@builder.jc.rl.ac.uk> - 2.4.0-1
- initial package

