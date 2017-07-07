%define pname cf-view
Summary: Graohical User Interface to cf-python and cf-plot
Name: python27-%{pname}
Version: 1.0.4
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andy Heaps <a.j.heaps@reading.ac.uk>
Packager: Andy Heaps <a.j.heaps@reading.ac.uk> and Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://ajheaps.github.io/cf-view/
Requires: python27-netCDF4
Requires: python27 python27-cf python27-cf-plot
BuildRequires: python27 python27-cf python27-cf-plot
BuildArch: noarch
Obsoletes: python27-cfview


%description

cfview is a graphical user interface that is used for plotting Climate and Forecast convention, CF, data.

%prep
%setup -n cf-view-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(755,root,root)


%changelog
* Wed Jul  5 2017  <builderdev@builder.jc.rl.ac.uk> - 1.0.4-1.ceda
- update to 1.0.4
- change architecture to 'noarch'
- change to use setup.py
- change package name to include hyphen (python27-cf-view), and obsolete python27-cfview

* Mon Nov 23 2015  <a.j.heaps@reading.ac.uk> - 0.6.10-1.ceda
- initial version 0.6.10


