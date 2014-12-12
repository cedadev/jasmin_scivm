%define pname @NAME@
Summary: @SUMMARY@
Name: python27-%{pname}
Version: @VERSION@
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: @LICENCE@
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: @VENDOR@
Url: @URL@
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: @BUILDARCH@

%description

@DESCRIPTION@

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
