%define pname filelock
Summary: A platform independent file lock.
Name: python27-%{pname}
Version: 3.0.4
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Benedikt Schmitt <benedikt@benediktschmitt.de>
Url: https://github.com/benediktschmitt/py-filelock
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

This package contains a single module, which implements a platform
independent file lock in Python, which provides a simple way of
inter-process communication:

    from filelock import Timeout, FileLock

    lock = FileLock("high_ground.txt.lock")
    with lock:
        open("high_ground.txt", "a").write("You were the chosen one.")

**Don't use** a *FileLock* to lock the file you want to write to,
*instead create a separate .lock* file as shown above.


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
