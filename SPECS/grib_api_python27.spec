# -*- Mode:rpm-spec -*-
Summary: The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.
%define rel 1

%define version 1.10.0
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
Distribution: Red Hat Enterprise Linux Server release 6.3 (Santiago) 

Vendor: ECMWF
License: LGPL
Group: Scientific/Libraries
Source: %{pkgname}-%{version}.tar.gz
Patch1: gribapi-python-init.diff
Patch2: gribapi-python-requires.diff
Patch3: gribapi-python-site-packages-dir.diff
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
Packager: Software Services <software.support@ecmwf.int>

%description 
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.

%changelog
* Mon May 26 2005 - Get the changelog from JIRA
- Added kmymoney-ofx package

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1 -F2
automake

%build
export PYTHON=/usr/bin/python2.7
%GNUconfigure %{?configure_args}
# This is why we copy the CFLAGS to the CXXFLAGS in configure.in
# CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure %{_target_platform} --prefix=%{prefix}
make

%install
# To make things work with BUILDROOT
echo Cleaning RPM_BUILD_ROOT: "$RPM_BUILD_ROOT"
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install

%clean


%files
%defattr(-, root, root)
#%doc COPYRIGHT ChangeLog README AUTHORS NEWS
#%doc doc/*
%prefix/bin/*
%prefix/lib*/libgrib_api.so
%prefix/lib*/libgrib_api-%{version}.so
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
Requires: grib_api
%description devel
Development files for %{pkgname}.
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1 and edition 2 messages.
%files devel
%defattr(-, root, root)
#%doc doc
%prefix/include/*
%prefix/lib*/*.a
%prefix/lib*/*.la
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
Requires: grib_api %{_python_package}
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
Requires: grib_api
%description fortran
Fortran 77 and 90 interface for %{pkgname}.
The ECMWF GRIB API is an application program interface accessible from C and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB edition 1
and edition 2 messages.
%files fortran
%defattr(-, root,root)
%prefix/lib*/*f90*
%prefix/lib*/*f77*
%endif

