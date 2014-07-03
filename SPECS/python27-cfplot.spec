%define pname cfplot
Summary: Climate plots in Python
Name: python27-%{pname}
Version: 1.2
%define gitsha 22374c7
Release: 1.ceda%{?dist}
Source0: %{pname}-%{gitsha}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Andy Heaps <a.j.heaps@reading.ac.uk>
Url: http://climate.ncas.ac.uk/~andy/cfplot_sphinx/_build/html
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-cf
BuildRequires: python27 python27-cf

%description
=====
cfplot
=====

cfplot is a set of Python plotting routines for contour/vector plots that climate
researchers commonly make.  


Documentation
=============
Please refer to the cfplot homepage http://climate.ncas.ac.uk/~andy/cfplot_sphinx/_build/html




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

* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 1.2-%{release}
- initial version; not tagged in git so source is just based on commit ID although contains a version number in setup.py

%files -f INSTALLED_FILES
%defattr(-,root,root)
