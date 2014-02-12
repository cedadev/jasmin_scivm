%define pname netCDF4-python
%define netcdf_min_version 4.3.1
Summary: Provides an object-oriented python interface to the netCDF version 4 library.
Name: python27-netCDF4
Version: 1.0.7
Release: 2.ceda%{?dist}
Source0: netCDF4-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html
Requires: python27 python27-numpy
BuildRequires: python27 python27-numpy
Requires: netcdf >= %{netcdf_min_version}
BuildRequires: netcdf-devel >= %{netcdf_min_version}

%description
netCDF version 4 has many features not found in earlier versions of the library, such as hierarchical groups, zlib compression, multiple unlimited dimensions, and new data types.  It is implemented on top of HDF5.  This module implements most of the new features, and can read and write netCDF files compatible with older versions of the library.  The API is modelled after Scientific.IO.NetCDF, and should be familiar to users of that module.

This project has a `Subversion repository <http://code.google.com/p/netcdf4-python/source>`_ where you may access the most up-to-date source.

%prep
%setup -n netCDF4-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# for i in nc3tonc4 nc4tonc3
# do
#   path=%{_bindir}/$i
#   tmppath=$RPM_BUILD_ROOT$path
#   mv $tmppath ${tmppath}_py27
#   perl -p -i -e "s,$path,${path}_py27," INSTALLED_FILES
# done

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Feb  6 2014  <builderdev@builder.jc.rl.ac.uk> - 1.0.7-2.ceda
- comment out renaming of executables

* Thu Jan 23 2014  <builderdev@builder.jc.rl.ac.uk> - 1.0.7-1.ceda
- update to v1.0.7 (built after updating netCDF on system to 4.3.1)

%files -f INSTALLED_FILES
%defattr(-,root,root)
