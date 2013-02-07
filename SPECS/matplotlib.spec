%define pname matplotlib
Summary: Python plotting package
Name: python-%{pname}
Version: 1.1.0
Release: 2.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: John D. Hunter <jdh2358@gmail.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://matplotlib.sourceforge.net

%description

      matplotlib strives to produce publication quality 2D graphics
      for interactive graphing, scientific publishing, user interface
      development and web application servers targeting multiple user
      interfaces and hardcopy output formats.  There is a 'pylab' mode
      which emulates matlab graphics
      

%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
