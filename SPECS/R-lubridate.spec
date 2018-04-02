Summary: Make Dealing with Dates a Little Easier (in R)
Name: R-lubridate
Version: 1.6.0
Release: 1.ceda%{dist}
License: GPLv2+
Group: Applications/Engineering
URL: http://cran.r-project.org/web/packages/ncdf/index.html
Source0: lubridate-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
Requires: R
BuildRequires: R

%description

Functions to work with date-times and time-spans: fast and user
friendly parsing of date-time data, extraction and updating of
components of a date-time (years, months, days, hours, minutes, and
seconds), algebraic manipulation on date-time and time-span
objects. The 'lubridate' package has a consistent and memorable syntax
that makes working with dates easy and fun. Parts of the 'CCTZ' source
code, released under the Apache 2.0 License, are included in this
package. See <https://github.com/google/cctz> for more details.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

export R_LIBS=%{buildroot}/usr/lib64/R/library
mkdir -p $R_LIBS
R CMD INSTALL %{SOURCE0}

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lubridate


%changelog
* Sat Mar 31 2018  <builderdev@builder.jc.rl.ac.uk> - 1.16-1.ceda%{dist}
- initial build

