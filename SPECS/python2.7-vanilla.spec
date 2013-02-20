%global pybasever 2.7

Summary: An interpreted, interactive, object-oriented programming language
Name: python27
Version: 2.7.3
Release: 1.ceda%{?dist}
License: Python
Group: Development/Languages
Provides: python-abi = %{pybasever}
Provides: python(abi) = %{pybasever}
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
URL: http://www.python.org/
AutoReq: no

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
./configure --prefix=/usr

make

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT

chmod u+w $RPM_BUILD_ROOT/usr/lib/libpython%{pybasever}.a

# delete/rename unversioned stuff that may conflict with system python
cd $RPM_BUILD_ROOT%{_bindir}
for i in 2to3 idle pydoc smtpd.py ; do mv $i $i-%{pybasever} ; done
rm -f python python2 python-config python2-config
rm -f $RPM_BUILD_ROOT/usr/lib/pkgconfig/python.pc
rm -f $RPM_BUILD_ROOT/usr/lib/pkgconfig/python2.pc

%files
%defattr(-, root, root, -)
%{_bindir}/*
%doc %{_mandir}/man1/python%{pybasever}.1.gz
/usr/include/python%{pybasever}
/usr/lib/python%{pybasever}
/usr/lib/pkgconfig/python-%{pybasever}.pc
/usr/lib/libpython%{pybasever}.a
#/usr/lib64/python%{pybasever}
#/usr/lib64/pkgconfig/python-%{pybasever}.pc
#/usr/lib64/libpython%{pybasever}.a

%changelog
* Sun Dec  9 2012 Alan Iwi <alan.iwi@stfc.ac.uk> - 2.7.3.1.ceda
- a simple-ish RPM with just the vanilla build and no separation into devel etc