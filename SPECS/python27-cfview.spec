%define pname cfview
Summary: Graohical User Interface to cf-python and cfplot
Name: python27-cfview
Version: 0.6.10
Release: 1.ceda%{?dist}
Source0: cfview
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andy Heaps <a.j.heaps@reading.ac.uk>
Packager: Andy Heaps <a.j.heaps@reading.ac.uk>
Url: http://climate.ncas.ac.uk/~andy/cfview_sphinx/_build/html/#
Requires: python27-netCDF4
Requires: python27 python27-cf python27-cfplot
BuildRequires: python27 python27-cf python27-cfplot


%description

cfview is a graphical user interface that is used for plotting Climate and Forecast convention, CF, data.

%prep

%build

%install
bindir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $bindir
cp %{SOURCE0} $bindir/

%files
%defattr(755,root,root)
%{_bindir}/cfview


%changelog
* Mon Nov 23 2015  <a.j.heaps@reading.ac.uk> - 0.6.10-1.ceda
- initial version 0.6.10


