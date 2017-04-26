%define pname nc-time-axis
Summary: netcdftime support for matplotlib axis
Name: python27-%{pname}
Version: 1.0.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Laura Dreyer, Philip Elson
Url: https://github.com/scitools/nc-time-axis
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-matplotlib python27-netCDF4
BuildRequires: python27 python27-matplotlib python27-netCDF4
BuildArch: noarch

%description

netcdftime support for matplotlib axis

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
