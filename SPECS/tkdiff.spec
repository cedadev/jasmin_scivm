Name: tkdiff
Version: 4.2
Release: 1.ceda%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GPL v2
Group: Development/Tools
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: John M. Klassa
Url: http://tkdiff.sourceforge.net
Summary: a Tcl/Tk front-end to diff
Requires: tk

%description
TkDiff is a Tcl/Tk front-end to diff for Unix and  Windows, and is Copyright (C) 1994-2005 by John M. Klassa.

%prep
%setup -n tkdiff-unix

%build

%install
dir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $dir
cp tkdiff $dir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/tkdiff
