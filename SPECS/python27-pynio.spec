%define pname PyNIO
Summary: Multi-format data I/O package
Name: python27-%{pname}
Version: 1.5.0_beta20160623
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: https://github.com/NCAR/pynio/blob/master/LICENSE
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: David I. Brown <dbrown@ucar.edu>
Url: http://www.pyngl.ucar.edu/Nio.shtml
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27, python27-numpy, netcdf-devel, hdf5-devel, ncl
BuildRequires: python27, python27-numpy, netcdf, hdf5, ncl

%description

       Enables NetCDF-like access for NetCDF (rw), HDF (rw), HDF-EOS2 (r), HDF-EOS5, GRIB (r), and CCM (r) data files

%prep
%setup -n pynio

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
