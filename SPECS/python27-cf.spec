%define pname cf-python
Summary: Python interface to the CF data model
Name: python27-cf
Version: 1.5.4.post1
Release: 1.ceda%{?dist}
Source0: cf-python-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: David Hassell <d.c.hassell at reading.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://cfpython.bitbucket.org/
Requires: python27-netCDF4 >= 1.2.9-1.ceda esmf-python27
BuildRequires: python27-netCDF4 >= 1.2.9-1.ceda
Requires: python27 python27-psutil
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
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%define clibdir /usr/lib/python2.7/site-packages/cf/um/umread/c-lib

# delete the C source and object files that shouldn't have been installed,
# and remove the files (in fact source only) from the list
# workaround for issue reported at 
# https://bitbucket.org/cfpython/cf-python/issues/23/umread-c-source-code-installed
clib=$RPM_BUILD_ROOT%{clibdir}
find $clib -not -name umfile.so -not -type d | xargs rm
rmdir $clib/bits $clib/type-dep
perl -n -i -e 'print unless m{^%{clibdir}}' INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{clibdir}/umfile.so

%changelog
* Wed Jul  5 2017  <builderdev@builder.jc.rl.ac.uk> - 1.5.4post1-1.ceda
- update to 1.5.4post1
- remove installation of man pages
- Add dependency on latest python27-netCDF4 (1.2.9-1). Earlier cf-python not working with latest
   netCDF4, and guessing that converse might be true.

* Sun Oct 16 2016  <builderdev@builder.jc.rl.ac.uk> - 1.3.2-1.ceda
- update version
- man pages are now installed properly from the tarball so no longer 
    add these separately

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 1.2.3-1.ceda
- update to 1.2.3

* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.1.5-1.ceda
- update to 1.1.5


* Tue Dec  1 2015  <builderdev@builder.jc.rl.ac.uk> - 1.1.2-1.ceda
- upgrade to 1.1.2 (1.1.1 wasn't released in JAP)
- add dependency esmf-python27

* Tue Nov 17 2015  <a.j.heaps@reading.ac.uk> - 1.1.1-1.ceda
- upgrade to 1.1.1

* Mon Aug 24 2015  <builderdev@builder.jc.rl.ac.uk> - 1.0.3-1.ceda
- upgrade to 1.0.3


* Tue Feb 17 2015  <a.j.heaps@reading.ac.uk> - 0.9.9.1.cms
- update version

* Thu Oct 23 2014 root <root@jasmin-sci1-dev.ceda.ac.uk> - 0.9.8.3-1.ami
- update to 0.9.8.3


