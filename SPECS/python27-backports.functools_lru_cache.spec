%define pname backports-functools_lru_cache
Summary: backports.functools_lru_cache
Name: python27-backports-functools_lru_cache
Version: 1.5
Release: 1.ceda%{?dist}
Source0: backports.functools_lru_cache-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Url: https://github.com/jaraco/backports.functools_lru_cache
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-backports-common
BuildRequires: python27
BuildArch: noarch

%description

Backport of functools.lru_cache from Python 3.3 as published at `ActiveState
<http://code.activestate.com/recipes/578078/>`_.

Usage
=====

Consider using this technique for importing the 'lru_cache' function::

    try:
        from functools import lru_cache
    except ImportError:
        from backports.functools_lru_cache import lru_cache




%prep
%setup -n backports.functools_lru_cache-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
perl -n -i -e 'print unless m{/usr/lib/python2.7/site-packages/backports/__init__\.py}' INSTALLED_FILES
rm $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/backports/__init__.py*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 1.5-2.ceda
- add python27-backports-common dependency and remove the __init__.py

* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 1.5-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
