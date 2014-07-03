%global pybasever 2.7

Summary: An interpreted, interactive, object-oriented programming language
Name: python27
Version: 2.7.3
Release: 3.ceda%{?dist}
License: Python
Group: Development/Languages
Provides: python-abi = %{pybasever}
Provides: python(abi) = %{pybasever}
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
URL: http://www.python.org/
AutoReq: no
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that need
a programmable interface. This package contains most of the standard
Python modules, as well as modules for interfacing to the Tix widget
set for Tk and RPM.

(This package contains everything for python 2.7, not separated 
into devel, doc etc.)


%prep
%setup -q -n Python-%{version}

%build
# %configure
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC"
./configure --prefix=/usr --enable-shared

make

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT

chmod u+w $RPM_BUILD_ROOT/usr/lib/libpython%{pybasever}.so.*

# delete/rename unversioned stuff that may conflict with system python
cd $RPM_BUILD_ROOT%{_bindir}
for i in 2to3 idle pydoc smtpd.py ; do mv $i $i-%{pybasever} ; done
rm -f python python2 python-config python2-config
rm -f $RPM_BUILD_ROOT/usr/lib/pkgconfig/python.pc
rm -f $RPM_BUILD_ROOT/usr/lib/pkgconfig/python2.pc

%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%files
%defattr(-, root, root, -)
%{_bindir}/*
%doc %{_mandir}/man1/python%{pybasever}.1.gz
/usr/include/python%{pybasever}
/usr/lib/python%{pybasever}
/usr/lib/pkgconfig/python-%{pybasever}.pc
/usr/lib/libpython%{pybasever}.so*

%changelog

* Fri Feb 21 2014  <builderdev@builder.jc.rl.ac.uk> - 2.7.3-2.ceda
- change from static to shared libs (--enable-shared and adjust %files)

* Thu Oct 17 2013  <builderdev@builder.jc.rl.ac.uk> - 2.7.3-1.ceda
- add PIC

* Sun Dec  9 2012 Alan Iwi <alan.iwi@stfc.ac.uk> - 2.7.3.1.ceda
- a simple-ish RPM with just the vanilla build and no separation into devel etc
