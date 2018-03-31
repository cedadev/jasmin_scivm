%define install_dir /usr/share/cmip6-cmor-tables/
Name:  cmip6-cmor-tables
Version: 6.1.23
Release: 1.ceda%{?dist}
Summary: CMIP6 tables for CMOR
Group: Scientific support
License: unknown
Source0: %{name}-%{version}.tar.gz
Packager: alan.iwi@stfc.ac.uk
Buildarch: noarch

%description

CMIP6 tables for use with CMOR and PrePARE.

This provides the tables under /usr/share/cmip6-cmor-tables.

The Tables directory may need to be symbolically linked into the current
directory so that CMOR can find them.

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{install_dir}
cp -pr Tables $RPM_BUILD_ROOT/%{install_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{install_dir}/Tables

%changelog
* Sat Mar 31 2018  <builderdev@builder.jc.rl.ac.uk> - 0.1-1.ceda
- initial version

