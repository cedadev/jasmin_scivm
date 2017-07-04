%define pname Sphinx
Summary: Python documentation generator
Name: python27-%{pname}
Version: 1.6.3
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Georg Brandl <georg@python.org>
Url: http://sphinx-doc.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
Requires: python27-six >= 1.5.2-1.ceda
Requires: python27-jinja2 >= 2.7.2-1.ceda
Requires: python27-Pygments >= 2.2.0-1.ceda
Requires: python27-docutils >= 0.13.1-1.ceda
Requires: python27-snowballstemmer >= 1.2.1-1.ceda
Requires: python27-Babel >= 2.4.0-1.ceda
Requires: python27-alabaster >= 0.7.10-1.ceda
Requires: python27-alabaster < 0.8
Requires: python27-imagesize >= 0.7.1-1.ceda
Requires: python27-requests >= 2.18.1-1.ceda
Requires: python27-setuptools
Requires: python27-sphinxcontrib-websupport
BuildRequires: python27
BuildArch: noarch

%description

Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of multiple
reStructuredText sources), written by Georg Brandl.  It was originally created
for the new Python documentation, and has excellent facilities for Python
project documentation, but C/C++ is supported as well, and more languages are
planned.

Sphinx uses reStructuredText as its markup language, and many of its strengths
come from the power and straightforwardness of reStructuredText and its parsing
and translating suite, the Docutils.

Among its features are the following:

* Output formats: HTML (including derivative formats such as HTML Help, Epub
  and Qt Help), plain text, manual pages and LaTeX or direct PDF output
  using rst2pdf
* Extensive cross-references: semantic markup and automatic links
  for functions, classes, glossary terms and similar pieces of information
* Hierarchical structure: easy definition of a document tree, with automatic
  links to siblings, parents and children
* Automatic indices: general index as well as a module index
* Code handling: automatic highlighting using the Pygments highlighter
* Flexible HTML output using the Jinja 2 templating engine
* Various extensions are available, e.g. for automatic testing of snippets
  and inclusion of appropriately formatted docstrings
* Setuptools integration


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
