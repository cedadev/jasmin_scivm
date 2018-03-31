%define pname s3transfer
Summary: An Amazon S3 Transfer Manager
Name: python27-%{pname}
Version: 0.1.13
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Amazon Web Services <kyknapp1@gmail.com>
Url: https://github.com/boto/s3transfer
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

=====================================================
s3transfer - An Amazon S3 Transfer Manager for Python
=====================================================

S3transfer is a Python library for managing Amazon S3 transfers.

.. note::

  This project is not currently GA. If you are planning to use this code in
  production, make sure to lock to a minor version as interfaces may break
  from minor version to minor version. For a basic, stable interface of
  s3transfer, try the interfaces exposed in `boto3 <https://boto3.readthedocs.io/en/latest/guide/s3.html#using-the-transfer-manager>`__


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
