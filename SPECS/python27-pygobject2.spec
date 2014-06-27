#%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define python_sitearch /usr/lib/python2.7/site-packages

# Last updated for version 2.20.0
%define glib2_version                  2.16.0
%define python2_version                2.3.5

# XXX Disable this and use "make <my-real-arch>" instead of
#     "make local" when building locally to avoid avoid the
#     "Arch dependent binaries in noarch package" error.
#     Added in Fedora 11, hopefully only temporarily.
%define noarch_docs 0

### Abstract ###

Name: python27-pygobject2
Version: 2.20.0
Release: 1.ceda%{?dist}
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for GObject
URL: http://www.pygtk.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source: http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.20/pygobject-%{version}.tar.bz2
# Don't build girepository module, which was removed upstream subsequent to 2.20
# https://bugzilla.redhat.com/show_bug.cgi?id=555583
Patch1: pygobject-2.20-no-gobject-introspection.patch

### Build Dependencies ###

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libtool
BuildRequires: python27

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package codegen
Summary: The code generation program for PyGObject
Group: Development/Languages

%description codegen
The package contains the C code generation program for PyGObject.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains files required to build wrappers for %{name}-based
libraries such as pygtk2.

%package doc
Summary: Documentation files for %{name}
Group: Development/Languages
%if %{noarch_docs}
BuildArch: noarch
%endif

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n pygobject-%{version}
%patch1 -p1 -b .no-gobject-introspection

%build
# For pygobject-2.20-no-gobject-introspection.patch
export PYTHON=python2.7
autoreconf

%configure --enable-thread
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
make LIBTOOL=/usr/bin/libtool DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

rm examples/Makefile*

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README
%doc examples

%{_libdir}/libpyglib-2.0-python2.7.so*
%dir %{python_sitearch}/gtk-2.0
%{python_sitearch}/gtk-2.0/dsextras.*
%{python_sitearch}/pygtk.*

%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gio
%{python_sitearch}/gtk-2.0/glib
%{python_sitearch}/gtk-2.0/gobject

%files codegen
%defattr(-,root,root,-)
%{_bindir}/pygobject-codegen-2.0
%dir %{_datadir}/pygobject/2.0
%{_datadir}/pygobject/2.0/codegen

%files devel
%defattr(-,root,root,-)
%dir %{_datadir}/pygobject
%dir %{_includedir}/pygtk-2.0
%{_datadir}/pygobject/2.0/defs
%{_includedir}/pygtk-2.0/pyglib.h
%{_includedir}/pygtk-2.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-2.0.pc

%files doc
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/pygobject
%{_datadir}/pygobject/xsl

%changelog
* Fri Jun 27 2014  <builderdev@builder.jc.rl.ac.uk> - 2.20.0-1.ceda
- change to python 2.7

* Wed Jun 23 2010 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-5.el6
- Spec file cleanups.

* Thu Jan 14 2010 Owen Taylor <otaylor@redhat.com> - 2.20.0-4.el6
- Build without gobject-introspection support, the form of support
  in 2.20 was subsequently removed upstream.
  Resolves: rhbz 555583

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-2.el6
- Provide a complete URI for the Source field.

* Wed Sep 23 2009 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-1.fc12
- Update to 2.20.0

* Tue Aug 11 2009 Matthew Barnes <mbarnes@redhat.com> - 2.19.0-1.fc12
- Update to 2.19.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Matthew Barnes <mbarnes@redhat.com> - 2.18.0-1.fc12
- Update to 2.18.0

* Thu Apr 30 2009 Matthew Barnes <mbarnes@redhat.com> - 2.17.1-1.fc12
- Update to 2.17.0
- Remove patch for GNOME bug #566571 (fixed upstream).

* Wed Apr 22 2009 Matthew Barnes <mbarnes@redhat.com> - 2.16.1-4.fc11
- Add patch for GNOME bug #566571 (classic vs new-style inheritance crash).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.16.1-2
- Make -doc noarch

* Sun Feb 22 2009 - Matthew Barnes <mbarnes@redhat.com> - 2.16.1-1.fc11
- Update to 2.16.1

* Sun Jan 04 2009 - Matthew Barnes <mbarnes@redhat.com> - 2.16.0-1.fc11
- Update to 2.16.0
- Remove patch for RH bug #457502 (fixed upstream).
- Remove patch for GNOME bug #551059 and #551212 (fixed upstream).

* Sat Nov 29 2008 - Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.15.4-4
- Rebuild for Python 2.6

* Tue Oct 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.15.4-3.fc10
- Add patch to fix typos breaking compilation

* Tue Oct 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.15.4-2.fc10
- Add 2-liner fixing the load_contents functions not working appropriately

* Wed Sep 03 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.4-1.fc10
- Update to 2.15.4

* Sun Aug 31 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.3-1.fc10
- Update to 2.15.3

* Tue Aug 12 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-3.fc10
- Modify thread initialization patch to fix RH bug #458522.

* Thu Aug 07 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-2.fc10
- Add patch for RH bug #457502 (error on gtk.gdk.threads_init).

* Sat Jul 26 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-1.fc10
- Update to 2.15.2

* Sun Jul 20 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-2.fc10
- Fix directory ownership.  (RH bug #455974, patch by Robert Scheck).

* Wed Jul 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-1.fc10
- Update to 2.15.1
- Bump glib2_version to 2.16.0.
- Remove ancient automake_version.
- Add a pygobject2-codegen subpackage.

* Fri May 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-1.fc10
- Update to 2.14.2

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.1-2.fc9
- Rebuild with GCC 4.3

* Thu Jan 03 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.1-1.fc9
- Update to 2.14.1

* Fri Oct 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.0-2.fc9
- Remove redundant requirements.
- Use name tag where appropriate.

* Sun Sep 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.0-1.fc8
- Update to 2.14.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.13.2-3
- Rebuild for selinux ppc32 issue.

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.13.2-2
- Update the license field

* Sat Jul 07 2007 Matthew Barnes <mbarnes@redhat.com> - 2.13.2-1.fc8
- Update to 2.13.2

* Fri May 18 2007 Matthew Barnes <mbarnes@redhat.com> - 2.13.1-1.fc8
- Update to 2.13.1
- Remove patch for RH bug #237179 (fixed upstream).

* Thu May 03 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-5.fc7
- Fix devel subpackage dependency (RH bug #238793).

* Thu Apr 19 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-3.fc7
- Add patch for RH bug #237179 (memory leak).

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.12.3-2
- rebuild against python 2.5

* Sat Nov 18 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-1.fc7
- Update to 2.12.3

* Thu Oct 26 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-3.fc7
- Add subpackage pygobject2-doc (bug #205231).

* Tue Oct 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-2.fc7
- Use python_sitearch instead of python_sitelib.

* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-1.fc7
- Update to 2.12.2

* Sun Sep 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-3.fc6
- Require glib2-devel for the -devel package.

* Fri Sep 22 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-2.fc6
- Define a python_sitelib macro for files under site_packages.
- Spec file cleanups.

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1.fc6
- Update to 2.12.1
- Require pkgconfig for the -devel package

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.4-1.fc6
- Update to 2.11.4
- Use pre-built docs

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.3-1.fc6
- Update to 2.11.3

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-2.fc6
- BR libxslt

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-1.fc6
- Update to 2.11.2

* Wed Jul 19 2006 Jesse Keating <jkeating@redhat.com> - 2.11.0-2
- rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Update to 2.11.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.10.1-3
- rebuild
- Add missing br libtool

* Fri May 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-2
- Cleanup

* Fri May 12 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-1
- Initial package
