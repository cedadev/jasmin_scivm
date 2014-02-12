%define version 100726.00.0
%define versiontag v%(echo %{version} | tr . -)
%define tandcs %{_datadir}/bbcp/legal

Summary: A multi-streaming network transfer utility
Name: bbcp
Version: %{version}
Release: 1.ceda
License: http://www.slac.stanford.edu/~abh/bbcp/#_Toc332986085
Group: Applications/Internet
URL: http://www.slac.stanford.edu/~abh/bbcp/
Source0: %{name}-%{versiontag}.tar.gz
Source1: bbcp-legal
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

A point-to-point multi-streaming network transfer utility intended for
fast and secure transfer of large files.

%prep
%setup -n %{name}

%build
cd src
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/bbcp
install -m 755 bin/*/bbcp $RPM_BUILD_ROOT/%{_bindir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{tandcs}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/bbcp
%doc %{tandcs}


%changelog
* Wed Oct 16 2013  Alan Iwi - 
- Initial build.

