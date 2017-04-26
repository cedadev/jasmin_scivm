%define pname psycopg2
Summary: psycopg2 - Python-PostgreSQL Database Adapter
Name: python27-%{pname}
Version: 2.6.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPL with exceptions or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Federico Di Gregorio <fog@initd.org>
Url: http://initd.org/psycopg/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 postgresql
BuildRequires: python27 postgresql-devel

%description

Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of concurrent "INSERT"s or "UPDATE"s.

Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being
both efficient and secure.  It features client-side and server-side cursors,
asynchronous communication and notifications, "COPY TO/COPY FROM" support.
Many Python types are supported out-of-the-box and adapted to matching
PostgreSQL data types; adaptation can be extended and customized thanks to a
flexible objects adaptation system.

Psycopg 2 is both Unicode and Python 3 friendly.


Documentation
-------------

Documentation is included in the 'doc' directory and is `available online`__.

.. __: http://initd.org/psycopg/docs/


%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
