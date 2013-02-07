%define pname scipy
%define packdir %{_libdir}/python2.6/site-packages/scipy

Summary: SciPy: Scientific Library for Python
Name: python-%{pname}
Version: 0.11.0rc2
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: SciPy Developers <scipy-dev@scipy.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.scipy.org
Requires: python-numpy
BuildRequires: python-numpy

%description
SciPy (pronounced "Sigh Pie") is open-source software for mathematics,
science, and engineering. The SciPy library
depends on NumPy, which provides convenient and fast N-dimensional
array manipulation. The SciPy library is built to work with NumPy
arrays, and provides many user-friendly and efficient numerical
routines such as routines for numerical integration and optimization.
Together, they run on all popular operating systems, are quick to
install, and are free of charge.  NumPy and SciPy are easy to use,
but powerful enough to be depended upon by some of the world's
leading scientists and engineers. If you need to manipulate
numbers on a computer and display or publish the results,
give SciPy a try!



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
