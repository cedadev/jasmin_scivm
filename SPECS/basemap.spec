%define pname basemap
Summary: Plot data on map projections with matplotlib
Name: python-%{pname}
Version: 1.0.5
Release: 3.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Whitaker <jeffrey.s.whitaker@noaa.gov>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://matplotlib.sourceforge.net/toolkits.html
BuildRequires: python-matplotlib, geos-devel
Requires: python-matplotlib, geos

%description

  An add-on toolkit for matplotlib that lets you plot data
  on map projections with coastlines, lakes, rivers and political boundaries.
  See http://www.scipy.org/wikis/topical_software/Maps for an
  example of what it can do.

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
%exclude %{_libdir}/python2.6/site-packages/mpl_toolkits/__init__.pyc
%exclude %{_libdir}/python2.6/site-packages/mpl_toolkits/__init__.pyo
