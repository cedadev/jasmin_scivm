%define pname pybtex
Summary: A BibTeX-compatible bibliography processor in Python
Name: python27-%{pname}
Version: 0.21
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Andrey Golovizin <ag@sologoc.com>
Url: https://pybtex.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27 python27-PyYAML >= 3.01 python27-latexcodec >= 1.0.4
BuildArch: noarch

%description

BibTeX-compatible bibliography processor in Python
==================================================

Synopsis
--------

::

    latex foo.tex
    pybtex foo.aux
    latex foo.tex
    latex foo.tex


Description
-----------

Pybtex reads citation information from a file and
produces a formatted bibliography. BibTeX style files are supported.
Alternatively it is possible to write styles in Python.

Pybtex currently understands the following bibliography formats:

- BibTeX

- BibTeXML

- YAML-based format

The resulting bibliography may be output in one of the following formats
(not supported by legacy BibTeX styles):

- LaTeX

- HTML

- markdown

- plain text


See also
--------

- `Home page <https://pybtex.org/>`_

- `Pybtex at Bitbucket <https://bitbucket.org/pybtex-devs/pybtex>`_

- `Pybtex at PyPI <https://pypi.python.org/pypi/pybtex>`_




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
