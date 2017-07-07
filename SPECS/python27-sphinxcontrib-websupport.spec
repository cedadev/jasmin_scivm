%define pname sphinxcontrib-websupport
Summary: Sphinx API for Web Apps
Name: python27-%{pname}
Version: 1.0.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Georg Brandl <georg@python.org>
Url: http://sphinx-doc.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

sphinxcontrib-webuspport provides a Python API to easily integrate Sphinx
documentation into your Web application.

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
