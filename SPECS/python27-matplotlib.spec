%define pname matplotlib
Summary: Python plotting package
Name: python27-%{pname}
Version: 2.2.2
# see matplotlibrc below when upgrading to >=1.5
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: John D. Hunter <jdh2358@gmail.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://matplotlib.sourceforge.net
Requires: python27 python27-dateutil python27-pyparsing python27-cycler python27-kiwisolver python27-backports-functools_lru_cache
BuildRequires: python27

%description

      matplotlib strives to produce publication quality 2D graphics
      for interactive graphing, scientific publishing, user interface
      development and web application servers targeting multiple user
      interfaces and hardcopy output formats.  There is a 'pylab' mode
      which emulates matlab graphics
      

%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# temporary fix to matplotlibrc - should apparently be able to remove once 
# 1.5.0 released - per https://github.com/matplotlib/matplotlib/issues/4883
#perl -p -i -e 's/^(backend\s*:).*$/$1 TkAgg/' $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 2.2.2-2.ceda
- added RPM dependencies

* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 2.2.2-1.ceda
- bump version

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 1.5.3-1.ceda
- update to 1.5.3

* Sun Aug 23 2015  <builderdev@builder.jc.rl.ac.uk> - 1.4.3-1.ceda
- upgrade to 1.4.3. Add requires python27-dateutil python27-pyparsing. Force TkAgg backend.

%files -f INSTALLED_FILES
%defattr(-,root,root)
