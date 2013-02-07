#
# spec file for package tclkit
#
# norootforbuild

%define kitgen_version 20130117
%define tcl_version 8.5.7
%define tcl_version_short 8.5

Name:           tclkit
Requires:       tcl = 1:%{tcl_version}
BuildRequires:  upx
BuildRequires:  tcl = 1:%{tcl_version}
License:        https://code.google.com/p/tclkit/
Group:          Development/Languages
AutoReqProv:    on
Version:        %{kitgen_version}.%{tcl_version}
Release:        1.ceda
# from http://github.com/patthoyts/kitgen/archives/master
Source:        kitgen-%{kitgen_version}.zip
# from http://sourceforge.net/projects/tcl/files/Tcl/
Source1:        tcl%{tcl_version}-src.tar.gz
Source2:        tk%{tcl_version}-src.tar.gz
Url:            https://code.google.com/p/tclkit/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Self-contained runtime for Tcl/Tk

%description
A Tclkit is a single-file executable that provides a complete Tcl and Tk runtime and can execute both normal tcl scripts or script archive files known as StarKits.

%define build_exe_dir %{tcl_version_short}/linux-ix86

%prep
%setup1 -n kitgen-master
tar xvfz %{SOURCE1}
tar xvfz %{SOURCE2}
mkdir %{tcl_version_short}
mv tcl%{tcl_version} %{tcl_version_short}/tcl
mv tk%{tcl_version} %{tcl_version_short}/tk
sh config.sh %{build_exe_dir} thread mk cli dyn 

%build
cd %{build_exe_dir}
make
./tclkit-cli ../../validate.tcl 

%install
tmp_bindir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $tmp_bindir
cd %{build_exe_dir}
pwd
for exe in `find . -maxdepth 1  -type f -perm -100`
do
   cp $exe $tmp_bindir/
done
# don't strip the binaries
%define __os_install_post %{nil}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*

%changelog
* Thu Jan 17 2013  Alan Iwi - 20130117.8.5.7-1.ceda
- initial version
