%define pname numpy
%define packdir /usr/lib/python2.7/site-packages/numpy


Summary: NumPy: array processing for numbers, strings, records, and objects.
Name: python27-%{pname}
Version: 1.14.5
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.zip
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: NumPy Developers <numpy-discussion@scipy.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://numpy.scipy.org
Requires: python27 python27-Cython swig
BuildRequires: python27 python27-Cython swig

# conflict because we create /usr/bin/f2py symlink below
Conflicts: python-numpy  

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
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# INSTALLED_FILES is not picking up some .pyc and .pyo files in tests/
# so remove everything from site-packages/numpy from the list, and then add
# it (recursively) below
egrep -v "^%{packdir}/" INSTALLED_FILES > INSTALLED_FILES1
pushd $RPM_BUILD_ROOT/%{_bindir}
ln -s f2py2.7 f2py
popd

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 17 2018  <builderdev@builder.jc.rl.ac.uk> - 1.14.5-1.ceda
- bump version

* Wed Jul  5 2017  <builderdev@builder.jc.rl.ac.uk> - 1.13.0-1.ceda
- update to 1.13.0
- add a conflicts with python27-numpy, and add a symlink /usr/bin/f2py

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.11.0-1.ceda
- update to 1.11.0


* Tue Nov  3 2015  <builderdev@builder.jc.rl.ac.uk> - 1.10.1-1.ceda
- upgrade to 1.10.1

%files -f INSTALLED_FILES1
%{_bindir}/f2py
%defattr(-,root,root)
%{packdir}
