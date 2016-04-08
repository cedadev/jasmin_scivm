Summary: NCAR Command Language
Name: ncl
Version: 6.3.0
Release: 2.ceda%{dist}
License: UCAR
Group: Scientific support
URL: http://www.ncl.ucar.edu/
Source0: ncl_ncarg-6.3.0.Linux_RHEL6.4_x86_64_gcc472.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: UCAR
Summary: NCAR Command Language
Requires: esmf

%define root /usr
%define profile_csh /etc/profile.d/ncl.csh
%define profile_sh /etc/profile.d/ncl.sh

%description

The NCAR Command Language (NCL) is a free interpreted language designed specifically for scientific data processing and visualization.

%prep
rm -fr ncl
mkdir ncl
cd ncl
tar xvfz %{SOURCE0}
#patch -p0 < %{PATCH0}

%build

%install
[ $RPM_BUILD_ROOT != / ] && rm -fr $RPM_BUILD_ROOT

install_root=$RPM_BUILD_ROOT/%{root}

mkdir -p $install_root

cd ncl
cp -r bin lib include $install_root/
rm $install_root/bin/ESMF_RegridWeightGen

mkdir -p $RPM_BUILD_ROOT/`dirname %{profile_sh}`
echo "setenv NCARG_ROOT %{root}" > $RPM_BUILD_ROOT/%{profile_csh}
echo "NCARG_ROOT=%{root} ; export NCARG_ROOT" > $RPM_BUILD_ROOT/%{profile_sh}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Dec 6 2015 <alan.iwi@stfc.ac.uk> - 6.3.0-2.ceda%{dist}
- remove ESMF_RegridWeightGen and add esmf package dependency,
  per https://github.com/cedadev/jasmin_scivm/issues/40

* Sat Nov  7 2015  <builderdev@builder.jc.rl.ac.uk> - 6.1.2-2.ceda%{dist}
- upgrade, still wrapping binaries
- ncl-shea_util.patch no longer needed

* Fri Feb 21 2014  <builderdev@builder.jc.rl.ac.uk> - 6.1.2-1.ceda%{dist}
- wrap binary release

%files
%{root}/bin/*
%{root}/lib/*
%{root}/include/*
%{profile_sh}
%{profile_csh}
