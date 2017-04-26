Summary: MISR Toolkit
Name: mtk
Version: 1.4.3
Release: 1.ceda%{dist}
License: MISR Toolkit License http://www.openchannelfoundation.org/project/print_license.php?group_id=354&license_id=31
Group: Scientific support
URL: https://eosweb.larc.nasa.gov/project/misr/tools/misr_toolkit
Source0: Mtk-src-%{version}.tar.gz
Patch0: mtk-1.4.3-ncinc.patch
Patch1: mtk-1.4.3-pythonexe.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libjpeg-turbo
Requires: zlib
Requires: hdf
Requires: hdfeos2
BuildRequires: hdfeos2 hdf-devel zlib-devel libjpeg-turbo-devel
Packager: alan.iwi@stfc.ac.uk

%description

The MISR Toolkit ( or "Mtk") is a simplified programming interface to access MISR Level 1B2, Level 2, and ancillary data products. It also handles the MISR conventional format. It consists of a collection of routines that can be used as command line tools or in the development of larger software tools and applications.

JUST RELEASED
MTK VERSION 1.4.3
Mtk is an interface built upon HDF-EOS that knows about MISR data products. It makes it very easy to extract and utilize MISR data sets. Reading a parameter requires the user to simply specify a file, grid, field, and a geographic region-of-interest; the concept of MISR "blocks" is handled internally, and data are presented to the user as a data plane (a flat array of values). Geo-location information is easily accessible for the data plane without the use of ancillary data sets. Any appropriate scaling factors or packed data sets are easily handled as well.

Features include:

    Specifying regions to read based on geographic bounding box, geographic location and extent, or the MISR path and block range

    Mapping between path, orbit, block, time range and geographic location

    Automatically stitching, unpacking and unscaling MISR data

    Perform coordinate conversions between lat/lon, SOM x/y, block/line/sample and line/sample of a data plane, which means geo-location can be computed instantly without referring to an ancillary data set lookup

    Retrieve pixel acquistion time from L1B2 product files

    Read a slice of a multi-dimensional field into an 2-D data plane (eg. RetrAppMask[0][5])

    Convert MISR product files to IDL ENVI files


%package devel
Group: Development/Libraries	
Summary: Development libraries for Mtk.
Requires: hdfeos2, hdf-devel, zlib-devel, libjpeg-turbo-devel
Requires: mtk = %{version}
%description devel
This package contains the development libraries for the MISR toolkit.
For further information see the description for the mtk (non-devel) package.

%package python27
Group: Development/Libraries	
Summary: Python bindings for Mtk.
Requires: python27
Requires: mtk = %{version}
%description python27
This package contains the python2.7 bindings for the MISR toolkit.
For further information see the description for the mtk (non-devel) package.

%prep
%setup -n Mtk-src-%{version}
%patch0 -p0
%patch1 -p0

%build

%define installprefix $RPM_BUILD_ROOT/usr
%define docdir /usr/share/doc/mtk-%{version}
%define tmpdocdir $RPM_BUILD_ROOT%{docdir}

export HDFEOS_INC=/usr/include
export HDFEOS_LIB=/usr/lib64/
export HDFLIB=/usr/lib64/hdf/
export HDFINC=/usr/include/hdf/

make
make PYTHON=python2.7 python

%install

export MTK_INSTALLDIR=$RPM_BUILD_ROOT/usr

rm -rf $RPM_BUILD_ROOT
make install
perl -p -i -e "s,$RPM_BUILD_ROOT,," %{installprefix}/bin/Mtk_{c,python}_env.{sh,csh}
mkdir -p `dirname %{tmpdocdir}`
mv %{installprefix}/doc %{tmpdocdir}
mv %{installprefix}/examples %{tmpdocdir}/
mv %{installprefix}/lib %{installprefix}/lib64
mkdir %{installprefix}/lib
mv %{installprefix}/lib64/python %{installprefix}/lib/python2.7

pushd wrappers/python
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=../../PYTHON_INSTALLED_FILES
popd

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%exclude %{_bindir}/Mtk_python_env*
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%doc %{_datadir}/doc/*

%files devel
%{_includedir}/*
%{_libdir}/*.a

%files python27 -f PYTHON_INSTALLED_FILES 
/usr/lib/python2.7/MisrToolkit.so
%{_bindir}/Mtk_python_env*

%changelog
* Tue Jan 27 2015  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.
