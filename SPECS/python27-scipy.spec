%define pname scipy
%define packdir /usr/lib/python2.7/site-packages/scipy

Summary: SciPy: Scientific Library for Python
Name: python27-%{pname}
Version: 0.17.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: SciPy Developers <scipy-dev@scipy.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.scipy.org
Requires: python27
BuildRequires: python27
Requires: python27-numpy, swig
BuildRequires: python27-numpy, swig

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
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# INSTALLED_FILES is not picking up some .pyc and .pyo files in tests/
# so remove everything from site-packages/numpy from the list, and then add
# it (recursively) below
egrep -v "^%{packdir}/" INSTALLED_FILES > INSTALLED_FILES1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 0.17.1-1.ceda
- update to 0.17.0

%files -f INSTALLED_FILES1
%defattr(-,root,root)
%{packdir}
