%define pname cf-python
Summary: Python interface to the CF data model
Name: python27-cf
Version: 0.9.8.3
Release: 1.ceda%{?dist}
Source0: cf-%{version}.tar.gz
Source1: cfa.1
Source2: cfdump.1
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: David Hassell <d.c.hassell at reading.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://cfpython.bitbucket.org/
Requires: python27-netCDF4
BuildRequires: python27-netCDF4
Requires: python27
BuildRequires: python27

%description

The python cf package implements the CF data model for the reading, writing and processing of data and its metadata.

CF is a netCDF convention which is in wide and growing use for the storage of model-generated and observational data relating to the atmosphere, ocean and Earth system.

With this package you can:

  *  Read CF-netCDF, CFA-netCDF and PP format files.
  *  Create CF fields.
  *  Aggregate collections of fields into as few multidimensional fields as possible using the CF aggregation rules.
  *  Write fields to CF-netCDF and CFA-netCDF files on disk.
  *  Create, delete and modify a field's data and metadata.
  *  Select fields according to their metadata.
  *  Subspace a field's data to create a new field.
  *  Perform broadcastable, metadata-aware arithmetic, comparison and trigonometric operation with fields.
  *  Collapse fields by statistical operations.
  *  Sensibly deal with date-time data. 

All of the above use Large Amounts of Massive Arrays (LAMA) functionality, which allows multiple fields larger than the available memory to exist and be manipulated.

The package provides command line utilities for viewing CF fields (cfdump) and aggregating datasets (cfa). 

%prep
%setup -n cf-%{version}
mkdir scripts/man1
cp %{SOURCE1} scripts/man1
cp %{SOURCE2} scripts/man1

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%define man1dir %{_datadir}/man/man1
tmp_man1dir=$RPM_BUILD_ROOT/%{man1dir}
mkdir -p $tmp_man1dir
cp scripts/man1/*.1 $tmp_man1dir

# weights.py and weights2.py have syntax errors - removed compiled versions 
# from file list
#perl -i -n -e 'print unless /\/weights(2)?.(pyo|pyc)/' INSTALLED_FILES

# for i in cfa cfdump
# do
#   path=%{_bindir}/$i
#   tmppath=$RPM_BUILD_ROOT$path
#   mv $tmppath ${tmppath}_py27
#   perl -p -i -e "s,$path,${path}_py27," INSTALLED_FILES
# done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc %man1dir/*.1.gz

%changelog

* Thu Oct 23 2014 root <root@jasmin-sci1-dev.ceda.ac.uk> - 0.9.8.3-1.ami
- update to 0.9.8.3

* Mon Jan 14 2013  <builderdev@builder.jc.rl.ac.uk> - 0.9.6-2.ceda
- add manpages
