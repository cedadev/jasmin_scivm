%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Last updated for version 2.15.0
%define glib2_version		2.8.0
%define pango_version		1.16.0
%define gtk2_version		2.9.0
%define libglade2_version	2.5.0
%define pycairo_version		1.0.2
%define pygobject2_version	2.16.1
%define python2_version		2.3.5

%define buildglade %(pkg-config libglade-2.0 && echo 1 || echo 0)

### Abstract ###

Name: pygtk2
Version: 2.16.0
Release: 3%{?dist}
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for GTK+
URL: http://www.pygtk.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source: http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.16/pygtk-%{version}.tar.bz2

### Patches ###

# RH bug #208608
Patch0: pygtk-nodisplay-exception.patch

### Dependencies ###

# Leave these requirements alone!  RPM isn't smart enough
# to derive these from the build requirements below.
Requires: pycairo
Requires: pygobject2

### Build Dependencies ###

BuildRequires: automake
BuildRequires: docbook-style-xsl
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libglade2-devel >= %{libglade2_version}
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: numpy
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: pycairo-devel >= %{pycairo_version}
BuildRequires: pygobject2-devel >= %{pygobject2_version}
BuildRequires: python2-devel >= %{python2_version}

%description
PyGTK is an extension module for Python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in Python with PyGTK (within reason), but with all the benefits of using a
high-level scripting language.

%package codegen
Summary: The code generation program for PyGTK
Group: Development/Languages

%description codegen
This package contains the C code generation program for PyGTK.

%package libglade
Summary: A wrapper for the libglade library for use with PyGTK
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description libglade
This module contains a wrapper for the libglade library.  Libglade allows
a program to construct its user interface from an XML description, which
allows the programmer to keep the UI and program logic separate.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: pkgconfig
Requires: pycairo-devel
Requires: pygobject2-devel

%description devel
This package contains files required to build wrappers for GTK+ add-on
libraries so that they interoperate with pygtk.

%package doc
Summary: Documentation files for %{name}
Group: Development/Languages
BuildArch: noarch

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n pygtk-%{version}
%patch0 -p1

%build
%configure --enable-thread --enable-numpy
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
make LIBTOOL=/usr/bin/libtool DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README MAPPING COPYING
%doc examples
%dir %{python_sitearch}/gtk-2.0
%dir %{python_sitearch}/gtk-2.0/gtk
%{python_sitearch}/gtk-2.0/gtk/*.py*
%dir %{_libdir}/pygtk
%dir %{_libdir}/pygtk/2.0
%{_libdir}/pygtk/2.0/*

%defattr(755, root, root, 755)
%{_bindir}/pygtk-demo
%{python_sitearch}/gtk-2.0/atk.so
%{python_sitearch}/gtk-2.0/pango.so
%{python_sitearch}/gtk-2.0/gtk/_gtk.so
%{python_sitearch}/gtk-2.0/gtkunixprint.so
%{python_sitearch}/gtk-2.0/pangocairo.so

%if %{buildglade}
%files libglade
%defattr(755, root, root, 755)
%{python_sitearch}/gtk-2.0/gtk/glade.so
%endif

%files codegen
%defattr(755, root, root, 755)
%{_prefix}/bin/pygtk-codegen-2.0

%files devel
%defattr(644, root, root, 755)
%dir %{_prefix}/include/pygtk-2.0
%dir %{_prefix}/include/pygtk-2.0/pygtk
%{_prefix}/include/pygtk-2.0/pygtk/*.h
%{_libdir}/pkgconfig/pygtk-2.0.pc
%dir %{_prefix}/share/pygtk
%dir %{_prefix}/share/pygtk/2.0
%dir %{_prefix}/share/pygtk/2.0/defs
%{_prefix}/share/pygtk/2.0/defs/*.defs
%{_prefix}/share/pygtk/2.0/defs/pangocairo.override

%files doc
%defattr(644, root, root, 755)
%{_datadir}/gtk-doc/html/pygtk

%changelog
* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.16.0-3.el6
- Remove patch for RH bug #379051 (fixed upstream, differently).

* Fri Jan 02 2010 Matthew Barnes <mbarnes@redhat.com> - 2.16.0-2.fc12
- Fix the major version number in the Source URI.

* Sun Aug 23 2009 Matthew Barnes <mbarnes@redhat.com> - 2.16.0-1.fc12
- Update to 2.16.0
- Remove patch for RH bug #511082 (fixed upstream).

* Tue Aug 18 2009 Adam Jackson <ajax@redhat.com> 2.15.2-4
- Drop the explicit Requires: numpy as per new packaging guidelines.  If
  your app calls gtk.gdk.get_pixels_array() you need to pull numpy in
  yourself.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-2.fc12
- Add patch for RH bug #511082 (missing gtk-2.16-types.defs).

* Sun Jun 21 2009 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-1.fc12
- Update to 2.15.2

* Tue Jun 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-2.fc12
- Require numpy instead of python-numeric (RH bug #503691).

* Mon May 25 2009 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-1.fc12
- Update to 2.15.1

* Sat May 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.15.0-1.fc12
- Update to 2.15.0
- Bump pygobject2_version to 2.16.1.

* Fri Mar 06 2009 Matthew Barnes <mbarnes@redhat.com> - 2.14.1-1.fc11
- Update to 2.14.1
- Bump gtk2_version to 2.9.0 for gtkunixprint requirement.

* Tue Feb 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.14.0-2
- Make -doc noarch

* Sat Jan 31 2009 Matthew Barnes <mbarnes@redhat.com> - 2.14.0-1.fc11
- Update to 2.14.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.13.0-3
- Rebuild for Python 2.6

* Tue Aug 26 2008 Matthew Barnes <mbarnes@redhat.com> - 2.13.0-2.fc10
- Restore pycairo and pygobject2 requirements, with a note to myself
  to stop screwing around with them (RH bug #460105).

* Mon Aug 25 2008 Matthew Barnes <mbarnes@redhat.com> - 2.13.0-1.fc10
- Update to 2.13.0
- Update version requirements.

* Mon Mar 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-6.fc9
- Add patch for RH bug #379051 (keyboard events in cell renderer).

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-5.fc9
- Rebuild with GCC 4.3

* Wed Feb 06 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-4.fc9
- Use a full URL for the source tag (RH bug #226333).

* Thu Jan 24 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-3.fc9
- Documentation files should not be executable (RH bug #430093).

* Mon Jan 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-2.fc9
- Update package description to match suggestions from Content Services.

* Thu Jan 03 2008 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-1.fc9
- Update to 2.12.1
- Remove patch for RH bug #217430 (fixed upstream).
- Remove patch for GNOME bug #479012 (fixed upstream).

* Fri Oct 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.0-3.fc8
- Add subpackage pygtk2-doc to avoid multilib conflicts.

* Fri Sep 21 2007 Jeremy Katz <katzj@redhat.com> - 2.12.0-2.fc8
- fix crash using TreeView.convert_widget_to_bin_window_coords

* Sun Sep 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.0-1.fc8
- Update to 2.12.0

* Mon Aug 27 2007 Matthew Barnes <mbarnes@redhat.com> - 2.11.0-1.fc8
- Update to 2.11.0

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.10.6-2
- Update the license field

* Tue Jul 10 2007 Matthew Barnes <mbarnes@redhat.com> - 2.10.6-1.fc8
- Update to 2.10.6

* Mon Jul 09 2007 Matthew Barnes <mbarnes@redhat.com> - 2.10.5-1.fc8
- Update to 2.10.5

* Tue Apr 17 2007 Matthew Barnes <mbarnes@redhat.com> - 2.10.4-2.fc7
- Make pygtk-demo executable (RH bug #236716).

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.10.4-1.fc7
- Update to 2.10.4

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-8.fc7
- Rename spec file to pygtk2.spec (RH bug #226333).

* Sat Dec 30 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-7.fc7
- Add Requires pkgconfig to devel subpackage.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.10.3-6
- rebuild for python 2.5

* Mon Nov 27 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-5.fc7
- Add patch for RH bug #217430 (missing gtk-extrafuncs.defs).

* Thu Oct 26 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-4.fc7
- Require pygtk2-codegen = %%{version}-%%{release} in devel.

* Thu Oct 26 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-3.fc7
- Add subpackage pygtk2-codegen (bug #212287).

* Tue Oct 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-2.fc7
- Oops, try using python_sitearch instead of python_sitelib.

* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.10.3-1.fc7
- Update to 2.10.3
- Spec file cleanups.
- Define a python_sitelib macro for files under site_packages.

* Mon Oct  2 2006 Jeremy Katz <katzj@redhat.com> - 2.10.1-4
- go back to raising an exception when importing gtk fails (#208608)

* Tue Sep  5 2006 Ray Strode <rstrode@redhat.com> - 2.10.1-3.fc6
- drop crazy reload hack patch, since it's been fixed by jdahlin
  upstream in a better way.

* Tue Sep  5 2006 Ray Strode <rstrode@redhat.com> - 2.10.1-2.fc6
- drop some old patches

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.10.1-1.fc6
- Update to 2.10.1

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.6-2.fc6
- Include docs 

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.6-1.fc6
- Update to 2.9.6

* Fri Jul 28 2006 Alexander Larsson <alexl@redhat.com> - 2.9.3-3
- Make sure reloading the gtk module works
- Fixes system-config-display (#199629)

* Wed Jul 19 2006 Chris Lumens <clumens@redhat.com> 2.9.3-2
- Revert to previous behavior of raising an error if $DISPLAY cannot be
  opened.

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.3-1
- Update to 2.9.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.9.2-1.1
- rebuild

* Thu Jun 22 2006 Jeremy Katz <katzj@redhat.com> - 2.9.2-1
- update to 2.9.2
- fix for gtk+ 2.9.4 API changes

* Thu Jun 15 2006 Ray Strode <rstrode@redhat.com> - 2.9.1-3
- Use full include path for defs parser

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.1-2
- Fix missing BuildRequries

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.1-1
- Update to 2.9.1

* Fri May 26 2006 Jeremy Katz <katzj@redhat.com> - 2.9.0-3
- BR should be pygobject2-devel, need to actually require pygobject2 at runtime

* Thu May 25 2006 John (J5) Palmieri <johnp@redhat.com> - 2.9.0-2
- Add BR for pygobject2
- Take out files now packaged in pygobject2 from the files list

* Wed May 10 2006 Matthias Clasem <mclasen@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Thu Apr 20 2006 John (J5) Palmieri <johnp@redhat.com> - 2.8.6-1
- Update to upstream 2.8.6

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.8.4-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Jan 15 2006 Christopher Aillon <caillon@redhat.com> - 2.8.4-1
- Bump to upstream 2.8.4

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 2.8.2-2
- Add the pycairo dependency since pycairo is now built in rawhide

* Mon Oct 24 2005 Christopher Aillon <caillon@redhat.com> - 2.8.2-1
- Bump to upstream 2.8.2

* Thu Sep 08 2005 John (J5) Palmieri <johnp@redhat.com> - 2.8.0-1
- Bump to upstream 2.8.0

* Tue Aug 23 2005 John (J5) Palmieri <johnp@redhat.com> - 2.7.3-3
- Add a BuildRequires on python-numeric so that Numeric
  python support is added
- Add a Requires on python-numeric as well

* Tue Aug 18 2005 John (J5) Palmieri <johnp@redhat.com> - 2.7.3-2
- Bump and rebuild for cairo ABI changes

* Wed Aug 10 2005  <jrb@redhat.com> - 2.7.3-1
- Update to 2.7.3

* Wed Aug 10 2005  <jrb@redhat.com> - 2.7.2-1
- Update to 2.7.2

* Wed Jul 27 2005 Mark McLoughlin <markmc@redhat.com> 2.7.1-1
- Update to 2.7.1

* Mon Jul 18 2005 John (J5) Palmieri <johnp@redhat.com> - 2.7.0-1
- Update to upstream 2.7.0

* Wed Jul  6 2005 John (J5) Palmieri <johnp@redhat.com> - 2.6.2-1
- update to upstream 2.6.2
- remove gcc4 patch as it is in updated tarball

* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 2.6.0-2
- fix build with gcc4
- add pygtk-demo

* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 2.6.0-1
- 2.6.0

* Thu Feb 10 2005 Mark McLoughlin <markmc@redhat.com> - 2.5.3-3
- Avoid assertion errors in signal handling patch

* Wed Feb  9 2005 Mark McLoughlin <markmc@redhat.com> - 2.5.3-2
- Backport fix for gnome #154779 - python signal handlers weren't
  getting executed while gobject.MainLoop was running

* Tue Jan 25 2005 Jeremy Katz <katzj@redhat.com> - 2.5.3-1
- 2.5.3

* Thu Jan 20 2005  <jrb@redhat.com> - 2.5.1-1
- New version

* Fri Nov 26 2004 Florian La Roche <laroche@redhat.com>
- add a %%clean target

* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 2.4.1-1
- update to 2.4.1

* Mon Oct  4 2004 GNOME <jrb@redhat.com> - 2.4.0-1
- new version

* Tue Aug 10 2004 Jonathan Blandford <jrb@redhat.com> 2.3.96-2
- cleaner lib64 patch

* Tue Aug 10 2004 Jonathan Blandford <jrb@redhat.com> 2.3.96-1
- move pythondir into /usr/lib64/

* Mon Aug  9 2004 Jonathan Blandford <jrb@redhat.com> 2.3.96-1
- new version

* Tue Aug  3 2004 Jeremy Katz <katzj@redhat.com> - 2.3.95-1
- update to 2.3.95

* Thu Jun 17 2004 Jeremy Katz <katzj@redhat.com> - 2.3.92-1
- update to 2.3.92

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Mar 11 2004 Jeremy Katz <katzj@redhat.com> - 2.2.0-1
- 2.2.0

* Wed Mar 10 2004 Jeremy Katz <katzj@redhat.com> 2.2.0-0.rc1
- 2.2.0 RC1

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 17 2004 Jeremy Katz <katzj@redhat.com> - 2.0.0-5
- GtkTextSearchFlags is flags, not enum (#114910)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Jeremy Katz <katzj@redhat.com> - 2.0.0-3
- own %%{_libdir}/python?.?/site-packages/gtk-2.0/gtk dir (#113048)

* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-2
- rebuild for python 2.3

* Thu Sep  4 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-1
- 2.0.0

* Thu Aug 14 2003 Elliot Lee <sopwith@redhat.com> 1.99.17-1
- Update to latest version
- Module filenames changed from foomodule.so to foo.so

* Thu Aug  7 2003 Elliot Lee <sopwith@redhat.com> 1.99.16-10
- Fix libtool

* Fri Jul 18 2003 Jeremy Katz <katzj@redhat.com> 1.99.16-8
- part of the fixnew patch wasn't applied upstream, apply it (#99400)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 27 2003 Jonathan Blandford <jrb@redhat.com> 1.99.16-5
- Update compat patch to include gtk_text_buffer_set_text

* Tue May 27 2003 Matt Wilson <msw@redhat.com> 1.99.16-4
- don't require the deprecated length parameter

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.99.16-3
- add compatibility for deprecated length field in GtkTextBuffer
  insert methods (#91519)

* Thu May 22 2003 Matt Wilson <msw@redhat.com> 1.99.16-2
- apply atom_intern patch again (#91349)

* Tue May 20 2003 Matt Wilson <msw@redhat.com> 1.99.16-1
- added a compatibility function for gtk.gdk.gc_new() so we won't have
  to fix all our code quite yet

* Mon May 19 2003 Matt Wilson <msw@redhat.com> 1.99.16-1
- enable threads (#83539, #87872)

* Fri Apr 11 2003 Jonathan Blandford <jrb@redhat.com> 1.99.16-1
- new version

* Thu Mar 13 2003 Jeremy Katz <katzj@redhat.com> 1.99.14-7
- and again

* Thu Mar 13 2003 Jeremy Katz <katzj@redhat.com> 1.99.14-6
- rebuild in new environment

* Wed Mar  5 2003 Thomas Woerner <twoerner@redhat.com> 1.99.14-5
- fixed new functions for ListStore, TreeStrore and ProgressBar

* Thu Feb  6 2003 Mihai Ibanescu <misa@redhat.com> 1.99.14-4
- rebuild to use the UCS4-enabled python

* Tue Jan 28 2003 Jeremy Katz <katzj@redhat.com> 1.99.14-3
- rerun auto* to use new python.m4 and work properly with multilib python
- libdir-ize

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 27 2002 Jeremy Katz <katzj@redhat.com> 1.99.14-1
- bump version to 1.99.14
- add patch to up the ref on gtkInvisible instantiation (#80283)

* Thu Dec 12 2002 Jonathan Blandford <jrb@redhat.com>
- bump version to 1.99.13
- backport gdk.Pixbuf.save

* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- rebuild for multilib
- use %%configure

* Fri Aug 30 2002 Matt Wilson <msw@redhat.com>
- fix pixbuf leaks (#72137)
- five more pixbuf leaks plugged

* Wed Aug 28 2002 Jonathan Blandford <jrb@redhat.com>
- remover Packager tag

* Tue Aug 27 2002 Jonathan Blandford <jrb@redhat.com>
- add binding for gdk_atom_intern

* Mon Jul 29 2002 Matt Wilson <msw@redhat.com>
- 0.99.12

* Wed Jul 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Thu Jun 27 2002 Tim Waugh <twaugh@redhat.com>
- Fix bug #65770.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Jeremy Katz <katzj@redhat.com>
- 1.99.10

* Wed Feb 27 2002 Matt Wilson <msw@redhat.com>
- 1.99.8

* Mon Jan 28 2002 Matt Wilson <msw@redhat.com>
- added atkmodule.so to file list

* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- fix devel filelist to match new header location

* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- get the headers from their new version-specific location

* Thu Oct 11 2001 Matt Wilson <msw@redhat.com>
- fixed typo in devel filelist
- added macro that tests to see if we have libglade2, make the
  filelist a condition of that
- changed name to 'pygtk2' to avoid name conflict with pygtk

