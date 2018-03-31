Summary: netCDF access library for R
Name: R-ncdf
Version: 1.16
Release: 1.ceda%{dist}
License: GPLv2+
Group: Applications/Engineering
URL: http://cran.r-project.org/web/packages/ncdf/index.html
Source0: https://cran.r-project.org/src/contrib/ncdf4_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
Requires: R
BuildRequires: R

%description

Provides a high-level R interface to data files written using
Unidata's netCDF library (version 4 or earlier), which are binary data
files that are portable across platforms and include metadata
information in addition to the data sets. Using this package, netCDF
files (either version 4 or "classic" version 3) can be opened and data
sets read in easily. It is also easy to create new netCDF dimensions,
variables, and files, in either version 3 or 4 format, and manipulate
existing netCDF files. This package replaces the former ncdf package,
which only worked with netcdf version 3 files. For various reasons the
names of the functions have had to be changed from the names in the
ncdf package. The old ncdf package is still available at the URL given
below, if you need to have backward compatibility. It should be
possible to have both the ncdf and ncdf4 packages installed
simultaneously without a problem. However, the ncdf package does not
provide an interface for netcdf version 4 files.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

export R_LIBS=%{buildroot}/usr/lib64/R/library
mkdir -p $R_LIBS
echo "install.packages('%{SOURCE0}', repo=NULL)" | R --no-save

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ncdf4


%changelog

* Sat Mar 31 2018  <builderdev@builder.jc.rl.ac.uk> - 1.16-1.ceda%{dist}
- initial build (modelled on R-ncdf)

