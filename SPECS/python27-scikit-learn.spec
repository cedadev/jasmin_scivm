%define pname scikit-learn
Summary: A set of python modules for machine learning and data mining
Name: python27-%{pname}
Version: 0.17b1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: new BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andreas Mueller <amueller@ais.uni-bonn.de>
Url: http://scikit-learn.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27, python27-numpy >= 1.6.1, python27-scipy >= 0.9
BuildRequires: python27, python27-numpy >= 1.6.1, python27-scipy >= 0.9

%description

scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

The project was started in 2007 by David Cournapeau as a Google Summer
of Code project, and since then many volunteers have contributed. See
the AUTHORS.rst file for a complete list of contributors.

It is currently maintained by a team of volunteers.

**Note** `scikit-learn` was previously referred to as `scikits.learn`.


Important links
===============

- Official source code repo: https://github.com/scikit-learn/scikit-learn
- HTML documentation (stable release): http://scikit-learn.org
- HTML documentation (development version): http://scikit-learn.org/dev/
- Download releases: http://sourceforge.net/projects/scikit-learn/files/
- Issue tracker: https://github.com/scikit-learn/scikit-learn/issues
- Mailing list: https://lists.sourceforge.net/lists/listinfo/scikit-learn-general
- IRC channel: ``#scikit-learn`` at ``irc.freenode.net``

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
