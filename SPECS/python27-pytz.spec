%define pname pytz
Summary: World timezone definitions, modern and historical
Name: python27-%{pname}
Version: 2016.10
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Stuart Bishop <stuart@stuartbishop.net>
Url: http://pythonhosted.org/pytz
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4
or higher. It also solves the issue of ambiguous times at the end
of daylight saving time, which you can read more about in the Python
Library Reference (``datetime.tzinfo``).

Almost all of the Olson timezones are supported.

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
