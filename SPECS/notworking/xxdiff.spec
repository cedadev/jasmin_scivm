Summary:	Graphical file and directories comparator and merge tool
Name:		xxdiff
Version:	3.2
Release:	12%{?dist}
License:	GPLv2+
Group:		Development/Tools
URL:		http://furius.ca/xxdiff/
# The orginal tar can be found at http://furius.ca/downloads/xxdiff/releases/xxdiff-%{version}.tar.bz2
# We remove the screenshots directory since the images in there can not be redistributed without permission.
Source0:	xxdiff-%{version}-noscreenshots.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	qt-devel, bison, flex

Patch0:		%{name}-fix-cstdlib_h.patch

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
xxdiff is a graphical browser for viewing the differences between two or three
files, or between two directories, and can be used to produce a merged version.

%package tools
Summary: Tools for xxdiff
Group: Development/Tools
URL: http://furius.ca/xxdiff/doc/xxdiff-scripts.html
Requires:	xxdiff
BuildRequires:  python-devel

%description tools
Tools for xxdiff

%prep
%setup -q
%patch0 -p2

%build

CFLAGS="${CFLAGS:-$RPM_OPT_FLAGS}"
CXXFLAGS="${CFLAGS:-$RPM_OPT_FLAGS}"
export CFLAGS
export CXXFLAGS

%{__make} -C src -f Makefile.bootstrap makefile
%{__sed} -i -e "s/^CFLAGS\s*=/CFLAGS +=/g" src/Makefile
%{__sed} -i -e "s/^CXXFLAGS\s*=/CXXFLAGS +=/g" src/Makefile
%{__make} -C src %{?_smp_mflags}
%{__python} setup.py build

find ./build  -name \*.py  -print  -exec %{__sed} -i "1{/^#\!/d}" {} \;

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 bin/xxdiff %{buildroot}%{_bindir}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot} --install-lib=%{python_sitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc index.html
%doc CHANGES COPYING README TODO VERSION
%{_bindir}/xxdiff

%files tools
%defattr(-,root,root,-)
%doc doc index.html
%{python_sitelib}/*
%{_bindir}/svn-foreign
%{_bindir}/xx-cond-replace
%{_bindir}/xx-cvs-diff
%{_bindir}/xx-cvs-revcmp
%{_bindir}/xx-diff-proxy
%{_bindir}/xx-encrypted
%{_bindir}/xx-filter
%{_bindir}/xx-find-grep-sed
%{_bindir}/xx-match
%{_bindir}/xx-pyline
%{_bindir}/xx-rename
%{_bindir}/xx-sql-schemas
%{_bindir}/xx-svn-diff
%{_bindir}/xx-svn-resolve

%changelog
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.2-9
- Rebuild for Python 2.6

* Mon Jun  9 2008 Russell Cattelan <cattelan@thebarn.com> - 3.2-8
- Create a new tar ball without the restricted copyrighted screen shots

* Thu May 29 2008 Russell Cattelan <cattelan@thebarn.com> - 3.2-7
- Remove desktop file, since xxdiff need files at least 2 files specified on
- the cmd line.
- It is confusing to have a menu option that does not work without
- dragging and dropping at least two files.

* Tue May 27 2008 Russell Cattelan <cattelan@thebarn.com> - 3.2-6
- Add desktop file

* Tue May  6 2008 Russell Cattelan <cattelan@thebarn.com> - 3.2-5
- Remove python from the main package Requires.
- Make sure the build picks rpm defined CFLAGS

* Mon Apr 28  2008 Russell Cattelan <cattelan@thebarn.com> 3.2-4
- Split out script into tools package
- Minor changes to build process and python lib handling

* Sun Mar 30  2008 Russell Cattelan <cattelan@thebarn.com> 3.2-3
- Minor fixups based on review comments

* Sat Mar 29  2008 Russell Cattelan <cattelan@thebarn.com> 3.2-2
- Added helper utilites	

* Sat Mar  8  2008 Russell Cattelan <cattelan@thebarn.com> 3.2-1
- Initial Revision
