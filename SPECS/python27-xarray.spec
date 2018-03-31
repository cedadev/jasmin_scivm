%define pname xarray
Summary: N-D labeled arrays and datasets in Python
Name: python27-%{pname}
Version: 0.10.2
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: xarray Developers <xarray@googlegroups.com>
Url: https://github.com/pydata/xarray
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy >= 1.11, python27-pandas >= 0.18.0
BuildRequires: python27
BuildArch: noarch

%description


**xarray** (formerly **xray**) is an open source project and Python package
that aims to bring the labeled data power of pandas_ to the physical sciences,
by providing N-dimensional variants of the core pandas data structures.

Our goal is to provide a pandas-like and pandas-compatible toolkit for
analytics on multi-dimensional arrays, rather than the tabular data for which
pandas excels. Our approach adopts the `Common Data Model`_ for self-
describing scientific data in widespread use in the Earth sciences:
``xarray.Dataset`` is an in-memory representation of a netCDF file.

.. _pandas: http://pandas.pydata.org
.. _Common Data Model: http://www.unidata.ucar.edu/software/thredds/current/netcdf-java/CDM
.. _netCDF: http://www.unidata.ucar.edu/software/netcdf
.. _OPeNDAP: http://www.opendap.org/

Important links
---------------

- HTML documentation: http://xarray.pydata.org
- Issue tracker: http://github.com/pydata/xarray/issues
- Source code: http://github.com/pydata/xarray
- SciPy2015 talk: https://www.youtube.com/watch?v=X0pAhJgySxk


%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
