Name:           lxterminal
Version:        0.1.9
Release:        1.ceda%{?dist}
Summary:        Desktop-independent VTE-based terminal emulator
Summary(de):    Desktop-unabhängiger VTE-basierter Terminal Emulator

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://lxde.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
# http://lxde.git.sourceforge.net/git/gitweb.cgi?p=lxde/lxterminal;a=commit;h=2cda6d2217f82cc993f4758ed44ef74c61f729ba
Patch0:         lxterminal-0.1.9-fixed-vte-failure-because-of-deprecated-API.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel >= 2.6
BuildRequires:  vte-devel >= 0.20.0
BuildRequires:  desktop-file-utils intltool gettext

%description
LXterminal is a VTE-based terminal emulator with support for multiple tabs. 
It is completely desktop-independent and does not have any unnecessary 
dependencies. In order to reduce memory usage and increase the performance 
all instances of the terminal are sharing a single process.

%description -l de
LXTerminal ist ein VTE-basierter Terminalemulator mit Unterstützung für 
mehrere Reiter. Er ist komplett desktop-unabhängig und hat keine unnötigen 
Abhängigkeiten. Um den Speicherverbrauch zu reduzieren und die Leistung zu
erhöhen teilen sich alle Instanzen des Terminals einen einzigen Prozess.

%prep
%setup -q
%patch0 -p1 -b .deprecated-API


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --vendor="fedora"                     \
  --delete-original                                        \
  --remove-category=Utility                                \
  --add-category=System                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*.1.gz


%changelog
* Tue Nov 18 2014  <builderdev@builder.jc.rl.ac.uk> - 0.1.9-1.ceda
- rebuild on JASMIN; no changes needed

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9
- Add patch for vte >= 0.20.0

* Mon Jul 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8
- Drop all previous patches, they are part of 0.1.8
- Update German translation

* Thu May 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-2
- Major code rework from git (fixes #571591 and 596358)

* Wed Mar 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-3
- Add patch to fix DSO linking (#564717)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6
- Remove missing-icons.patch, changes got upstreamed

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-2
- Rebuilt for libvte SONAME bump

* Wed May 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5
- Fix icon for Info menu entry

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Jun 28 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3
- Add the new manpage

* Fri Jun 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Initial Fedora package
