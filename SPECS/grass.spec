# "shared lib calls exit" -- http://trac.osgeo.org/grass/ticket/1598

# The manpages are created from HTML with a parser, that is
# included. It has some flaws, see:
# https://trac.osgeo.org/grass/ticket/612

# Ticket on FHS violation
# http://trac.osgeo.org/grass/ticket/1610

#TODO: Add Module Makefile for developers?
#TODO: xml-etree?
#TODO: Consider to drop the separate libs packages, like Debian did
#TODO: Review the pkgconf file
# Ubuntu doesn't have the Requires line in the pkgconfig file
## Ubuntu's gdal-grass is called libgdal1-1.7.0-grass
#TODO: Consider a documentation sub-package

# All EPEL 5 specific elements are left inside to make life easier for ELGIS

%global shortversion 64

%if %{__isa_bits} == 64
%global configure_64_bit --enable-64bit
%endif

Name:      grass
Version:   6.4.4
Release:   1.ceda%{?dist}
Summary:   GRASS - Geographic Resources Analysis Support System
Group:     Applications/Engineering
License:   GPLv2+
URL:       http://grass.osgeo.org
Source0:   http://grass.osgeo.org/%{name}%{shortversion}/source/%{name}-%{version}.tar.gz
Source2:   %{name}-config.h
Patch0:    0001-grass-pkgconf.patch

# Warning: This patch contains the GRASS version number
Patch1:    0002-grass-shlib-soname.patch

Patch2:    0003-grass-docfiles.patch

# Address -Werror-format-string-security issues.
Patch3:    0004-Eliminate-Werror-format-string-security-issues.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  proj-nad proj-epsg python27-wxPython
Requires:  wxGTK-gl
Requires:  python27-numpy

BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw2-devel
BuildRequires:  flex
BuildRequires:  freetype-devel
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  gettext
BuildRequires:  lapack-devel
BuildRequires:  openmotif-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGLw-devel
BuildRequires:  mysql-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  proj-devel  

#TODO: Really BR?
BuildRequires:  proj-epsg
BuildRequires:  proj-nad

#BuildRequires:  python-devel
BuildRequires:  python27

BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  swig
BuildRequires:  tk-devel 
BuildRequires:  unixODBC-devel
BuildRequires:  wxGTK-devel
#BuildRequires:  wxPython-devel
BuildRequires:  python27-wxPython

BuildRequires:  zlib-devel

#TODO: Python PIL will be required

# We have multi-lib triage
%if "%{_lib}" == "lib"
%global cpuarch 32
%else
%global cpuarch 64
%endif

%description
GRASS (Geographic Resources Analysis Support System) is a Geographic
Information System (GIS) used for geospatial data management and
analysis, image processing, graphics/maps production, spatial
modeling, and visualization. GRASS is currently used in academic and
commercial settings around the world, as well as by many governmental
agencies and environmental consulting companies.

%package libs
Summary: GRASS (Geographic Resources Analysis Support System) runtime libraries
Group: Applications/Engineering

%description libs
GRASS (Geographic Resources Analysis Support System) runtime libraries.

%package devel
Summary: GRASS (Geographic Resources Analysis Support System) development headers
Group: Applications/Engineering
Requires: %{name}%{?isa}-libs = %{version}-%{release}

# Can be removed after EOL of EPEL5
Requires: pkgconfig

Requires: openmotif-devel python27-wxPython
Requires: mesa-libGL-devel libX11-devel libXt-devel
Requires: gdal-devel proj-devel xorg-x11-proto-devel

%description devel
GRASS (Geographic Resources Analysis Support System) development headers.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Correct mysql_config query
sed -i 's|--libmysqld-libs|--libs|g' configure

# Preserve timestamp during install process
# TODO: Ticket?
sed -i 's|^cp |cp -p |' tools/build_html_index.sh
sed -i 's|-cp |-cp -p |' Makefile

# EOL wrong
sed -i -e 's|\r||g' gui/icons/%{name}/vdigit/box.xbm


%build
# Keep timestamp over install section
#TODO: Necessary?
export INSTALL="%{__install} -c -p"

%define python python2.7

%configure \
   --enable-largefile \
   --enable-shared \
   --with-blas \
   --with-cairo \
   --with-cxx \
   --with-fftw \
   --with-freetype-includes=%{_includedir}/freetype2 \
   --with-freetype=yes \
   --with-gdal \
   --with-geos \
   --with-glw \
   --with-lapack \
   --with-motif \
   --with-mysql \
   --with-mysql-includes=%{_includedir}/mysql \
   --with-mysql-libs=%{_libdir}/mysql \
   --with-nls \
   --with-odbc \
   --with-opengl \
   --with-postgres  \
   --with-proj \
   --with-proj-share=%{_datadir}/proj \
   --with-python=%{python} \
   --with-readline \
   --with-sqlite \
   --with-wxwidgets=wx-config \
   --with-x \
   %{configure_64_bit}

make %{?_smp_mflags} PYTHON=%{python}


%install
rm -rf %{buildroot}

# make install
make prefix=%{buildroot}%{_prefix} BINDIR=%{buildroot}%{_bindir} \
    PREFIX=%{buildroot}%{_prefix} install

# Change GISBASE in startup script to point to systems %{_libdir}/%{name}-%{version}
#TODO: Still necessary? Version-less?
sed -i -e "1,\$s&^GISBASE.*&GISBASE=%{_libdir}/%{name}-%{version}&"  \
    %{buildroot}%{_bindir}/%{name}%{shortversion}

# Sadly, parts of the following can't be done safely in prep,
# hence they're done here
# Replace GISBASE environment variable with paths that match our documentation file layout
sed -i -e 's|$env(GISBASE)/docs/|%{_docdir}/%{name}-%{version}/docs/|' \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/gis_set.tcl \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/gui.tcl \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/nviz2.2_script
sed -i -e 's|C_BASE="$GISBASE"|C_BASE=\"%{_docdir}/%{name}-%{version}/docs"|g' \
    %{buildroot}%{_prefix}/%{name}-%{version}/scripts/g.manual
sed -i -e 's|%{name}-%{version}/docs|%{name}-%{version}|g' \
    %{buildroot}%{_prefix}/%{name}-%{version}/scripts/g.manual
sed -i -e 's|(\"GISBASE\"), \"docs\", \"html\", \"icons\", \"silk\")|(\"GISBASE\"), \"icons\", \"silk\")|g' \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/wxpython/icons/icon.py
sed -i -e 's|self.fspath = os.path.join(gisbase|self.fspath = os.path.join("%{_docdir}/%{name}-%{version}\"|' \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/wxpython/gui_core/ghelp.py
sed -i 's|file://$env(GISBASE)|file://%{_docdir}/%{name}-%{version}|' %{buildroot}%{_prefix}/%{name}-%{version}/etc/r.li.setup/r.li.setup.main
sed -i 's|GRASS_DOC_BASE=`check_docbase "$GISBASE"`|GRASS_DOC_BASE=%{_docdir}/%{name}-%{version}|' %{buildroot}%{_prefix}/%{name}-%{version}/scripts/g.manual

# Exceptional path for files used in the GUI as well
#TODO: Could include them in the main package too
sed -i -e 's|os\.getenv("GISBASE")|\"%{_docdir}/%{name}-libs-%{version}\"|' \
    %{buildroot}%{_prefix}/%{name}-%{version}/etc/wxpython/gui_core/ghelp.py

#TODO: Quotes and linebreaks in sed calls
# Replace GISBASE environment variable with paths that match our locale file layout
sed -i -e 's|os.path.join(os.getenv("GISBASE"), '\''locale'\''|os.path.join('\''%{_datadir}'\'', '\''locale'\''|' -e 's|os.path.join(os.getenv("GISBASE"), "etc"|os.path.join(\"%{_libdir}/%{name}-%{version}\", "etc"|' -e 's|self.gisbase  = os.getenv("GISBASE")|self.gisbase = "%{_docdir}/%{name}-%{version}"|' %{buildroot}%{_prefix}/%{name}-%{version}/etc/wxpython/*.py %{buildroot}%{_prefix}/%{name}-%{version}/etc/python/grass/script/*.py

# Make grass headers and libraries available on the system
mv %{buildroot}%{_prefix}/%{name}-%{version}/lib/ %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/%{name}-%{version}/include %{buildroot}%{_prefix}/
rm -rf %{buildroot}%{_includedir}/Make

# Create universal multilib header bz#341391
install -p -m 644 %{buildroot}%{_includedir}/%{name}/config.h \
           %{buildroot}%{_includedir}/%{name}/config-%{cpuarch}.h
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/%{name}/config.h

#TODO: Do we still need this?
# Fix prelink issue bz#458427
mkdir -p %{buildroot}%{_sysconfdir}/prelink.conf.d
cat > %{buildroot}%{_sysconfdir}/prelink.conf.d/%{name}-%{cpuarch}.conf <<EOF
-b %{_libdir}/libgrass_gproj.so.6.4.0
-b %{_libdir}/libgrass_sim.so.6.4
EOF

# Make man pages available on system, convert to utf8 and avoid name conflict with "parallel" manpage
mkdir -p %{buildroot}%{_mandir}/man1
for manpage in `find  %{buildroot}%{_prefix}/%{name}-%{version}/man/man1 -type f` ; do
   iconv -f iso8859-1 -t utf8 \
        $manpage > %{buildroot}%{_mandir}/man1/`basename $manpage`"grass"
done
sed -i -e 's/^.TH \(.*\) 1/.TH \1 1grass/' %{buildroot}%{_mandir}/man1/*
rm -rf %{buildroot}%{_prefix}/%{name}-%{version}/man

# Make locales available on system, correct case for pt_br locale
mkdir -p %{buildroot}%{_datadir}/locale/
mv %{buildroot}%{_prefix}/%{name}-%{version}/locale %{buildroot}%{_datadir}/
mv %{buildroot}%{_datadir}/locale/pt_br %{buildroot}%{_datadir}/locale/pt_BR

%find_lang %{name}mods
%find_lang %{name}libs
%find_lang %{name}wxpy

mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -m 644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/

for res in 48x48 64x64; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
  install -p -m 644 gui/icons/%{name}-${res}.png %{buildroot}%{_datadir}/icons/hicolor/${res}/apps/%{name}.png
done

# "Encoding" should be removed; Gone for releases after 6.4.3
# http://trac.osgeo.org/grass/changeset/57941/grass
desktop-file-install \
				--dir=%{buildroot}%{_datadir}/applications gui/icons/%{name}.desktop

# Install AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 gui/icons/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Correct permissions
#TODO: Still necessary; create a ticket and/or change in prep
#TODO: Why are the permissions right in Ubuntu?
find %{buildroot} -name "*.tcl" -exec chmod +r-x '{}' \;
chmod -x %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/configIndex
chmod -x %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/nviz_params
chmod -x %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/tclIndex
chmod -x %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/panelIndex
chmod +x %{buildroot}%{_prefix}/%{name}-%{version}/etc/g.mapsets.tcl
chmod +x %{buildroot}%{_prefix}/%{name}-%{version}/etc/dm/tksys.tcl
chmod +x %{buildroot}%{_prefix}/%{name}-%{version}/etc/gm/tksys.tcl
chmod +x %{buildroot}%{_prefix}/%{name}-%{version}/etc/gm/animate.tcl

# fixup few nviz script header, it will anyway always be executed by nviz
for nviz in {script_play,nviz2.2_script,script_tools,script_file_tools,script_get_line}; do
 cat %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/$nviz \
  | grep -v '#!nviz' > %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/$nviz.tmp 
 mv  %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/$nviz.tmp \
     %{buildroot}%{_prefix}/%{name}-%{version}/etc/nviz2.2/scripts/$nviz
done

# Move icon folder in GISBASE and set its path to be FHS compliant
mv %{buildroot}%{_prefix}/%{name}-%{version}/docs/html/icons %{buildroot}%{_prefix}/%{name}-%{version}/

# Switch to the system wide docs, to be FHS compliant
rm -rf %{buildroot}%{_prefix}/%{name}-%{version}/docs

# Hide GISBASE into system's %{_libdir} instead, to be FHS compliant
mv %{buildroot}%{_prefix}/%{name}-%{version} %{buildroot}%{_libdir}/

# Correct font path
sed -i -e 's|%{buildroot}%{_prefix}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|' \
%{buildroot}%{_libdir}/%{name}-%{version}/etc/fontcap

# Create versionless symlinks for binary and libdir
# The libdir symlink is handy for QGIS. QGIS asks the user for gisbase
# and then stores it. See BZ 711860
# The binary symlink keeps us from updating the desktop file
# Ubuntu does it the same way
ln -s %{_bindir}/%{name}%{shortversion} %{buildroot}%{_bindir}/%{name}
ln -s %{_libdir}/%{name}-%{version} %{buildroot}%{_libdir}/%{name}


%clean
rm -rf %{buildroot}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files -f %{name}mods.lang -f %{name}libs.lang -f %{name}wxpy.lang
%doc dist.*/docs
%{_sysconfdir}/prelink.conf.d/%{name}-%{cpuarch}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}%{shortversion}
%{_bindir}/gem%{shortversion}
%dir %{_libdir}/%{name}-%{version}
%exclude %{_libdir}/%{name}-%{version}/etc/*.table
%exclude %{_libdir}/%{name}-%{version}/driver/db/*
%{_libdir}/%{name}-%{version}/*
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/locale/*/LC_MESSAGES
%{_mandir}/man1/*.1grass*

%files libs
%doc AUTHORS COPYING GPL.TXT CHANGES ChangeLog_%{version}.gz translators.csv contributors.csv contributors_extra.csv
%{_libdir}/%{name}
%{_libdir}/lib%{name}_*.so.*
%{_libdir}/%{name}-%{version}/etc/*.table
%{_libdir}/%{name}-%{version}/driver/db/*

%files devel
%doc TODO doc SUBMITTING*
%exclude %{_libdir}/lib%{name}_*.a
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_libdir}/lib%{name}_*.so


%changelog
* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 6.4.4-1.ceda
- rebuilding from RedHat RPM on JASMIN

* Fri Nov 14 2014 Dave Johansen <dave@johansen@gmail.com> - 6.4.4-6
- Using openmotif-devel and removing --set-icon so it will build on RHEL 6

* Tue Sep 23 2014 Richard Hughes <richard@hughsie.com> - 6.4.4-5
- Install the shipped AppData file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 6.4.4-3
- Add 0004-Eliminate-Werror-format-string-security-issues.patch (RHBZ#1037102)
- Re-enable building w/ -Werror=format-security.

* Sat Aug 09 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 6.4.4-2
- Rebase patches against grass-6.4.4.
- Convert -Werror=format-security into warnings (RHBZ#1106720).
- Minor spec cleanup.

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> - 6.4.4-1
- Update to 6.4.4
- Make 64bit conditionals generic

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 6.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Thu Mar 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 6.4.3-6
- Don't ship patch backup files

* Mon Oct 14 2013 Volker Fröhlich <volker27@gmx.at> - 6.4.3-5
- Solve build failure on PPC tests (BZ#961838)

* Wed Oct 9 2013 Devrim Gündüz <devrim@gunduz.org> - 6.4.3-4
- Rebuild against new GEOS

* Thu Oct  3 2013 Volker Fröhlich <volker27@gmx.at> - 6.4.3-3
- Add patch for release name encoding crash
- Use upstream desktop file (BZ #986852)
- Install icons of different sizes

* Sat Sep 14 2013 Volker Fröhlich <volker27@gmx.at> - 6.4.3-2
- Remove gcc patch (upstream)
- Remove useless BR for libjpeg
- Make config.h a source file instead of defining it in the spec file
- Truncate changelog

* Thu Sep 12 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.3-1
- Update to 6.4.3
- Rebuild with new geos.

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 6.4.2-11
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 6.4.2-9
- Drop desktop vendor tag.

* Wed Mar 06 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.2-8
- Rebuild with new geos.

* Fri Jan 25 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.2-7
- Rebuild with geos 3.3.7.

* Sun Nov 18 2012 Volker Fröhlich <volker27@gmx.at> - 6.4.2-6
- Rebuild with ever newer geos

* Wed Nov 14 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.2-5
- Rebuild with new geos.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.2-3
- Rebuilt

* Sun Mar  4 2012 Volker Fröhlich <volker27@gmx.at> - 6.4.2-2
- Solve name conflict with "parallel" man pages (BZ 797824)
- Correct man page encoding conversion
- Build with multiple workers; assumuption on race-condition was wrong

* Fri Mar  2 2012 Tom Callaway <spot@fedoraproject.org> - 6.4.2-1
- update to 6.4.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-8
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Volker Fröhlich <volker27@gmx.at> - 6.4.1-7
- Race condition in build system assumed -- going back to one worker

* Mon Jan 9 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.4.1-6
- Rebuilt with new geos

* Wed Nov 23 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.1-5
- Move string substitution back to the install section, because
  it causes problems otherwise
- Add patch for libpng API change

* Wed Nov 02 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.1-4
- Remove encoding from desktop file
- Remove BR on wxGTK, because wxGTK requires it anyway
- Disable Ubuntu patches, because they don't seem to work in Fedora
- Move all the string substitution for locales and docs to prep
- Use name macro in Source
- Drop custom compiler flags -- no evidence they serve a purpose
- Remove 2 unnecessary chmods
- Don't use sysconfdir macro in places, where etc means something different
- Add contributors to documentation

* Wed Nov 02 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.1-3
- Patch locale and documentation paths properly for the GUI

* Thu Sep 22 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.1-2
- Remove duplicate documentation
- Correct further documentation paths
- Create version-less symlinks for library directory and binary
- Supply all lang files to the files section directly
- Add ternary operator patch for Python 2.4 (ELGIS)

* Tue Aug 02 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.1-1
- Update to 6.4.1
- Remove explicit lib and include dirs, where not necessary
- Really build with geos
- Remove sed call on ncurses

* Tue Aug 02 2011 Volker Fröhlich <volker27@gmx.at> - 6.4.0-4
- Correct license to GPLv2+
- Update URL
- Replace define with global macro
- Devel package required itself
- Simplify setup macro
- Don't add -lm manually anymore
- Correct FSF postal address
- Drop cstdio patch
- Correct Exec and Icon entry in desktop file
- Remove wrong and unnecessary translation entries from desktop file
  GRASS didn't start for the first issue
- Add numpy as requirement
- Delete defattr, as the defaults work right
- Use name macro where possible
- Devel package required itself
- Changelog doesn't need encoding conversion anymore
  Same goes for translators and infrastructure files
- Use mandir macro on one occasion
- Introduce "shortversion" macro
- Beautify case construction for 64 bit build flags
- Update syntax for Require on base package to guidelines
- Don't list LOCALE files twice, own directory
- Don't ship same documentation in different packages
- Drop README
- Simplify file list in devel package
- Replace extra icon source with one from the tarball

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 6.4.0-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 6.4.0-1
- Rebuilt with new gdal 1.7.3.
- Updated to upstream version 6.4.0.
- Removed grass-gdilib.patch
- Spec review

* Fri Dec 4 2009 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.3.0-15
- Rebuilt with new geos

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 6.3.0-14
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 23 2009 Lubomir Rintel <lkundrak@v3.sk> - 6.3.0-12
- Fix build with GCC 4.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Balint Cristian <cristian.balint@gmail.com> - 6.3.0-10
- email change
- rebuild for new mysql

* Sun Dec 07 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-9
- rebuild against newer gdal

* Sun Dec 07 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-8
- rebuild against newer gdal

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 6.3.0-7
- Rebuild for Python 2.6

* Sun Aug 24 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-6
- bz#458427 (prelink fail)
- bz#458563 (grass not able to display documentation)

* Sat Jul 05 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-5
- address bz#454146 (wxPython miss)

* Thu Jun 12 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-4
- address bz#341391 (multilib issue)

* Mon May 26 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-3
- bugfix initscripts permission

* Thu May 15 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-2
- require swig to build

* Thu May 15 2008 Balint Cristian <rezso@rdsor.ro> 6.3.0-1
- final stable release upstream
