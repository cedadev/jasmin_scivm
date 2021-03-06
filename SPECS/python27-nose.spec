%define pname nose
Summary: nose extends unittest to make testing easier
Name: python27-%{pname}
Version: 1.3.7
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GNU LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jason Pellerin <jpellerin+nose@gmail.com>
Url: http://readthedocs.org/docs/nose/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch
Conflicts: python-nose

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
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%{_mandir}
perl -p -i -e 's,^/usr/man/,/usr/share/man/,; s/$/.gz/ if m{^/usr/share/man/man(.*?)/.*\.\1$}' INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Wed Jul  5 2017  <builderdev@builder.jc.rl.ac.uk> - 1.3.7-1.ceda
- update to 1.3.7


%files -f INSTALLED_FILES
%defattr(-,root,root)
