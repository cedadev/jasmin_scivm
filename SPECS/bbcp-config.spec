Summary: configures bbcp to use IPv4 by default
Name: bbcp-config
Version: 1
Release: 1.ceda
License: CEDA
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: bbcp >= 140414.00.1

%description

configures bbcp so that IPv4 is the default

For use on JASMIN, which doesn't support IPv6

%prep
#%setup -q

%build

%install

%define configfile %{_datadir}/bbcp/config

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/profile.d/
echo "export bbcp_CONFIGFN=%{configfile}" > $RPM_BUILD_ROOT/etc/profile.d/bbcp.sh
echo "setenv bbcp_CONFIGFN %{configfile}" > $RPM_BUILD_ROOT/etc/profile.d/bbcp.csh
mkdir -p `dirname $RPM_BUILD_ROOT/%{configfile}`
echo "-4" > $RPM_BUILD_ROOT/%{configfile}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config %{configfile}
%config /etc/profile.d/bbcp.sh
%config /etc/profile.d/bbcp.csh

%changelog
* Wed Sep 10 2014  <builderdev@builder.jc.rl.ac.uk> - config-1
- Initial build.

