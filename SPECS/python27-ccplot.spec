%define pname ccplot
Summary: CloudSat and CALIPSO plotting tool
Name: python27-%{pname}
Version: 1.5.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Peter Kuma <peter.kuma@ccplot.org>
Url: http://www.ccplot.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27 hdf-devel

%description

ccplot is an open source command-line program for
    plotting profile, layer and earth view data sets from CloudSat, CALIPSO
    and Aqua MODIS products.


%prep
%setup -n %{pname}-%{version}

%build
export LDFLAGS="-L/usr/lib64/hdf"
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

* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 1.5.2-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
