%define pname scikit-image
Summary: Image processing routines for SciPy
Name: python27-%{pname}
Version: 0.13.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Modified BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Stefan van der Walt <stefan@sun.ac.za>
Url: http://scikit-image.org
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

Image Processing SciKit

Image processing algorithms for SciPy, including IO, morphology, filtering,
warping, color manipulation, object detection, etc.

Please refer to the online documentation at
http://scikit-image.org/

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
# two files not listed in INSTALLED_FILES for some reason - list explicitly
/usr/lib/python2.7/site-packages/skimage/future/graph/tests/test_rag.pyc
/usr/lib/python2.7/site-packages/skimage/future/graph/tests/test_rag.pyo


%changelog

* Tue Jul  4 2017  <builderdev@builder.jc.rl.ac.uk> - 0.13.0-1.ceda
- initial version

