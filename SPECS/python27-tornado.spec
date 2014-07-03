%define pname tornado
Summary: Tornado is an open source version of the scalable, non-blocking web server and and tools that power FriendFeed
Name: python27-%{pname}
Version: 3.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: http://www.apache.org/licenses/LICENSE-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
#BuildArch: noarch
Vendor: Facebook <python-tornado@googlegroups.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.tornadoweb.org/
Requires: python27
BuildRequires: python27

%description
UNKNOWN

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Apr 28 2014  <builderdev@builder.jc.rl.ac.uk> - 3.2-1.ceda
- upgrade to 3.2

%files -f INSTALLED_FILES
%defattr(-,root,root)
