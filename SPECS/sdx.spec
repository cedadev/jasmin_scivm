Name: sdx
Version: 20130117
Release: 1.ceda%{?dist}
Source0: http://equi4.com/pub/sk/sdx.kit
License: http://equi4.com/starkit/sdx.html
Group: Development/Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://equi4.com/starkit/sdx.html
Summary: The Starkit Developer eXtension
Requires: tclkit

%description

SDX combines a number of functions into a single command-line developer utility. Its most common use (example) is to create, browse, and unravel Starkits:

      sdx qwrap myscript.tcl ?options...?
      a quick way to create a starkit when the input is a single Tcl script

      sdx wrap mystar.kit ?options...?
      this is the way to create a starkit from a mystar.vfs/ directory structure

      sdx unwrap mystar.kit
      the reverse of wrap , it lets you disect any starkit

      sdx lsk mystar.kit
      list the contents of a starkit, as seen when mounted in Tcl

      sdx version mystar.kit
      calculate the Version ID of a starkit, report newest file found inside

      sdx mkpack oldstar.kit newstar.kit
      copies and optimally packs the Metakit data be removing all unused areas

      sdx mksplit mystar.kit
      disects a starkit into mystar.head and a mystar.tail parts (example)

      sdx update mystar.kit ?options...?
      fetch a starkit from the mini.net SDarchive, or update-in-place with minimal fuss

Not all functions in SDX are related to Starkits and Metakit. Nor are all functions generally useful in fact. Use sdx help and sdx help command for further info.

SDX is itself a Starkit, you can inspect it by doing sdx unwrap sdx and then looking at things like sdx.vfs/lib/app-sdx/sdx.tcl. SDX consists of Tcl scripts and is machine-independent: it runs on all platforms for which Tclkit is available.

%prep

%build

%install
dir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $dir
cp %{SOURCE0} $dir/
ln -s sdx.kit $dir/sdx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%{_bindir}/sdx
%{_bindir}/sdx.kit
