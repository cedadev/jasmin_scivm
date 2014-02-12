Name: xconv
Version: 1.92dev
Release: 1.ceda%{?dist}
Source0: xconv1.92
License: NCAS
Group: Scientific support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: NCAS
Url: http://badc.nerc.ac.uk/help/software/xconv/
Summary: a tool for viewing and converting climate data in various formats

%description

xconv allows the user to access, subset, interpolate, manipulate, convert and visualise data files in the following formats:

    * NetCDF format
    * GRIB format
    * GrADS format
    * UK Met Office Unified Model Data Output format
    * UK Met Office PP format
    * DRS format 

%prep

%build

%install
[ $RPM_BUILD_ROOT != / ] && rm -fr $RPM_BUILD_ROOT

dir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $dir
#gzip -dc < %{SOURCE0} > $dir/xconv
cp %{SOURCE0} $dir/xconv
ln -s xconv $dir/convsh

# don't strip the binaries during RPM build
%define __os_install_post %{nil}

# also prevent prelink tampering with the executable, which breaks it
%define prelink_conf /etc/prelink.conf.d/xconv.conf
tmp_prelink_conf=$RPM_BUILD_ROOT/%{prelink_conf}
mkdir -p `dirname $tmp_prelink_conf`
echo "-b /usr/bin/xconv" > $tmp_prelink_conf

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Wed Feb  5 2014  <builderdev@builder.jc.rl.ac.uk> - 1.92dev-1.ceda
- upgrade to 1.92dev

* Wed Jan 23 2013  <builderdev@builder.jc.rl.ac.uk> - 1.91-3.ceda
- add prelink stuff

%files
%defattr(755,root,root)
%{_bindir}/xconv
%{_bindir}/convsh
%defattr(-,root,root)
%{prelink_conf}
