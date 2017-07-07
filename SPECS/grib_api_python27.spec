# -*- Mode:rpm-spec -*-
Summary: The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.
%define rel 1.ceda%{?dist}

%define version 1.23.0
%define automake_version 1.13.4
%define pkgname grib_api
%define prefix /usr
%define _prefix /usr
%define _target_platform x86_64-unknown-linux-gnu
%define _target_cpu x86_64
%define _enable_python %(test -z "" && echo 1 || echo 0)
%define _enable_fortran %(test -z "" && echo 1 || echo 0)
%define _requires_openjpeg %(test -n "" && echo 1 || echo 0)
%define _requires_jasper %(test -n "-ljasper" && echo 1 || echo 0)

%define lt_release @LT_RELEASE@
%define lt_version @LT_CURRENT@.@LT_REVISION@.@LT_AGE@

%define __aclocal   aclocal || aclocal -I ./macros
%define configure_args  '--with-pic' '--enable-python' '--prefix=/usr'

Name: %{pkgname}
Version: %{version}
Release: %{rel}
Distribution: Red Hat Enterprise Linux Server release 6.4 (Santiago) 
Vendor: ECMWF
License: Apache Licence version 2.0 
Group: Scientific/Libraries
Source: %{pkgname}-%{version}-Source.tar.gz
Source1: automake-%{automake_version}.tar.gz
#Patch1: gribapi-python-requires.diff
Patch2: gribapi-python-site-packages-dir-aclocal.diff
# %if %{_requires_jasper}
# Requires: libjasper
# %endif
# %if %{_requires_openjpeg}
# Requires: openjpeg 
# %endif
Buildroot: /tmp/%{pkgname}-root
URL: http://www.ecmwf.int
Prefix: %{prefix}
BuildArchitectures: %{_target_cpu}
Packager: alan.iwi@stfc.ac.uk - forked from ECMWF RPM

%description 
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.

%prep
%setup -n %{pkgname}-%{version}-Source
#%patch1 -p1
%patch2 -p1 -F2
autoconf
tar xvfz %{SOURCE1}

%build
export PYTHON=/usr/bin/python2.7
%configure %{?configure_args}
# This is why we copy the CFLAGS to the CXXFLAGS in configure.in
# CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure %{_target_platform} --prefix=%{prefix}

am_dir=`pwd`/automake
mkdir $am_dir
pushd automake-%{automake_version}
./configure --prefix=$am_dir
make
make install
popd
export PATH=$am_dir/bin:$PATH

make

%install
# To make things work with BUILDROOT
echo Cleaning RPM_BUILD_ROOT: "$RPM_BUILD_ROOT"
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
#
# rename files to avoid a conflict with new eccodes package
# 
pushd $RPM_BUILD_ROOT/usr/bin
for f in * ; do mv $f ${f}_from_legacy_grib_api ; done
popd
pushd $RPM_BUILD_ROOT/usr/include
mkdir legacy_grib_api
mv grib_api* legacy_grib_api/
popd
pushd $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages
rm __init__.py*
for i in gribapi.py*; do mv $i legacy_$i; done
popd

%clean


%files
%defattr(-, root, root)
#%doc COPYRIGHT ChangeLog README AUTHORS NEWS
#%doc doc/*
%prefix/bin/*
%prefix/lib*/libgrib_api.so
%prefix/lib*/libgrib_api.so.*
%prefix/share/grib_api/definitions/*

# If you install a library
%post 
/sbin/ldconfig || exit 1
exit 0

# If you install a library
%postun 
/sbin/ldconfig
exit 0

%package devel
Summary: Development files for %{pkgname}
Group: Scientific/Libraries
Requires: grib_api = %{version}
%description devel
Development files for %{pkgname}.
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.
%files devel
%defattr(-, root, root)
#%doc doc
%prefix/include/legacy_grib_api/grib_api.h
%prefix/include/legacy_grib_api/grib_api_windef.h
%prefix/include/legacy_grib_api/grib_api_version.h
%prefix/lib*/libgrib_api.a
%prefix/lib*/libgrib_api.la
%prefix/lib*/pkgconfig/*
%prefix/share/grib_api/samples/*
%prefix/share/grib_api/ifs_samples/*

# Only generate package if python is enabled
%if %{_enable_python}
# The name of the package providing python (variable '_python_package'
# below) will be used both for dependencies and also for the suffix
# part of the package name for the grib_api python bindings.  For example,
# it might be just "python" for the system python, or "python27" for a
# package providing a coexisting alternative version.
%define _python_command %(test -z "@PYTHON" && echo python || echo "/usr/bin/python2.7")
%define _python_exe %(which %{_python_command})
%define _python_package %(rpm -qf %{_python_exe} --queryformat="%{NAME}")
%package %{_python_package}
Summary: Python interface for %{pkgname}
Group: Scientific/Libraries
Requires: grib_api = %{version} %{_python_package}
%description %{_python_package}
Python interface for %{pkgname}.
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.
%files %{_python_package}
%defattr(-, root, root)
%prefix/lib*/python*/*
%endif

# Only generate package if fortran is enabled
%if %{_enable_fortran}
%package fortran
Summary: Fortran 90 interface for %{pkgname}
Group: Scientific/Libraries
Requires: grib_api = %{version}
%description fortran
Fortran 77 and 90 interface for %{pkgname}.
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1
and edition 2 messages.
%files fortran
%defattr(-, root,root)
%prefix/include/legacy_grib_api/*.mod
%prefix/include/legacy_grib_api/*f77*
%prefix/lib*/*f90*
%prefix/lib*/*f77*
%endif

%changelog
* Mon Jul  3 2017  <builderdev@builder.jc.rl.ac.uk> - 1.23.0-2.ceda%{?dist}
- update to 1.23.0
- rename all executables and include files to avoid conflicts with 
    versions from new eccodes package

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 1.17.0-1.ceda%{?dist}
- update to 1.17.0
- automake now bundled in source

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.12.1-2.ceda
- make -devel depend on exact version of base package

* Thu Mar 15 2012 - Get the changelog from JIRA
- Multiple bugfixes

* Mon May 26 2005 - Get the changelog from JIRA
- Added kmymoney-ofx package

