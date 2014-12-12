%define pname pyspharm
%define spherepack_version 3.2
Summary: Python Spherical Harmonic Transform Module
Name: python27-%{pname}
Version: 1.0.8
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
Source1: spherepack3.2.tar
Source2: pyspharm-and-spherepack-COPYING
License: MIT and SPHEREPACK licenses
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Url: http://code.google.com/p/pyspharm
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 gcc-gfortran
BuildRequires: python27 gcc-gfortran

%description

Provides an object-oriented python interface to the NCAR SPHEREPACK
library. Can perform spherical harmonic transforms to and from
regularly spaced and gaussian lat/lon grids.

%prep
%setup -n %{pname}-%{version}
tar xvf %{SOURCE1}
cd src
ln -s ../spherepack%{spherepack_version}/src/*.f ./

%build
python2.7 setup.py build

%install
%define docdir %{_datadir}/%{pname}
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT/%{docdir}
cp %{SOURCE2} $RPM_BUILD_ROOT/%{docdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc %{docdir}/pyspharm-and-spherepack-COPYING
