Name: xconv-testing
Version: 1.91
Release: 2.ceda%{?dist}
Source0: xconvR81.91.gz
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
dir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $dir
gzip -dc < %{SOURCE0} > $dir/xconv
ln -s xconv $dir/convsh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%{_bindir}/xconv
%{_bindir}/convsh
