%define pname virtualenv
#%define snapshot 74b1e5b
Summary: Virtual Python Environment builder
Name: python27-%{pname}
Version: 1.10.1
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
#Source0: pypa-virtualenv-1.8.1-6-g%{snapshot}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jannis Leidel, Carl Meyer and Brian Rosner <python-virtualenv@groups.google.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.virtualenv.org
Requires: python27
BuildRequires: python27

%description

virtualenv is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into /usr/lib/python2.7/site-packages (or whatever your platform's standard location is), it's easy to end up in a situation where you unintentionally upgrade an application that shouldn't be upgraded.

Or more generally, what if you want to install an application and leave it be? If an application works, any change in its libraries or the versions of those libraries can break the application.

Also, what if you can't install packages into the global site-packages directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that has its own installation directories, that doesn't share libraries with other virtualenv environments (and optionally doesn't access the globally installed libraries either).

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# # put unversioned virtualenv exe in /usr/local/bin, where it is less likely to
# # conflict with python-virtualenv for system python (2.6)
# exe_path=/usr/local/bin/virtualenv
# local_exe_path=$RPM_BUILD_ROOT$exe_path
# tmp_filelist=INSTALLED_FILES.new
# mkdir -p `dirname $local_exe_path`
# mv $RPM_BUILD_ROOT%{_bindir}/virtualenv $local_exe_path
# egrep -v "^%{_bindir}/virtualenv$" INSTALLED_FILES > $tmp_filelist
# echo $exe_path >> $tmp_filelist
# mv $tmp_filelist INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Thu Feb  6 2014  <builderdev@builder.jc.rl.ac.uk> - 1.10.1-2.ceda
- comment out renaming of executable

* Tue Sep  3 2013  <builderdev@builder.jc.rl.ac.uk> - 1.10.1-1.ceda
- upgrade to 1.10.1 and put exe in /usr/local

%files -f INSTALLED_FILES
%defattr(-,root,root)
