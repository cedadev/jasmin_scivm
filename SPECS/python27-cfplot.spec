%define pname cf-plot
Summary: Climate plots in Python
Name: python27-%{pname}
Version: 2.1.75
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Andy Heaps <a.j.heaps@reading.ac.uk>
Url: http://ajheaps.github.io/cf-plot/
Packager: Andy Heaps <a.j.heaps@reading.ac.uk> and Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-cf
BuildRequires: python27 python27-cf
Obsoletes: python27-cfplot
Provides: python27-cfplot

%description
=====
cfplot
=====

cfplot is a set of Python plotting routines for contour/vector plots that climate
researchers commonly make.  


Documentation
=============
Please refer to the cfplot homepage http://ajheaps.github.io/cf-plot/


%prep
%setup -n cf-plot-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 2.1.75-1.ceda
- bump version

* Thu Oct  5 2017  <builderdev@builder.jc.rl.ac.uk> - 2.1.51-1.ceda
- bump version

* Wed Jul  5 2017  <builderdev@builder.jc.rl.ac.uk> - 2.1.35-1.ceda
- upgrade to 2.1.35
- change URL
- change package name to include hyphen (python27-cf-plot), and obsolete python27-cfplot
   (also "provides" python27-cfplot, so that can be updated with existing cfview)

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.9.10-1.ceda
- upgrade to 1.9.10

* Mon Nov 30 2015  <a.j.heaps@reading.ac.uk> - 1.7.22-1.ceda
- upgrade to 1.7.22

* Tue Nov 17 2015  <a.j.heaps@reading.ac.uk> - 1.7.16-1.ceda
- upgrade to 1.7.16

* Thu Feb 20 2014  <builderdev@builder.jc.rl.ac.uk> - 1.2-%{release}
- initial version; not tagged in git so source is just based on commit ID although contains a version number in setup.py

%files -f INSTALLED_FILES
%defattr(-,root,root)
