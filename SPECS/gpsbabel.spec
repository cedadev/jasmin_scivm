Name:          gpsbabel
Version:       1.4.4
Release:       1.ceda%{?dist}
Summary:       A tool to convert between various formats used by GPS devices

Group:         Applications/Text
License:       GPLv2+
URL:           http://www.gpsbabel.org
# There is no Source0 URL as upstream only offers download via HTTP
# POST, and only for the latest release.  Point your web browser to
# http://www.gpsbabel.org/download.html, scroll down to the linux
# source tarball download button and click on it.  Or try the included
# gpsbabel-download-latest.py script to download the latest tarball
# (requires the python-BeautifulSoup package):
#
# $ ./gpsbabel-download-latest.py
# Loading HTML page http://www.gpsbabel.org/download.html
# Running curl to get tarball via HTTP POST: gpsbabel-1.4.2.tar.gz
#   % Total   % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                 Dload  Upload   Total   Spent    Left  Speed
# 100 5421k 100 5421k  100   260   252k     12  0:00:21  0:00:21 --:--:--  263k
# Successfully downloaded tarball: gpsbabel-1.4.2.tar.gz
# $
Source0:       %{name}-%{version}.tar.gz
Source2:       %{name}.png
Source21:      http://www.gpsbabel.org/style3.css
# Use system shapelib - not suitable for upstream in this form.
Patch11:       gpsbabel-1.4.3-use-system-shapelib.patch
# Remove network access requirement for XML doc builds and HTML doc reading
Patch21:       gpsbabel-1.4.2-xmldoc.patch
# Pickup gmapbase.html from /usr/share/gpsbabel
Patch22:       gpsbabel-1.4.3-gmapbase.patch
# No automatic phone home by default (RHBZ 668865)
Patch23:       gpsbabel-1.4.3-nosolicitation.patch
# Fix invalid gzFile pointer use
Patch24:       gpsbabel-1.4.3-gzip.diff
# Add aarch64 (RHBZ 925480)
Patch25:       gpsbabel-1.4.4-config.patch

BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%global translationdir %{_datadir}/qt4/translations

BuildRequires: expat-devel
BuildRequires: libusb-devel
BuildRequires: zlib-devel
%if (0%{?fedora} >= 14)
# f14, f15, etc.
BuildRequires: qt-devel
BuildRequires: qt-webkit-devel
%define        build_gui 1
%else
%if 0%{?fedora}
# f13, f12 mainly
BuildRequires: qt4-devel
BuildRequires: qt4-webkit-devel
%define        build_gui 1
%else
# EL stuff, e.g. el6
%endif
%endif
BuildRequires: desktop-file-utils
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: shapelib-devel

%description
Converts GPS waypoint, route, and track data from one format type
to another.

%if 0%{?build_gui}
%package gui
Summary:        Qt GUI interface for GPSBabel
Group:          Applications/Engineering
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}

%description gui
Qt GUI interface for GPSBabel
%endif

%prep
%setup -q
# Use system shapelib instead of bundled partial shapelib
rm -rf shapelib
%patch11 -p1
# Remove network access requirement for XML doc builds and HTML doc reading
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

# Get rid of bundled zlib
# configure --with-zlib=system is not enough,
# building still accesses bundled zlib headers
rm -rf zlib/*
touch zlib/empty.in
sed -i -e 's, zlib/[^ ]*,,g' -e '/^zlib*/d' -e 's, jeeps/../zlib/[^ ]*,,g' Makefile.in


cp -p %{SOURCE21} gpsbabel.org-style3.css

# Avoid calling autoconf from Makefile
touch -r configure.in configure Makefile.in

# fix bad execute perms
find . -type f \( -name '*.c' -or -name '*.h' -or -name '*.cpp' \) -print0 |
     xargs -0 chmod a-x

%build
%configure --with-zlib=system --with-doc=./manual
make %{?_smp_mflags}
perl xmldoc/makedoc
make gpsbabel.html

%if 0%{?build_gui}
pushd gui
qmake-qt4
lrelease-qt4 *.ts
make %{?_smp_mflags}
popd
%endif

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%if 0%{?build_gui}
make -C gui DESTDIR=%{buildroot} install

install -m 0755 -d                            %{buildroot}%{_bindir}/
install -m 0755 -p gui/objects/gpsbabelfe-bin %{buildroot}%{_bindir}/
install -m 0755 -d                            %{buildroot}%{translationdir}/
install -m 0644 -p gui/gpsbabel*_*.qm         %{buildroot}%{translationdir}/

install -m 0755 -d %{buildroot}%{_datadir}/gpsbabel
install -m 0644 -p gui/gmapbase.html %{buildroot}%{_datadir}/gpsbabel

desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        gui/gpsbabel.desktop

install -m 0755 -d            %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%find_lang %{name} --with-qt --all-name
%endif

%clean
rm -rf %{buildroot}

%if 0%{?build_gui}
%post gui
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun gui
if [ $1 -eq 0 ] ; then
        touch --no-create %{_datadir}/icons/hicolor &>/dev/null
        gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gui
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%defattr(-,root,root,-)
%doc README* COPYING AUTHORS
%doc gpsbabel.html gpsbabel.org-style3.css
%{_bindir}/gpsbabel

%if 0%{?build_gui}
%files gui -f %{name}.lang
%defattr(-,root,root,-)
%doc gui/{AUTHORS,COPYING*,README*,TODO}
%{_bindir}/gpsbabelfe-bin
%{_datadir}/gpsbabel
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*
%endif

%changelog
* Fri Apr 26 2013  <builderdev@builder.jc.rl.ac.uk> - 1.4.4-1.ceda
- local build on jasmin - otherwise unmodified

* Sun Mar 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.4-3
- Add aarch64 (RHBZ 925480).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.4-1
- Upstream update.
- Rebase patches.
- Use upstream gpsbabel.desktop.
- Address RHBZ 668865.
- Fix gzFile pointer abuse.
- Install gmapbase.html to /usr/share/gpsbabel.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.4.2-6
- Rebuild for libusb-config (#715220)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.2-4
- Have this spec file build on f12,f13,f14,f15,el6. (el6 without GUI).
- Rename local copy of style3.css
- Ship translations for the GUI
- Enforce network less doc build with xsltproc --nonet

* Tue Jan 11 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.2-2
- Shut up desktop-file-install warnings
- Comment the patches in the spec file

* Tue Jan 11 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.2-1
- Update to 1.4.2
- Document how to get source tarball via HTTP POST
- Use Fedora's system shapelib instead of gpsbabel's bundled shapelib parts
- Use new mktemp based BuildRoot
- Build and view gpsbabel.html without network access
- Avoid rpm macros for scriptlet commands
- Remove x bit also from src files in subdirectories
- Add Additional Category to .desktop file: Geography

* Fri Sep 17 2010 Mikhail Kalenkov <mikhail.kalenkov@gmail.com> - 1.4.1-2
- build documentation (gpsbabel.html)

* Thu Sep 16 2010 Mikhail Kalenkov <mikhail.kalenkov@gmail.com> - 1.4.1-1
- update to 1.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Douglas E. Warner <silfreed@silfreed.net> - 1.3.6-1
- update to 1.3.6

* Fri May 09 2008 Douglas E. Warner <silfreed@silfreed.net> - 1.3.5-1
- update to 1.3.5
- switching out variables for macros; adding macros for commands
- fixing license to be GPLv2+
- adding patch to fix re-running autoconf
- perserving times when installing gpsbabel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.4-2
- Autorebuild for GCC 4.3

* Tue Dec 18 2007 Douglas E. Warner <silfreed@silfreed.net> - 1.3.4-1
- Update to 1.3.4

* Wed Apr 16 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.3-1
- Make first Fedora spec based on the one provided upstream
