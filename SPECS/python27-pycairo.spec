# %{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define python_sitearch /usr/lib/python2.7/site-packages

%define cairo_version 1.8.6

### Abstract ###

Name: python27-pycairo
Version: 1.8.6
Release: 1.ceda%{?dist}
License: MPLv1.1 or LGPLv2
Group: Development/Languages
Summary: Python bindings for the cairo library
URL: http://cairographics.org/pycairo
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://cairographics.org/releases/pycairo-%{version}.tar.gz

### Build Dependencies ###

BuildRequires: cairo-devel >= %{cairo_version}
BuildRequires: pkgconfig
BuildRequires: python27

%description
Python bindings for the cairo library.

%package devel
Summary: Libraries and headers for pycairo
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: cairo-devel
Requires: pkgconfig
Requires: python27

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with pycairo.

This devel package has identical content to the standard RedHat
pycairo-devel package (as it does not depend on python versions), so
to avoid conflicts it should not be installed if other packages on the
system depend on "pycairo-devel".  The only difference is that the
standard pycairo-devel depends on "pycairo" (i.e. the wrappers for
python 2.6), whereas this one depends on "python27-pycairo" (the
2.7 equivalent).

%prep
%setup -q -n pycairo-%{version}

%build
export PYTHON=python2.7
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README
%doc examples doc/faq.rst doc/overview.rst doc/README
%{python_sitearch}/cairo/

%files devel
%defattr(-,root,root,-)
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc

%changelog
* Fri Jun 27 2014  <builderdev@builder.jc.rl.ac.uk> - 1.8.6-1.ceda
- change to python 2.7

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.8.6-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.6-1
- Update to 1.8.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Tue Dec 16 2008 Matthew Barnes <mbarnes@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.12-5
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.12-4
- fix license tag

* Wed May 07 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-3
- Add more documentation files to the package (RH bug #445519).

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-2.fc9
- Rebuild with GCC 4.3

* Thu Dec 13 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-1.fc9
- Update to 1.4.12
- Bump cairo requirement to 1.4.12.

* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-2.fc7
- Rebuild

* Thu Mar 15 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-1.fc7
- Update to 1.4.0

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-3.fc7
- Incorporate suggestions from package review (RH bug #226329).

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.2.6-2
- rebuild against python 2.5

* Tue Nov 28 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-1.fc7
- Update to 1.2.6
- Clean up the spec file.

* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-1.1
- rebuild

* Wed Jul 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.0-1
- Update to upstream 1.2.0

* Mon Jul  3 2006 Jeremy Katz <katzj@redhat.com> - 1.0.2-3
- require new enough cairo (#197457)

* Mon Jun 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-2
- add pkgconfig BR

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-1
- Updated to latest and push into rawhide

* Fri Dec 10 2004 Kristian Høgsberg <krh@redhat.com> - 0.1.3-1
- Add python-devel build requires.

* Wed Nov 24 2004  <jrb@redhat.com> - 
- Initial build.

