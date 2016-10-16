%define pname cf-python
Summary: Python interface to the CF data model
Name: python27-cf
Version: 0.9.9.1
Release: 1.ceda%{?dist}
Source0: cf-%{version}.tar.gz
#Patch0: cf-0.9.4.2-emptyimport.patch
#Patch1: cf-0.9.4.2-straycolon.patch
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: David Hassell <d.c.hassell at reading.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://code.google.com/p/cf-python
Requires: python27-netCDF4
BuildRequires: python27-netCDF4
Requires: python27
BuildRequires: python27

%description

A minimal reference implementation of the proposed CF data model.

CF is a netCDF convention which is in wide and growing use for the
storage of model-generated and observational data relating to the
atmosphere, ocean and Earth system.

This software:

    * Reads and writes CF-netCDF files, and contains the data and
      metadata in memory in objects called fields in a way which is
      consistent with the data model.

    * Aggregates fields according to the CF aggregation rules.

    * Allows the creation, deletion and alteration of a field's data
      and metadata.

    * Allows the subsetting of a list of fields according to their
      metadata attributes.

    * Extracts sub-regions from fields, creating new
      fields. Sub-regions may be defined by specifying ranges of
      coordinates or ranges indices along the dimensions.

There are currently no other processing abilities or any graphical
functions, but it is envisaged that such higher-level functions could
be built on the axiomatic capabilities so far included. A collapse
function is under development.

%prep
%setup -n cf-%{version}
#%patch0 -p1
#%patch1 -p1

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%define man1dir %{_datadir}/man/man1
tmp_man1dir=$RPM_BUILD_ROOT/%{man1dir}
mkdir -p $tmp_man1dir
cp scripts/man1/*.1 $tmp_man1dir

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

* Tue Feb 17 2015  <a.j.heaps@reading.ac.uk> - 0.9.9.1.cms
- update version

