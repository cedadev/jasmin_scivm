%define pname iris_sample_data
Summary: Iris sample data
Name: python27-%{pname}
Version: 2.0.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Open Government
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Met Office Hadley Centre
Url: https://github.com/SciTools/iris-sample-data
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

This repository is a store for the data used in the iris examples. 

See the iris repository's INSTALL file for instructions of installation.

Documentation, example and data license
---------------------------------------
 
    |copy| British Crown copyright, 2012.
    
    You may use and re-use the information featured in this repository (not including logos) free of 
    charge in any format or medium, under the terms of the 
    `Open Government Licence <http://reference.data.gov.uk/id/open-government-licence>`_. 
    We encourage users to establish hypertext links to this website.
    
    Any email enquiries regarding the use and re-use of this information resource should be 
    sent to: psi@nationalarchives.gsi.gov.uk.

%prep
%setup -n iris-sample-data-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
