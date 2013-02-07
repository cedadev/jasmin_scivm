%define pname nose
Summary: nose extends unittest to make testing easier
Name: python-%{pname}
Version: 1.2.0
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GNU LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason Pellerin <jpellerin+nose@gmail.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://readthedocs.org/docs/nose/

%description
nose extends the test loading and running features of unittest, making
    it easier to write, find and run tests.

    By default, nose will run tests in files or directories under the current
    working directory whose names include "test" or "Test" at a word boundary
    (like "test_this" or "functional_test" or "TestClass" but not
    "libtest"). Test output is similar to that of unittest, but also includes
    captured stdout output from failing tests, for easy print-style debugging.

    These features, and many more, are customizable through the use of
    plugins. Plugins included with nose provide support for doctest, code
    coverage and profiling, flexible attribute-based test selection,
    output capture and more. More information about writing plugins may be
    found on in the nose API documentation, here:
    http://readthedocs.org/docs/nose/

    If you have recently reported a bug marked as fixed, or have a craving for
    the very latest, you may want the development version instead:
    https://github.com/nose-devs/nose/tarball/master#egg=nose-dev
    

%prep
%setup -n %{pname}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --install-data=%{_datadir} --record=INSTALLED_FILES

# replace any man pages with .gz version in file list (Alan)
perl -p -i -e 's/$/.gz/ if m{^/usr/share/man/man(.*?)/.*\.\1$}' INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt
