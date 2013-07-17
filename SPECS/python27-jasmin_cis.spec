%define pname jasmin_cis
Summary: JASMIN Community Inter-comparison Suite
Name: python27-%{pname}
Version: 0.6
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LGPL 3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Stephen Pascoe <Stephen.Pascoe@stfc.ac.uk>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://proj.badc.rl.ac.uk/cedaservices/wiki/JASMIN/CommunityIntercomparisonSuite
Requires: python27
Requires: python27-iris python27-numpy python27-matplotlib python27-pyhdf
BuildRequires: python27
BuildRequires: python27-setuptools

%description
This package contains code for the JASMIN Community Inter-comparison Suite.  Development is documented at http://proj.badc.rl.ac.uk/cedaservices/wiki/JASMIN/CommunityIntercomparisonSuite

Contact
-------

Stephen.Pascoe@stfc.ac.uk
Philip.Stier@physics.ox.ac.uk


Copyright and licence
---------------------

(C) University of Oxford 2013

This file is part of the JASMIN Community Inter-comparison Suite (CIS).

CIS is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Iris.  If not, see <http://www.gnu.org/licenses/>.



%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --install-data=%{_datadir} --record=INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT

%changelog

%files -f INSTALLED_FILES
%defattr(-,root,root)
