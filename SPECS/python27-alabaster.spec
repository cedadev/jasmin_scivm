%define pname alabaster
Summary: A configurable sidebar-enabled Sphinx theme
Name: python27-%{pname}
Version: 0.7.10
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Jeff Forcier <jeff@bitprophet.org>
Url: https://alabaster.readthedocs.io
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

What is Alabaster?
==================

Alabaster is a visually (c)lean, responsive, configurable theme for the `Sphinx
<http://sphinx-doc.org>`_ documentation system. It is Python 2+3 compatible.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is selected
as the default theme.

Live examples of this theme can be seen on `this project's own website
<http://alabaster.readthedocs.io>`_, `paramiko.org <http://paramiko.org>`_,
`fabfile.org <http://fabfile.org>`_ and `pyinvoke.org <http://pyinvoke.org>`_.

For more documentation, please see http://alabaster.readthedocs.io.

.. note::
    You can install the development version via ``pip install -e
    git+https://github.com/bitprophet/alabaster/#egg=alabaster``.



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
