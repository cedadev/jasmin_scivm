%define pname tqdm
Summary: Fast, Extensible Progress Meter
Name: python27-%{pname}
Version: 4.19.9
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MPLv2.0, MIT Licences
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: tqdm developers <python.tqdm@gmail.com>
Url: https://github.com/tqdm/tqdm
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

Instantly make your loops show a smart progress meter - just wrap any
iterable with ``tqdm(iterable)``, and you're done!

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

%files -f INSTALLED_FILES
%defattr(-,root,root)
