%define pname setuptools
Summary: Easily download, build, install, upgrade, and uninstall Python packages
Name: python27-%{pname}
Version: 18.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: PSF or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Python Packaging Authority <distutils-sig@python.org>
Url: https://bitbucket.org/pypa/setuptools
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects, where packaging includes:

        Python package and module definitions
        Distribution package metadata
        Test hooks
        Project installation
        Platform-specific details
        Python 3 support

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# suppress the easy_install executable without 2.7 in filename because we want
# to keep the RedHat RPM that provides that path with 2.6
rm $RPM_BUILD_ROOT/usr/bin/easy_install
perl -n -l -i -e 'print unless $_ eq "/usr/bin/easy_install"' INSTALLED_FILES

# and one of the files has a space in it... put them all in quotes
perl -n -l -i -e 'print "\"$_\""' INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 18.2-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
