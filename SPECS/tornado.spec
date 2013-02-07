%define pname tornado
Summary: Tornado is an open source version of the scalable, non-blocking web server and and tools that power FriendFeed
Name: python-%{pname}
Version: 2.4
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: http://www.apache.org/licenses/LICENSE-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Facebook <python-tornado@googlegroups.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.tornadoweb.org/
BuildRequires: python-devel

%description
UNKNOWN

%prep
%setup -n %{pname}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
