Summary: Common files for backports packages
Name: python27-backports-common
Version: 1.1
Release: 1.ceda%{?dist}
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: CEDA
Requires: python27
BuildRequires: python27

%description

The __init__.py for the backports packages, separated out into a
separate package to avoid conflicts.

%prep
rm -fr %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}

cat > __init__.py <<EOF
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
EOF

%build
cd %{name}-%{version}
pwd
python2.7 -O -m compileall .
python2.7 -c 'import __init__' || true

%install
rm -fr $RPM_BUILD_ROOT
%define dir /usr/lib/python2.7/site-packages/backports
mkdir -p $RPM_BUILD_ROOT/%{dir}
cp __init__.py* $RPM_BUILD_ROOT/%{dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{dir}/__init__.py
%{dir}/__init__.pyc
%{dir}/__init__.pyo

%changelog

* Wed Jul 18 2018  <builderdev@builder.jc.rl.ac.uk> - 1.1-2.ceda
- initial version
