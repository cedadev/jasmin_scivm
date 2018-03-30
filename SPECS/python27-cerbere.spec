%define pname cerbere
Summary: The Ifremer/Cersat library for reading and normalizing EO data. 
Name: python27-%{pname}
Version: 0.1.619
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Felyx Project Collaborators: Jean-François Piollé <jean.francois.piolle@ifremer.fr>
Url: http://hrdds.ifremer.fr
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

#
# Note: the package is obtained from 
#   git clone https://git.cersat.fr/cerbere/cerbere.git
#
# and the minor version number (currently 619) obtained from
#    git rev-list HEAD | wc
#
# the tarball created locally after renaming the top directory as 
# cerbere-<version>
#

%description

The Ifremer/Cersat library for reading and normalizing EO data. 
See online documentation at: http://cerbere.readthedocs.org/

%prep
%setup -n %{pname}-%{version}
echo %{version} > VERSION.txt

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
