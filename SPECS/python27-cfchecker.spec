%define pname cf-checker

Summary: The NetCDF Climate Forcast Conventions compliance checker
Name: python27-%{pname}
Version: 2.0.6
Release: 1.ceda%{?dist}
Source0: https://github.com/cedadev/cf-checker/archive/8f7d4e16af05222d8eaf3436cd8292c1c5ce0b93.zip
License: UNKNOWN
Group: Scientific support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rosalyn Hatcher <r.s.hatcher@reading.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: https://github.com/cedadev/cf-checker/wiki
Requires: python27 python27-cdat_lite udunits >= 2.1
BuildRequires: python27

%define spooldir /var/spool/cf-checker

%description

The NetCDF Climate Forcast Conventions compliance checker

%prep
%setup -n cf-checker-8f7d4e16af05222d8eaf3436cd8292c1c5ce0b93/

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT%{spooldir}
chmod 777 $RPM_BUILD_ROOT%{spooldir}
install -m 755 src/cf-checker $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_bindir}/cf-checker
%{spooldir}

%changelog
* Thu Sep 11 2014  <builderdev@builder.jc.rl.ac.uk> - 2.0.5-4.ceda
- move to git release cd671f

* Tue Jan 14 2014  <builderdev@builder.jc.rl.ac.uk> - 2.0.5-2.ceda
- nove to git release 9cb6a90

* Tue Dec 17 2013  <builderdev@builder.jc.rl.ac.uk> - 2.0.5-2.ceda
- move to git release 8da3237 and add cf-checker /var/spool/cf-checker

* Thu Nov 14 2013  <builderdev@builder.jc.rl.ac.uk> - 2.0.5-1.ceda
- initial build
