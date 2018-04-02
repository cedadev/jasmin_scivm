%define pname dask
Summary: Parallel PyData with Task Scheduling
Name: python27-%{pname}
Version: 0.17.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Matthew Rocklin <mrocklin@gmail.com>
Url: http://github.com/dask/dask/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-cloudpickle python27-numpy python27-pandas python27-partd python27-toolz
BuildRequires: python27
BuildArch: noarch

%description

Dask
====

Dask is a flexible parallel computing library for analytics.  See
documentation for more information.

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
