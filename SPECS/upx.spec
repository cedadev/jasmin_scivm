#
# spec file for package upx (Version 3.03 )
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           upx
BuildRequires:  gcc-c++ ucl ucl-devel zlib-devel
License:        GPL v2 or later
Group:          Development/Tools/Other
AutoReqProv:    on
Version:        3.08
Release:        1.ceda
Source:        %{name}-%{version}-src.tar.bz2
Patch1:          %{name}-%{version}_ia64-endianity.patch
Url:            http://upx.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The Ultimate Packer for eXecutables

%description
UPX is a free, portable, extendable, high-performance executable packer
for several different executable formats. It achieves an excellent
compression ratio and offers very fast decompression. Your executables
suffer no memory overhead or other drawbacks.



Authors:
--------
    Markus F.X.J. Oberhumer <markus@oberhumer.com>

%prep
%setup -q -n %{name}-%{version}-src
%patch1 -p0

%build
export UCLDIR=%{_prefix}
make -C src CXXFLAGS="$RPM_OPT_FLAGS"
make -C doc

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_mandir}/man1
cp -a $RPM_BUILD_DIR/%{name}-%{version}-src/src/upx.out $RPM_BUILD_ROOT%{_prefix}/bin/upx
cp -a $RPM_BUILD_DIR/%{name}-%{version}-src/doc/upx.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc BUGS COPYING LICENSE NEWS PROJECTS README README.SRC THANKS
%doc doc/upx.html
%doc %{_mandir}/man1/*
%{_prefix}/bin/*

%changelog
* Thu Jan 17 2013  <builderdev@builder.jc.rl.ac.uk> - 1.ceda
- build on RedHat and upgrade to 3.08 (upgrade "endianity" patch by hand)
* Thu Jul 31 2008 pgajdos@suse.cz
- updated to 3.03:
  o optional LZMA compression
* Mon Jan 21 2008 pgajdos@suse.cz
- update to 3.02:
  * fix unmapping on arm-linux.elf
  * fix error checking in mmap for i386-linux.elf [triggered by -fPIE]
  * new options --no-mode, --no-owner and --no-time to disable preservation
    of mode (file permissions), file ownership and timestamps.
  * new format linux/mipsel supports ELF on [32-bit] R3000
  * fix argv[0] on PowerPC with --lzma
  * another bug fixes
* Thu Oct  4 2007 bg@suse.de
- use ia64 fix for hppa
* Mon Jul 23 2007 pgajdos@suse.cz
- updated to 3.00 (supports some new formats)
- fixed failed build on ia64
  * ia64-endianity.patch
* Thu Mar 29 2007 meissner@suse.de
- buildrequire zlib-devel
* Tue Oct 31 2006 meissner@suse.de
- build with RPM_OPT_FLAGS
* Thu Oct  5 2006 anicka@suse.cz
- update to 2.02
  * support for many new formats
  * various bugfixes
- build for all architectures (new formats supported)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Sep 29 2005 dmueller@suse.de
- add norootforbuild
* Wed Aug 11 2004 tcrhak@suse.cz
- update to 1.25
* Thu Jul 24 2003 tcrhak@suse.cz
- update to version 1.24
* Fri May 10 2002 ro@suse.de
- removed malloc hacks (does not work this way with gcc-3.1)
* Sat Apr 20 2002 ro@suse.de
- fixed changelog
* Fri Apr 19 2002 tcrhak@suse.cz
- fixed to compile with gcc 3.1
* Mon Jan 14 2002 rvasice@suse.cz
- fix URL in spec file
* Wed Jun 20 2001 rvasice@suse.cz
- fix neededforbuild section
* Fri Jun 15 2001 rvasice@suse.cz
- initial package release (version 1.20)
