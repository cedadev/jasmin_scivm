Summary: An Analysis Tool for Gridded and Non-Gridded Data
Name: ferret
Version: 6.93
Release: 1.ceda%{dist}
License: OSD - http://ferret.pmel.noaa.gov/Ferret/ferret-legal
Group: Scientific support
URL: http://www.ferret.noaa.gov/Ferret/
Source0: fer_dsets_6.93.tar.gz
Source1: fer_environment_6.93.tar.gz
Source2: fer_executables_6.93.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

Ferret is an interactive computer visualization and analysis
environment designed to meet the needs of oceanographers and
meteorologists analyzing large and complex gridded data sets.

%define fer_dir /usr/lib/ferret

%prep
rm -fr ferret
mkdir ferret
cd ferret
tar xfz %{SOURCE0}
tar xfz %{SOURCE1}
tar xfz %{SOURCE2}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{fer_dir}  $RPM_BUILD_ROOT%{_bindir}
cd ferret
pushd bin
cp ferret_paths_template.sh ferret_paths.sh
cp ferret_paths_template.csh ferret_paths.csh
perl -p -i -e 's,((setenv|export).*FER_(DIR|DSETS).*")(.*)("),\1%{fer_dir}\5,' ferret_paths.{sh,csh}
popd

mv * $RPM_BUILD_ROOT%{fer_dir}/
chmod -R a+rX $RPM_BUILD_ROOT%{fer_dir}
ln -s %{fer_dir}/bin/{ferret,ferret_paths.{sh,csh}} $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/ferret
%{_bindir}/ferret_paths.*
%{fer_dir}

%changelog
* Tue Jan 27 2015  <builderdev@builder.jc.rl.ac.uk> - bin-1
- Initial build.
