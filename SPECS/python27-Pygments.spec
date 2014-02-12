%define pname Pygments
Summary: Pygments is a syntax highlighting package written in Python.
Name: python27-%{pname}
Version: 1.5
Release: 3.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Georg Brandl <georg@python.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://pygments.org/
Requires: python27
BuildRequires: python27

%description

    Pygments
    ~~~~~~~~

    Pygments is a syntax highlighting package written in Python.

    It is a generic syntax highlighter for general use in all kinds of software
    such as forum systems, wikis or other applications that need to prettify
    source code. Highlights are:

    * a wide range of common languages and markup formats is supported
    * special attention is paid to details, increasing quality by a fair amount
    * support for new languages and formats are added easily
    * a number of output formats, presently HTML, LaTeX, RTF, SVG, all image       formats that PIL supports and ANSI sequences
    * it is usable as a command-line tool and as a library
    * ... and it highlights even Brainfuck!

    The `Pygments tip`_ is installable with ``easy_install Pygments==dev``.

    .. _Pygments tip:
       http://bitbucket.org/birkenfeld/pygments-main/get/tip.zip#egg=Pygments-dev

    :copyright: Copyright 2006-2012 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# for i in pygmentize
# do
#   path=%{_bindir}/$i
#   tmppath=$RPM_BUILD_ROOT$path
#   mv $tmppath ${tmppath}_py27
#   perl -p -i -e "s,$path,${path}_py27," INSTALLED_FILES
# done

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Thu Feb  6 2014  <builderdev@builder.jc.rl.ac.uk> - 1.5-3.ceda
- comment out renaming of executables

%files -f INSTALLED_FILES
%defattr(-,root,root)
