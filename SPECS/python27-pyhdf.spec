%define pname pyhdf
%define version 0.8_1
%define unmangled_version 0.8-1

Summary: Python interface to the NCSA HDF4 library
Name: python27-%{pname}
Version: %{version}
Release: 2.ceda%{?dist}
Source0: %{pname}-%{unmangled_version}.tar.gz
Patch0: pyhdf.lib64.patch
Patch1: pyhdf.noszip.patch
Patch2: pyhdf.include.patch
License: public
Group: Development/Python
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Robert Kern <robert.kern@enthought.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.sourceforge.net/projects/pysclint
Requires: python27 hdf python27-numpy
BuildRequires: python27 hdf-devel python27-numpy

%description

The pyhdf package wraps the functionality
 of the NCSA HDF version 4 library inside a Python OOP
 framework. The SD (scientific dataset), VS
 (Vdata) and V (Vgroup) APIs are currently implemented.
 SD datasets are read/written
 through numpy arrays. netCDF files can also
 be read and modified with pyhdf.
The function parse_odl is also provided to
deal specifically with data in the ODL
(Object Desdription Language) format.

%prep
%setup -n %{pname}-%{unmangled_version}
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Mar  6 2013  <builderdev@builder.jc.rl.ac.uk> - 0.8_1-2.ceda
- add patch that fixes segfaults due to implicit declarations in the C
  code from not including hdf.h

* Fri Feb 15 2013  <builderdev@builder.jc.rl.ac.uk> - 0.8_1-1.ceda
- initial RPM

%files -f INSTALLED_FILES
%defattr(-,root,root)
