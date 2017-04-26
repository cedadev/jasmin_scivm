%define pname xxdiff
Summary: Python package for writing scripts around xxdiff
Name: python27-%{pname}
Version: 3.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.bz2
License: GNU GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Martin Blais <blais@furius.ca>
Url: http://furius.ca/xxdiff
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

This package provides a number of scripts that are used to perform a variety of
tasks that all involve getting user verification and feedback using the xxdiff
graphical differences viewer.

For example, there are scripts to perform global renaming of strings within a
large codebase, where each transformed file is viewed by the user with an
xxdiff, accepted, rejected or merged changes written over the original file
(file backups are supported).  Also, this infrastructure is mostly provided as
modules, in order to allow users to write file transformations in Python and to
leverage this interactive confirmation process.

There are also scripts that visualize diffs for a number of SCM systems, like
CVS, Subversion, etc.  This package was born after a number of these useful
scripts had sprouted, and it became apparent that sharing the common code for
the scripts would be a great advantage to tools writers.

See documentation for a full list of the scripts and their role:
http://furius.ca/xxdiff/doc/xxdiff-scripts.html

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

install -c -m 755 -s bin/xxdiff ${RPM_BUILD_ROOT}%{_bindir}/
install -c -m 644 src/xxdiff.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/xxdiff.1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Tue May 19 2015  <builderdev@builder.jc.rl.ac.uk> - 3.2-1.ceda
- initial build based on vanilla python 2.7 package plus install of executable and manpage

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_bindir}/xxdiff
%{_mandir}/man1/xxdiff.1

