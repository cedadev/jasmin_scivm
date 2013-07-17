%global pybasever 2.4

Summary: An old unsupported Python version
Name: python24
Version: 2.4.6
Release: 1.ceda%{?dist}
License: Python
Group: Development/Languages
Provides: python-abi = %{pybasever}
Provides: python(abi) = %{pybasever}
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
URL: http://www.python.org/
AutoReq: no

%description
Python 2.4 basic package, for use on JASMIN without support.
Please use 2.7 for supported version.

%prep
%setup -q -n Python-%{version}

%build
./configure --prefix=/usr
make

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT

# delete/rename unversioned stuff that may conflict with system python
cd $RPM_BUILD_ROOT%{_bindir}
for i in idle pydoc smtpd.py ; do mv $i $i-%{pybasever} ; done
rm -f python
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT/usr/man/man1/python.1 $RPM_BUILD_ROOT%{_mandir}/man1/python%{pybasever}.1 
gzip $RPM_BUILD_ROOT%{_mandir}/man1/python%{pybasever}.1 

%files
%defattr(-, root, root, -)
%{_bindir}/*
%doc %{_mandir}/man1/python%{pybasever}.1.gz
/usr/include/python%{pybasever}
/usr/lib/python%{pybasever}

%changelog
* Mon Apr 29 2013  <builderdev@builder.jc.rl.ac.uk> - 2.4.6-1.ceda
- change to 2.4

* Sun Dec  9 2012 Alan Iwi <alan.iwi@stfc.ac.uk> - 2.7.3.1.ceda
- a simple-ish RPM with just the vanilla build and no separation into devel etc
