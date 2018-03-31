%define pname botocore
Summary: Low-level, data-driven core of boto 3.
Name: python27-%{pname}
Version: 1.9.21
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Amazon Web Services <UNKNOWN>
Url: https://github.com/boto/botocore
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the
`AWS CLI <https://github.com/aws/aws-cli>`__ as well as
`boto3 <https://github.com/boto/boto3>`__.


Documentation
-------------
Documentation for ``botocore`` can be found on `Read the Docs <https://botocore.readthedocs.io/en/latest/>`__.


Getting Help
------------

We use GitHub issues for tracking bugs and feature requests and have limited
bandwidth to address them. Please use these community resources for getting
help. Please note many of the same resources available for ``boto3`` are
applicable for ``botocore``:

* Ask a question on `Stack Overflow <https://stackoverflow.com/>`__ and tag it with `boto3 <https://stackoverflow.com/questions/tagged/boto3>`__
* Come join the AWS Python community chat on `gitter <https://gitter.im/boto/boto3>`__
* Open a support ticket with `AWS Support <https://console.aws.amazon.com/support/home#/>`__
* If it turns out that you may have found a bug, please `open an issue <https://github.com/boto/botocore/issues/new>`__




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
