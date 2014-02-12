%define pname setuptools
%define version 0.6c12dev_r88846
%define unmangled_version 0.6c12dev-r88846

Summary: Download, build, install, upgrade, and uninstall Python packages -- easily!
Name: python27-%{pname}
Version: %{version}
Release: 2.ceda%{?dist}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: PSF or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Phillip J. Eby <distutils-sig@python.org>
Requires: python27
BuildRequires: python27
Url: http://pypi.python.org/pypi/setuptools
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>

%description
===============================
Installing and Using Setuptools
===============================

.. contents:: **Table of Contents**


-------------------------
Installation Instructions
-------------------------

Windows
=======

32-bit version of Python
    Install setuptools using the provided ``.exe`` installer.

64-bit versions of Python
    Download `ez_setup.py`_ and run it; it will download the appropriate .egg file and install it for you.  (Currently, the provided ``.exe`` installer does not support 64-bit versions of Python for Windows, due to a `distutils installer compatibility issue`_

.. _ez_setup.py: http://peak.telecommunity.com/dist/ez_setup.py
.. _distutils installer compatibility issue: http://bugs.python.org/issue6792


NOTE: Regardless of what sort of Python you're using, if you've previously
installed older versions of setuptools, please delete all ``setuptools*.egg``
and ``setuptools.pth`` files from your system's ``site-packages`` directory
(and any other ``sys.path`` directories) FIRST.

If you are upgrading a previous version of setuptools that was installed using
an ``.exe`` installer, please be sure to also *uninstall that older version*
via your system's "Add/Remove Programs" feature, BEFORE installing the newer
version.

Once installation is complete, you will find an ``easy_install.exe`` program in
your Python ``Scripts`` subdirectory.  Be sure to add this directory to your
``PATH`` environment variable, if you haven't already done so.


RPM-Based Systems
=================

Install setuptools using the provided source RPM.  The included ``.spec`` file
assumes you are installing using the default ``python`` executable, and is not
specific to a particular Python version.  The ``easy_install`` executable will
be installed to a system ``bin`` directory such as ``/usr/bin``.

If you wish to install to a location other than the default Python
installation's default ``site-packages`` directory (and ``$prefix/bin`` for
scripts), please use the ``.egg``-based installation approach described in the
following section.


Cygwin, Mac OS X, Linux, Other
==============================

1. Download the appropriate egg for your version of Python (e.g.
   ``setuptools-0.6c9-py2.4.egg``).  Do NOT rename it.

2. Run it as if it were a shell script, e.g. ``sh setuptools-0.6c9-py2.4.egg``.
   Setuptools will install itself using the matching version of Python (e.g.
   ``python2.4``), and will place the ``easy_install`` executable in the
   default location for installing Python scripts (as determined by the
   standard distutils configuration files, or by the Python installation).

If you want to install setuptools to somewhere other than ``site-packages`` or
your default distutils installation locations for libraries and scripts, you
may include EasyInstall command-line options such as ``--prefix``,
``--install-dir``, and so on, following the ``.egg`` filename on the same
command line.  For example::

    sh setuptools-0.6c9-py2.4.egg --prefix=~

You can use ``--help`` to get a full options list, but we recommend consulting
the `EasyInstall manual`_ for detailed instructions, especially `the section
on custom installation locations`_.

.. _EasyInstall manual: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _the section on custom installation locations: http://peak.telecommunity.com/DevCenter/EasyInstall#custom-installation-locations


Cygwin Note
-----------

If you are trying to install setuptools for the **Windows** version of Python
(as opposed to the Cygwin version that lives in ``/usr/bin``), you must make
sure that an appropriate executable (``python2.3``, ``python2.4``, or
``python2.5``) is on your **Cygwin** ``PATH`` when invoking the egg.  For
example, doing the following at a Cygwin bash prompt will install setuptools
for the **Windows** Python found at ``C:\\Python24``::

    ln -s /cygdrive/c/Python24/python.exe python2.4
    PATH=.:$PATH sh setuptools-0.6c9-py2.4.egg
    rm python2.4


Downloads
=========

All setuptools downloads can be found at `the project's home page in the Python
Package Index`_.  Scroll to the very bottom of the page to find the links.

.. _the project's home page in the Python Package Index: http://pypi.python.org/pypi/setuptools#files

In addition to the PyPI downloads, the development version of ``setuptools``   
is available from the `Python SVN sandbox`_, and in-development versions of the 
`0.6 branch`_ are available as well.

.. _0.6 branch: http://svn.python.org/projects/sandbox/branches/setuptools-0.6/#egg=setuptools-dev06

.. _Python SVN sandbox: http://svn.python.org/projects/sandbox/trunk/setuptools/#egg=setuptools-dev

--------------------------------
Using Setuptools and EasyInstall
--------------------------------

Here are some of the available manuals, tutorials, and other resources for
learning about Setuptools, Python Eggs, and EasyInstall:

* `The EasyInstall user's guide and reference manual`_
* `The setuptools Developer's Guide`_
* `The pkg_resources API reference`_
* `Package Compatibility Notes`_ (user-maintained)
* `The Internal Structure of Python Eggs`_

Questions, comments, and bug reports should be directed to the `distutils-sig
mailing list`_.  If you have written (or know of) any tutorials, documentation,
plug-ins, or other resources for setuptools users, please let us know about
them there, so this reference list can be updated.  If you have working,
*tested* patches to correct problems or add features, you may submit them to
the `setuptools bug tracker`_.

.. _setuptools bug tracker: http://bugs.python.org/setuptools/
.. _Package Compatibility Notes: http://peak.telecommunity.com/DevCenter/PackageNotes
.. _The Internal Structure of Python Eggs: http://peak.telecommunity.com/DevCenter/EggFormats
.. _The setuptools Developer's Guide: http://peak.telecommunity.com/DevCenter/setuptools
.. _The pkg_resources API reference: http://peak.telecommunity.com/DevCenter/PkgResources
.. _The EasyInstall user's guide and reference manual: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _distutils-sig mailing list: http://mail.python.org/pipermail/distutils-sig/


-------
Credits
-------

* The original design for the ``.egg`` format and the ``pkg_resources`` API was
  co-created by Phillip Eby and Bob Ippolito.  Bob also implemented the first
  version of ``pkg_resources``, and supplied the OS X operating system version
  compatibility algorithm.

* Ian Bicking implemented many early "creature comfort" features of
  easy_install, including support for downloading via Sourceforge and
  Subversion repositories.  Ian's comments on the Web-SIG about WSGI
  application deployment also inspired the concept of "entry points" in eggs,
  and he has given talks at PyCon and elsewhere to inform and educate the
  community about eggs and setuptools.

* Jim Fulton contributed time and effort to build automated tests of various
  aspects of ``easy_install``, and supplied the doctests for the command-line
  ``.exe`` wrappers on Windows.

* Phillip J. Eby is the principal author and maintainer of setuptools, and
  first proposed the idea of an importable binary distribution format for
  Python application plug-ins.

* Significant parts of the implementation of setuptools were funded by the Open
  Source Applications Foundation, to provide a plug-in infrastructure for the
  Chandler PIM application.  In addition, many OSAF staffers (such as Mike
  "Code Bear" Taylor) contributed their time and stress as guinea pigs for the
  use of eggs and setuptools, even before eggs were "cool".  (Thanks, guys!)

.. _files:


%prep
%setup -n %{pname}-%{unmangled_version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# # remove easy_install link that conflicts with system python
# unversioned_exe=%{_bindir}/easy_install
# rm -f $RPM_BUILD_ROOT$unversioned_exe
# perl -n -i -e "print unless m{^$unversioned_exe$}" INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Thu Feb  6 2014  <builderdev@builder.jc.rl.ac.uk> - 0.6c12dev_r88846-2.ceda
- comment out removal of unversioned executable

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc setuptools.txt EasyInstall.txt pkg_resources.txt README.txt
