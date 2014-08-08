Summary: NCAR Command Language
Name: ncl
Version: 6.1.2
Release: 1.ceda%{dist}
License: UCAR
Group: Scientific support
URL: http://www.ncl.ucar.edu/
Source0: ncl_ncarg-6.1.2.Linux_RHEL6.2_x86_64_gcc446.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: UCAR
Summary: NCAR Command Language

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

%build

%install
[ $RPM_BUILD_ROOT != / ] && rm -fr $RPM_BUILD_ROOT

install_root=$RPM_BUILD_ROOT/%{root}

mkdir -p $install_root

cd ncl
cp -r bin lib include $install_root/

mkdir -p $RPM_BUILD_ROOT/`dirname %{profile_sh}`
echo "setenv NCARG_ROOT %{root}" > $RPM_BUILD_ROOT/%{profile_csh}
echo "NCARG_ROOT=%{root} ; export NCARG_ROOT" > $RPM_BUILD_ROOT/%{profile_sh}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Feb 21 2014  <builderdev@builder.jc.rl.ac.uk> - 6.1.2-1.ceda%{dist}
- wrap binary release

%files
%{root}/bin/*
%{root}/lib/*
%{root}/include/*
%{profile_sh}
%{profile_csh}
