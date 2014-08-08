%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%global php_apiver %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

# Fix for the 387 extended precision (rhbz#772637)
%ifarch i386 i686
%global FFSTORE -ffloat-store
%endif

Name:			graphviz
Summary:		Graph Visualization Tools
Version:		2.36.0
Release:		1.ceda%{?dist}
Group:			Applications/Multimedia
License:		CPL
URL:			http://www.graphviz.org/
Source0:		http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:		zlib-devel, libpng-devel, libjpeg-devel, expat-devel, freetype-devel >= 2
BuildRequires:		/bin/ksh, bison, m4, flex, tk-devel, tcl-devel >= 8.3, swig
BuildRequires:		fontconfig-devel, libtool-ltdl-devel, ruby-devel, ruby, guile-devel, python-devel, python27
BuildRequires:		libXaw-devel, libSM-devel, libXext-devel, java-devel, php-devel
BuildRequires:		cairo-devel >= 1.1.10, pango-devel, gmp-devel, lua-devel, gtk2-devel, libgnomeui-devel
BuildRequires:		gd-devel, perl-devel, swig >= 1.3.33
BuildRequires:		urw-fonts
BuildRequires:		perl-ExtUtils-Embed
Requires:		urw-fonts
Requires(post):		/sbin/ldconfig
Requires(postun):	/sbin/ldconfig

# Necessary conditionals
%global SHARP  0
%global OCAML  0
%global ARRRR  0
%global DEVIL  0
# Not in Fedora yet.
%global MING   0

%description
A collection of tools for the manipulation and layout of graphs (as in nodes 
and edges, not as in barcharts).

%package devel
Group:			Development/Libraries
Summary:		Development package for graphviz
Requires:		%{name} = %{version}-%{release}, pkgconfig
Requires:		%{name}-gd = %{version}-%{release}

%description devel
A collection of tools for the manipulation and layout of graphs (as in nodes 
and edges, not as in barcharts). This package contains development files for 
graphviz.

%if %{DEVIL}
%package devil
Group:			Applications/Multimedia
Summary:		Graphviz plugin for renderers based on DevIL
Requires:		%{name} = %{version}-%{release}

%description devil
Graphviz plugin for renderers based on DevIL. (Unless you absolutely have
to use BMP, TIF, or TGA, you are recommended to use the PNG format instead
supported directly by the cairo+pango based renderer in the base graphviz rpm.)
%endif

%package doc
Group:			Documentation
Summary:		PDF and HTML documents for graphviz

%description doc
Provides some additional PDF and HTML documentation for graphviz.

%package gd
Group:			Applications/Multimedia
Summary:		Graphviz plugin for renderers based on gd
Requires:		%{name} = %{version}-%{release}
Requires(post):		%{_bindir}/dot /sbin/ldconfig
Requires(postun):	%{_bindir}/dot /sbin/ldconfig

%description gd
Graphviz plugin for renderers based on gd.  (Unless you absolutely have to use 
GIF, you are recommended to use the PNG format instead because of the better 
quality anti-aliased lines provided by the cairo+pango based renderer.)

%package graphs
Group:			Applications/Multimedia
Summary:		Demo graphs for graphviz

%description graphs
Some demo graphs for graphviz.

%package guile
Group:			Applications/Multimedia
Summary:		Guile extension for graphviz
Requires:		%{name} = %{version}-%{release}, guile

%description guile
Guile extension for graphviz.

%package java
Group:			Applications/Multimedia
Summary:		Java extension for graphviz
Requires:		%{name} = %{version}-%{release}

%description java
Java extension for graphviz.

%package lua
Group:			Applications/Multimedia
Summary:		Lua extension for graphviz
Requires:		%{name} = %{version}-%{release}, lua

%description lua
Lua extension for graphviz.

%if %{MING}
%package ming
Group:			Applications/Multimedia
Summary:		Graphviz plugin for flash renderer based on ming
Requires:		%{name} = %{version}-%{release}

%description ming
Graphviz plugin for -Tswf (flash) renderer based on ming.
%endif

%if %{OCAML}
%package ocaml
Group:			Applications/Multimedia
Summary:		Ocaml extension for graphviz
Requires:		%{name} = %{version}-%{release}, ocaml

%description ocaml
Ocaml extension for graphviz.
%endif

%package perl
Group:			Applications/Multimedia
Summary:		Perl extension for graphviz
Requires:		%{name} = %{version}-%{release}
Requires:		perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description perl
Perl extension for graphviz.

%package php
Group:			Applications/Multimedia
Summary:		PHP extension for graphviz
Requires:		%{name} = %{version}-%{release}
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}

%description php
PHP extension for graphviz.

%package python
Group:			Applications/Multimedia
Summary:		Python extension for graphviz
Requires:		%{name} = %{version}-%{release}, python

%description python
Python extension for graphviz.

%package python27
Group:			Applications/Multimedia
Summary:		Python 2.7 extension for graphviz
Requires:		%{name} = %{version}-%{release}, python27

%description python27
Python 2.7 extension for graphviz.

%if %{ARRRR}
%package R
Group:			Applications/Multimedia
Summary:		R extension for graphviz
Requires:		%{name} = %{version}-%{release}, R-core

%description R
R extension for graphviz.
%endif

%package ruby
Group:			Applications/Multimedia
Summary:		Ruby extension for graphviz
Requires:		%{name} = %{version}-%{release}, ruby

%description ruby
Ruby extension for graphviz.

%if %{SHARP}
%package sharp
Group:			Applications/Multimedia
Summary:		C# extension for graphviz
Requires:		%{name} = %{version}-%{release}, mono-core

%description sharp
C# extension for graphviz.
%endif

%package tcl
Group:			Applications/Multimedia
Summary:		Tcl extension & tools for graphviz
Requires:		%{name} = %{version}-%{release}, tcl >= 8.3, tk

%description tcl
Various tcl packages (extensions) for the graphviz tools.

%prep
%setup -q

# fix sources permissions
find . -type f '(' -name '*.h' -or -name '*.c' ')' -exec chmod 644 {} ';'

# fix ruby include path on ppc
sed -i 's:[ \t]*\(RUBY_INCLUDES=`echo $RUBY_INCLUDES | sed '"'s/powerpc/universal/'"'`.*\)$:#\1:' configure

%build
# %%define NO_IO --disable-io

# Hack in the java includes we need
sed -i '/JavaVM.framework/!s/JAVA_INCLUDES=/JAVA_INCLUDES=\"_MY_JAVA_INCLUDES_\"/g' configure
sed -i 's|_MY_JAVA_INCLUDES_|-I%{java_home}/include/ -I%{java_home}/include/linux/|g' configure
%configure --with-x --disable-static --disable-dependency-tracking --without-mylibgd --with-ipsepcola --with-pangocairo --with-gdk-pixbuf \
	   --enable-python27 \
%if ! %{SHARP}
	--disable-sharp \
%endif
%if ! %{OCAML}
	--disable-ocaml \
%endif
%if ! %{MING}
	--without-ming \
%endif
%if ! %{ARRRR}
	--disable-r \
%endif
%if ! %{DEVIL}
	--without-devil \
%endif

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing %{?FFSTORE}" CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing %{?FFSTORE}"

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} \
	docdir=%{buildroot}%{_docdir}/%{name}-%{version} \
	pkgconfigdir=%{_libdir}/pkgconfig \
	install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod -x %{buildroot}%{_datadir}/%{name}/lefty/*

# Move docs to the right place
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mv %{buildroot}%{_datadir}/%{name}/doc/* %{buildroot}%{_docdir}/%{name}-%{version}

# Install README
install -m0644 README %{buildroot}%{_docdir}/%{name}-%{version}

# remove hidden .libs dir
rm -rf libltdl/.libs

# PHP configuration file
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} << __EOF__ > %{buildroot}%{_sysconfdir}/php.d/%{name}.ini
; Enable %{name} extension module
extension=gv.so
__EOF__

# Remove executable modes from demos
find %{buildroot}%{_datadir}/%{name}/demo -type f -exec chmod a-x {} ';'

# Move demos to doc
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}-%{version}/

# Rename python demos to prevent byte compilation
find %{buildroot}%{_docdir}/%{name}-%{version}/demo -type f -name "*.py" -exec mv {} {}.demo ';'

%check
cd rtest
make rtest

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
%{_bindir}/dot -c

# if there is no dot after everything else is done, then remove config*
%postun
if [ $1 -eq 0 ]; then
	rm -f %{_libdir}/graphviz/config* || :
fi
/sbin/ldconfig

# run "dot -c" to generate plugin config in %%{_libdir}/graphviz/config*
%if %{DEVIL}
%post devil
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig

%postun devil
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig
%endif

# run "dot -c" to generate plugin config in %%{_libdir}/graphviz/config*
%post gd
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig

%postun gd
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig

%if %{MING}
# run "dot -c" to generate plugin config in %%{_libdir}/graphviz/config*
%post ming
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig

%postun ming
%{_bindir}/dot -c 2>/dev/null || :
/sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/*
%dir %{_libdir}/graphviz
%{_libdir}/*.so.*
%{_libdir}/graphviz/*.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%dir %{_datadir}/graphviz
%exclude %{_docdir}/%{name}-%{version}/html
%exclude %{_docdir}/%{name}-%{version}/pdf
%exclude %{_docdir}/%{name}-%{version}/demo
%{_datadir}/graphviz/lefty
%{_datadir}/graphviz/gvpr
%{_datadir}/graphviz/gvedit
%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin_gd.*
%if %{DEVIL}
%exclude %{_libdir}/graphviz/libgvplugin_devil.*
%endif
%if %{MING}
%exclude %{_libdir}/graphviz/libgvplugin_ming.*
%exclude %{_libdir}/graphviz/*fdb
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/graphviz/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.gz

%if %{DEVIL}
%files devil
%defattr(-,root,root,-)
%{_libdir}/graphviz/libgvplugin_devil.so.*
%endif

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/html
%doc %{_docdir}/%{name}-%{version}/pdf
%doc %{_docdir}/%{name}-%{version}/demo

%files gd
%defattr(-,root,root,-)
%{_libdir}/graphviz/libgvplugin_gd.so.*

%files graphs
%defattr(-,root,root,-)
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/graphs

%files guile
%defattr(-,root,root,-)
%{_libdir}/graphviz/guile/
%{_mandir}/man3/gv.3guile*

%files java
%defattr(-,root,root,-)
%{_libdir}/graphviz/java/
%{_mandir}/man3/gv.3java*

%files lua
%defattr(-,root,root,-)
%{_libdir}/graphviz/lua/
%{_libdir}/lua*/*
%{_mandir}/man3/gv.3lua*

%if %{MING}
%files ming
%defattr(-,root,root,-)
%{_libdir}/graphviz/libgvplugin_ming.so.*
%{_libdir}/graphviz/*fdb
%endif

%if %{OCAML}
%files ocaml
%defattr(-,root,root,-)
%{_libdir}/graphviz/ocaml/
%{_mandir}/man3/gv.3ocaml*
%endif

%files perl
%defattr(-,root,root,-)
%{_libdir}/graphviz/perl/
%{_libdir}/perl*/*
%{_mandir}/man3/gv.3perl*

%files php
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{_libdir}/graphviz/php/
%{php_extdir}/gv.so
%{_datadir}/php*/*
%{_mandir}/man3/gv.3php*

%files python
%defattr(-,root,root,-)
%{_libdir}/graphviz/python/
%{_libdir}/python2.6/*
%{_mandir}/man3/gv.3python*

%files python27
%defattr(-,root,root,-)
%{_libdir}/graphviz/python27/
/usr/lib/python2.7/*

%if %{ARRRR}
%files R
%defattr(-,root,root,-)
%{_libdir}/graphviz/R/
%{_mandir}/man3/gv.3r.gz
%endif

%files ruby
%defattr(-,root,root,-)
%{_libdir}/graphviz/ruby/
%{_libdir}/*ruby*/*
%{_mandir}/man3/gv.3ruby*

%if %{SHARP}
%files sharp
%defattr(-,root,root,-)
%{_libdir}/graphviz/sharp/
%{_mandir}/man3/gv.3sharp*
%endif

%files tcl
%defattr(-,root,root,-)
%{_libdir}/graphviz/tcl/
%{_libdir}/tcl*/*
# hack to include gv.3tcl only if available
#  always includes tcldot.3tcl, gdtclft.3tcl
%{_mandir}/man3/*.3tcl*
%{_mandir}/man3/tkspline.3tk*


%changelog
* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 2.36.0-1.ceda
- upgrade to 2.36.0 (removing patches) and add python27 packages

* Fri Aug 17 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-10
- Fixed post/postuns for plugins
  Resolves: rhbz#849134

* Wed Aug  1 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-9
- Fixed -fno-strict-aliasing usage on C++ code
- Python demos are no longer byte compiled

* Tue May 22 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-8
- All docs are now installed into /usr/share/doc/graphviz-%%{version}
- Demos packaged as docs not to automatically bring in unnecessary deps
  Resolves: rhbz#821920
- Removed -ffast-math, added -ffloat-store (on i386) to fix arithmetic on i386
  Resolves: rhbz#772637
- Fixed build failure due to change in php_zend_api macro type

* Thu Jul 07 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-7
- Added gd as devel requirement

* Thu Jul 07 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-6
- Recompiled with -fno-strict-aliasing in CXXFLAGS

* Wed Oct 13 2010 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-5
- Fixed broken links in index.html (doc-index-fix patch)
  Resolves: rhbz#624658
- Enabled and fixed testsuite (testsuite-sigsegv-fix, rtest-errout-fix patches)
  Resolves: rhbz#624690
- Fixed rpmlint warnings on spec file
- Rebuilt with updated swig
  Resolves: rhbz#679715
- Fixed gtk plugin program-name (gtk-progname patch)
  Resolves: rhbz#640247
- Added urw-fonts to BuildRequires
- Compiled with -fno-strict-aliasing

* Mon Mar 01 2010 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-4
- Disabled R, DevIL, mono
- Fixed ruby include path on ppc

* Fri Feb 26 2010 Jaroslav Škarvada <jskarvad@redhat.com> - 2.26.0-3
- Fixed several rpmlint warnings
- Rebuilt

* Mon Jan 04 2010 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.26.0-2
- Rebuild for updated ocaml
- Happy new year, Fedora!

* Fri Dec 18 2009 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.26.0-1
- Updated to latest release
- Removed patches that have been applied upstream
- Fixed man page paths (mann -> man3)
- Disabled mono and ocaml for ARM (Jitesh Shah, BZ#532047)
- Disabled regression tests on sparc64 as well as ppc/ppc64 (Dennis Gilmore)

* Fri Aug 28 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.20.3-5.1
- disable R, DevIL, mono

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.3-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Remi Collet <Fedora@FamilleCollet.com> 2.20.3-4.1
- fix mistake in make rtest fix

* Mon Jul 13 2009 Remi Collet <Fedora@FamilleCollet.com> 2.20.3-4
- rebuild for new PHP 5.3.0 ABI (20090626)
- add PHP ABI check
- use php_extdir (and don't own it)
- add php configuration file (/etc/php.d/graphviz.ini)

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.20.3-3
- this spec makes baby animals cry... massively clean it up
- hack in java includes to build against openjdk
- add ruby as a BuildRequires (configure checks for /usr/bin/ruby)

* Wed Feb 25 2009 John Ellson <ellson@graphviz.org> 2.20.3-2.2
- fixes for swig changes

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.3-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Karsten Hopp <karsten@redhat.com> 2.20.3-.2
- make it build on s390, s390x (#469044)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.20.3-1.1
- Rebuild for Python 2.6

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.20.3-1
- update to 2.20.3

* Sat Nov 22 2008 Rex Dieter <rdieter@fedoraproject.org> 2.16.1-0.7
- respin (libtool)

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.16.1-0.6
- fix conditional comparison

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.16.1-0.5
- add Requires for versioned perl (libperl.so)

* Tue Mar 04 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16.1-0.4
- Disable R support

* Mon Mar 03 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16.1-0.2
- New upstream release (fixes BZ#433205, BZ#427376)
- Merged spec changes in from upstream
- Added patch from BZ#432683

* Tue Feb 12 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-3.3
- Added upstream-provided patch for building under GCC 4.3 (thanks John!)

* Thu Jan  3 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-3.2
- Re-added tcl/tk 8.5 patch
- Tweaked ming stuff

* Thu Jan  3 2008 Alex Lancaster <alexlan[AT]fedoraproject.org> - 2.16-3.1
- Rebuild against new Tcl 8.5

* Wed Dec 12 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-2
- What the heck?  Can't BR stuff that hasn't even gotten reviewed yet.

* Wed Nov 28 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-1
- New upstream release
- Remove arith.h patch

* Tue Sep 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.14.1-3
- Patch to resurrect arith.h

* Thu Aug 23 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.14.1-2
- Added perl-devel to BR for F7+

* Wed Aug 15 2007 John Ellson <ellson@research.att.com>
- release 2.14.1 - see ChangeLog for details
* Wed Aug 2 2007 John Ellson <ellson@research.att.com>
- release 2.14 - see ChangeLog for details
* Fri Mar 16 2007 Stephen North <north@research.att.com>
- remove xorg-X11-devel from rhel >= 5
* Mon Dec 11 2006 John Ellson <john.ellson@comcast.net>
- fix graphviz-lua description (Fedora BZ#218191)
* Tue Sep 13 2005 John Ellson <ellson@research.att.com>
- split out language bindings into their own rpms so that 
  main rpm doesn't depend on (e.g.) ocaml

* Sat Aug 13 2005 John Ellson <ellson@research.att.com>
- imported various fixes from the Fedora-Extras .spec by Oliver Falk <oliver@linux-kernel.at>

* Wed Jul 20 2005 John Ellson <ellson@research.att.com>
- release 2.4
