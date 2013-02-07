%define pname numpy
%define packdir %{_libdir}/python2.6/site-packages/numpy


Summary: NumPy: array processing for numbers, strings, records, and objects.
Name: python-%{pname}
Version: 1.6.2
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: NumPy Developers <numpy-discussion@scipy.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://numpy.scipy.org

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type which also makes NumPy suitable for
interfacing with general-purpose data-base applications.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation.


%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# INSTALLED_FILES is not picking up some .pyc and .pyo files in tests/
# so remove everything from site-packages/numpy from the list, and then add
# it (recursively) below
egrep -v "^%{packdir}/" INSTALLED_FILES > INSTALLED_FILES1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES1
%defattr(-,root,root)
%{packdir}
