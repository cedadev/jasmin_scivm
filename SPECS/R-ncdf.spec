Summary: netCDF access library for R
Name: R-ncdf
Version: 1.6.8
Release: 2.ceda%{dist}
License: GPLv2+
Group: Applications/Engineering
URL: http://cran.r-project.org/web/packages/ncdf/index.html
Source0: http://cran.ma.imperial.ac.uk/src/contrib/ncdf_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
Requires: R
BuildRequires: R

%description

        This package provides a high-level R interface to
        Unidata's netCDF data files, which are portable across
        platforms and include metadata information in addition to the
        data sets. Using this package netCDF files can be opened and
        data sets read in easily. It is also easy to create new netCDF
        dimensions, variables, and files, or manipulate existing netCDF
        files. This interface provides considerably more functionality
        than the old "netCDF" package for R, and is not compatible with
        the old "netCDF" package for R. Release 1.2 (2005-01-24) adds
        better support for character variables, and miscellaneous bug
        fixes.  Release 1.3 (2005-03-27) is for miscellaneous bug
        fixes, and improves the documentation.  Release 1.4
        (2005-06-27) improves the efficiency, and adds small bug fixes.
        Release 1.5 (2006-02-27) adds support for byte variables, plus
        small bug fixes. Release 1.6 (2006-06-19) adds various bug
        fixes, plus support for making dimensions WITHOUT dimvars
        (coordinate variables), although I think this is a bad idea in
        general.  ALSO, the default behavior for put.var.ncdf with
        unlimited variables and NO specified start and count parameters
        has changed!  Before, the default was to append to the end of
        the existing variable.  Now, the default is to assume a start
        of 1 along each dimension, and a count of the current length of
        each dimension.  This really can be ambiguous when using an
        unlimited dimension. I always specify both start and count when
        writing to a variable with an unlimited dimension, and suggest
        you do as well.  I may require this in a future release, as it
        seems to cause people problems.

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
/usr/lib64/R/library/ncdf


%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.6.8-2.ceda%{dist}
- rebuild with netcdf 4.4.0

* Wed Jul 15 2015  <builderdev@builder.jc.rl.ac.uk> - ncdf-1
- Initial build.

