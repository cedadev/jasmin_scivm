%define pname six
Summary: Python 2 and 3 compatibility utilities
Name: python27-%{pname}
Version: 1.5.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: Benjamin Peterson <benjamin@python.org>
Url: http://pypi.python.org/pypi/six/
Requires: python27
BuildRequires: python27

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports every Python version since 2.5.  It is contained in only one Python
file, so it can be easily copied into your project. (The copyright and license
notice must be retained.)

Online documentation is at http://pythonhosted.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also be
found there.

For questions about six or porting in general, email the python-porting mailing
list: http://mail.python.org/mailman/listinfo/python-porting


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
