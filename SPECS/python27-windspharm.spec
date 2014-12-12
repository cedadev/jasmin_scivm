%define pname windspharm
Summary: vector wind analysis in spherical coordinates
Name: python27-%{pname}
Version: 1.3.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andrew Dawson <dawson@atm.ox.ac.uk>
Url: http://ajdawson.github.com/windspharm/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-pyspharm
BuildRequires: python27
BuildArch: noarch

%description

      windspharm provides a simple interface for doing calculations on
      vector wind fields (e.g., computing streamfunction) in spherical
      geometry using spherical harmonics

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
