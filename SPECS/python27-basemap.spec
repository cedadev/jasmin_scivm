%define pname basemap
Summary: Plot data on map projections with matplotlib
Name: python27-%{pname}
Version: 1.0.5
Release: 4.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://matplotlib.sourceforge.net/toolkits.html
BuildRequires: python27-matplotlib >= 1.2, geos-devel >= 3.3.6
Requires: python27-matplotlib >= 1.2, geos >= 3.3.6
Requires: python27
BuildRequires: python27

%description

  An add-on toolkit for matplotlib that lets you plot data
  on map projections with coastlines, lakes, rivers and political boundaries.
  See http://www.scipy.org/wikis/topical_software/Maps for an
  example of what it can do.

%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 22 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0.5-4.ceda
- require geos 3.3.6 (in order to use version built on JASMIN instead of one taken from Fedora)

* Thu Dec 20 2012  <builderdev@builder.jc.rl.ac.uk> - 1.0.5-3.ceda
- requre matplotlib 1.2

%files -f INSTALLED_FILES
%defattr(-,root,root)
%exclude /usr/lib/python2.7/site-packages/mpl_toolkits/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/mpl_toolkits/__init__.pyo
