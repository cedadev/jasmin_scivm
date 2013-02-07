%{!?__python_ver:%global __python_ver EMPTY}
#define __python_ver 26
%global unicode ucs4

%global _default_patch_fuzz 2

%if "%{__python_ver}" != "EMPTY"
%global main_python 0
%global python python%{__python_ver}
%global tkinter tkinter%{__python_ver}
%else
%global main_python 1
%global python python
%global tkinter tkinter
%endif

%global pybasever 2.7
%global pylibdir %{_libdir}/python%{pybasever}
%global tools_dir %{pylibdir}/Tools
%global demo_dir %{pylibdir}/Demo
%global doc_tools_dir %{pylibdir}/Doc/tools
%global dynload_dir %{pylibdir}/lib-dynload
%global site_packages %{pylibdir}/site-packages

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0
%global py_INSTSONAME libpython%{pybasever}.so.%{py_SOVERSION}

%global with_gdb_hooks 1

%global with_systemtap 1

%ifarch %{ix86} x86_64 ppc ppc64
%global with_valgrind 1
%global with_valgrind_config_opt --with-valgrind
%else
%global with_valgrind 0
%global with_valgrind_config_opt
%endif

Summary: An interpreted, interactive, object-oriented programming language
Name: %{python}
Version: 2.7.3
Release: 1.ceda%{?dist}
License: Python
Group: Development/Languages
Provides: python-abi = %{pybasever}
Provides: python(abi) = %{pybasever}
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2


# We install a collection of hooks for gdb that make it easier to debug
# executables linked against libpython (such as /usr/lib/python itself)
#
# These hooks are implemented in Python itself
#
# gdb-archer looks for them in the same path as the ELF file, with a -gdb.py suffix.
# We put them in the debuginfo package by installing them to e.g.:
#  /usr/lib/debug/usr/lib/libpython2.6.so.1.0.debug-gdb.py
#
# See https://fedoraproject.org/wiki/Features/EasierPythonDebugging for more
# information
#
# Downloaded from:
#  http://bugs.python.org/issue8032
# This is Tools/gdb/libpython.py from v5 of the patch
Source1: python-gdb.py

# Systemtap tapset to make it easier to use the systemtap static probes,
# allowing the use of "python.function.entry" and "python.function.return",
# rather than requiring scripts to spell out the full path to the python
# library.
# This is actually a template; LIBRARY_PATH will get fixed up during install:
Source3: libpython.stp

# Example systemtap script using the tapset: shows the hierarchy of pure-python
# function calls and returns:
Source4: systemtap-example.stp

# Another example systemtap script that uses the tapset: shows a "top"-like
# view of python function calls:
Source5: pyfuntop.stp

Patch0: python-2.6.2-config.patch
Patch1: Python-2.2.1-pydocnogui.patch

# Fixup configure.in and setup.py to build against system expat library.
# Adapted from http://svn.python.org/view?view=rev&revision=77169
Patch3: python-2.6.2-with-system-expat.patch

Patch4: python-2.5-cflags.patch

Patch6: python-2.5.1-plural-fix.patch
Patch7: python-2.5.1-sqlite-encoding.patch

Patch10: python-2.6.2-binutils-no-dep.patch
Patch11: python-2.5.1-codec-ascii-tolower.patch

Patch13: python-2.5.1-socketmodule-constants.patch
Patch14: python-2.5.1-socketmodule-constants2.patch

Patch16: python-2.6-rpath.patch

# Fix distutils to follow the Fedora/RHEL/CentOS policies of having .pyo files
Patch51: python-2.6-distutils_rpm.patch

# Automatically disable arena allocator when run under valgrind:
# From http://bugs.python.org/issue2422
#   http://bugs.python.org/file9872/disable-pymalloc-on-valgrind-py26.patch
# with the "configure" part removed; appears to be identical to the version committed to 2.7
Patch52: disable-pymalloc-on-valgrind-py26.patch

# lib64 patches
Patch101: python-2.3.4-lib64-regex.patch
Patch102: python-2.6-lib64.patch

# SELinux patches
Patch110: python-2.6.5-ctypes-noexecmem.patch

# Patch the Makefile.pre.in so that the generated Makefile doesn't try to build
# a libpythonMAJOR.MINOR.a (bug 550692):
Patch111: python-2.6.2-no-static-lib.patch

# Add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
# (rhbz:553020); partially upstream as http://bugs.python.org/issue7647
Patch112: python-2.6.2-statvfs-f_flag-constants.patch

# Fix an incompatibility between pyexpat and the system expat-2.0.1 that led to
# a segfault running test_pyexpat.py (rhbz:583931)
# Sent upstream as http://bugs.python.org/issue9054
Patch117: python-2.6.2-fix-expat-issue9054.patch

# Support OpenSSL FIPS mode:
# - handle failures from OpenSSL (e.g. on attempts to use MD5 in a
#   FIPS-enforcing environment)
# - add a new "usedforsecurity" keyword argument to the various digest
#   algorithms in hashlib so that you can whitelist a callsite with
#   "usedforsecurity=False"
# (sent upstream for python 3 as http://bugs.python.org/issue9216; this is a
# backport to python 2.6)
# - enforce usage of the _hashlib implementation: don't fall back to the _md5
#   and _sha* modules (leading to clearer error messages if fips selftests
#   fail)
# - don't build the _md5 and _sha* modules; rely on the _hashlib implementation
#   of hashlib
Patch119: python-2.6.5-hashlib-fips.patch

# Fix a 2.7-ism accidentally added upstream into 2.6.6's selftest suite that
# leads to a failure in test_posix when run as root
# Sent upstream as http://bugs.python.org/issue10585
Patch120: python-2.6.6-fix-test_setgroups.patch

# Fix dbm.contains on ppc64 and s390x (rhbz#626756)
# Sent upstream as http://bugs.python.org/issue9687
Patch121: fix-dbm_contains-on-64bit-bigendian.patch

# Add various lib2to3/tests/data and various directories below it to
# Makefile.pre.in's LIBSUBDIRS, so that they get installed, for use by the
# "test" subpackage (rhbz#625395)
# Based on upstream r71740 vs r71395, but also removing some usages of "with"
# with multiple context managers from py2_test_grammar (as this was introduced in
# 3.1/2.7):
Patch122: python-2.6.6-install-missing-lib2to3-test-files.patch

# test_commmands fails on SELinux systems due to a change in the output
# of "ls" (http://bugs.python.org/issue7108) (rhbz#625393)
Patch123: fix-test_commands-expected-ls-output-issue7108.patch

# Make "pydoc -k" more robust in the face of broken modules
# (rhbz#603073; patch sent upstream as http://bugs.python.org/issue7425 )
Patch124: make-pydoc-more-robust-001.patch

# Use an ephemeral port for IDLE, enabling multiple instances to be run
# (cherrypick upstream r71126 for http://bugs.python.org/issue1529142
# rhbz#639222)
Patch125: use-ephemeral-port-for-IDLE.patch

# Systemtap support: add statically-defined probe points "function__entry" and
# "function__return" to the bytecode dispatch loop (rhbz#569695)
Patch126: python-2.6.6-systemtap.patch

# Port subprocess to use the "poll" system call (via "select.poll"), rather
# than the "select" system call (via "select.select"), avoiding an arbitrary
# limit on the number of filedescriptors that can be monitored, and thus on the
# number of subprocesses.
#
# Upstream issue http://bugs.python.org/issue3392
#
# This is a backport of upstream r73825, r73916 and r73818 from "trunk" to 2.6
# (rhbz#650588)
Patch127: python-2.6.6-subprocess-poll.patch

# Allow the "no_proxy" env variable to override "ftp_proxy" in urllib2, by
# ensuring that req.host is set in ProxyHandler.proxy_open() (rhbz#637895)
Patch128: python-2.6.6-urllib2-ftp-no-proxy.patch

# Try to print repr() when an C-level assert fails in the garbage collector,
# typically indicating a reference-counting error somewhere else (e.g in an
# extension module)
# Backported to 2.6 from a patch I sent upstream for py3k
#   http://bugs.python.org/issue9263  (rhbz#614680)
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing
# them within the extension API.
Patch129: python-2.6.6-gc-assertions.patch

# Prevent _sqlite3.so being built with a redundant RPATH of _libdir:
# (rhbz#634944)
Patch130: python-2.6.6-remove-sqlite-rpath.patch


# Add an optional "timeout" argument to the subprocess module (rhbz#567229)
#
# This is a non-standard extension to Python 2.6, but is based on an upstream
# proposal being tracked for Python 3 as:
#    http://bugs.python.org/issue5673
# 
# The "timeout" argument is a number of seconds, which can be an integer or a
# float (though there are no precision guarantees)
#
# This change adds the "timeout" argument to the following API entrypoints:
#   subprocess.call
#   Popen.communicate
#   Popen.wait
#
# A TimeoutExpired exception will be raised after the given number of seconds
# elapses, if the call has not yet returned.
#
# Based on upstream subprocess-timeout-v5.patch, with fixes for
# assertStderrEqual, and marking the API as non-standard
Patch131: python-2.6.6-subprocess-timeout.patch

# Fix a regression in 2.6.6 relative to 2.6.5 in urllib2
# (ased on upstream SVN commit 84207; rhbz#669847)
Patch132: python-2.6.6-fix-urllib2-AbstractBasicAuthHandler.patch

# Add workaround for bug in Rhythmbox exposed by 2.6.6 (rhbz#684991)
Patch133: python-2.6.6-rhythmbox-workaround.patch

# Fix incompatibility between 2.6.6 and M2Crypto.SSL.SSLTimeoutError from our
# m2crypto-0.18-timeouts.patch (rhbz#681811)
Patch134: python-2.6.6-fix-EINTR-check-for-nonstandard-exceptions.patch

# A new test in 2.6.6 fails on 64-bit big-endian architectures (rhbz#677392)
Patch135: python-test_structmembers.patch

# Backport of improvements to the forthcoming Python 3.3's "crypt" module,
# adding precanned ways of salting a password  (rhbz#681878)
# Based on r88500 patch to py3k from forthcoming Python 3.3
# plus 6482dd1c11ed, 0586c699d467, 62994662676a, plus edits to docstrings to
# note that this additional functionality is not standard within 2.6
Patch136: python-2.6.6-crypt-module-salt-backport.patch

# Fix race condition in parallel make that could lead to graminit.c failing
# to compile, or linker errors with "undefined reference to
# `_PyParser_Grammar'":
# See e.g. http://bugs.python.org/issue10013
Patch137: python-2.6.6-fix-parallel-make.patch

# Fix for CVE-2011-1521, based on
# http://hg.python.org/cpython/rev/9eeda8e3a13f/
Patch138: python-2.6.6-CVE-2011-1521.patch

# Fix for CVE-2011-1015, based on
# http://hg.python.org/cpython/raw-rev/c6c4398293bd
Patch139: python-2.6.6-CVE-2011-1015.patch

# Fix for CVE-2010-3493, based on
# http://hg.python.org/cpython/rev/aa30b16d07bc/
Patch140: python-2.6.6-CVE-2010-3493.patch

# Backport the fix for transient failures in multiprocess's
# forking.Process.poll() from 2.7 to 2.6 (rhbz#685234):
Patch141: python-2.6.6-fix-transient-multiprocessing-failures.patch

# Port _multiprocessing.Connection.poll() to use the "poll" syscall, rather
# than "select", allowing large numbers of subprocesses (rhbz#713082)
Patch142: python-2.6.6-use-poll-for-multiprocessing-socket-connection.patch

# Backport to 2.6 of the upstream fix allowing getpass.getpass() to be
# interrupted using Ctrl-C or Ctrl-Z (rhbz#689794)
Patch143: python-2.6.6-allow-getpass-to-be-interrupted.patch

# Memory leak fixes for readline module (rhbz#699740)
#
#   Based on upstream fix for upstream issue #9450:
Patch144: python-2.6.6-readline-introduce-py-free-history-entry.patch
#
#   Based on upstream fix for upstream issue #8065; fixes leaks in
# readline.get_history_length() and readline.get_history_item():
Patch145: python-2.6.6-readline-introduce-get-history-length.patch

# subprocess.Popen's communicate() could sometimes fail on short-lived
# processes with:  OSError: [Errno 32] Broken pipe
# Backport the fix for this from 2.7 to 2.6.6: (rhbz#667431)
Patch146: python-2.6.6-Popen-communicate-EPIPE.patch

# Update uid/gid handling throughout the standard library: uid_t and gid_t are
# unsigned 32-bit values, but existing code often passed them through C long
# values, which are signed 32-bit values on 32-bit architectures, leading to
# negative int objects for uid/gid values >= 2^31 on 32-bit architectures.
#
# Introduce _PyObject_FromUid/Gid to convert uid_t/gid_t values to python
# objects, using int objects where the value will fit (long objects otherwise),
# and _PyArg_ParseUid/Gid to convert int/long to uid_t/gid_t, with -1 allowed
# as a special case (since this is given special meaning by the chown syscall)
#
# Update standard library to use this throughout for uid/gid values, so that
# very large uid/gid values are round-trippable, and -1 remains usable.
# (rhbz#697470)
Patch147: python-2.6.6-uid-gid-overflows.patch

# Update distutils.sysconfig so that if CFLAGS is defined in the environment,
# when building extension modules, it is appended to the full compilation
# flags from Python's Makefile, rather than instead reducing the compilation
# flags to the subset within OPT and adding it to those:
# (rhbz#727364)
Patch148: python-2.6.6-distutils-cflags.patch

# CVE-2012-1150/oCERT-2011-003: add -R command-line option and PYTHONHASHSEED
# environment variable, to provide an opt-in way to protect against denial of
# service attacks due to hash collisions within the dict and set types
#
# Based on the following upstream changesets:
#  75100:6b7704fe1be1
#  75101:19e6e55f09f3
#  75124:04738f35e0ec
#  75133:357e268e7c5f
#    with the
#        assert(_Py_HashSecret_Initialized);
#    invocations in string_hash and unicode_hash removed, and
#    _Py_HashSecret_Initialized made public, even in optimized builds
#  75148:76d72e92fdea
#  75158:65d1fe86618f
#  75181:c7baaf0cde8d
#  75183:bff3fd529e33
#  75188:0f095a0f124c
# (we don't need 75130:4c69ec7e9bca which was removed in 75150:6075df248b90
# as superceded by 75148:76d72e92fdea)
#
# This also has minor documentation changes relative to upstream to indicate
# that the randomization covers str, unicode, buffer, and datetime
Patch149: python-2.6.6-hash-randomization.patch

# Fix an endless loop in SimpleXMLRPCServer upon malformed POST request
# (http://bugs.python.org/issue14001; CVE-2012-0845):
Patch150: python-2.6.6-CVE-2012-0845.patch

# Send encoding in SimpleHTTPServer.list_directory to protect IE7 against
# potential XSS attacks (http://bugs.python.org/issue11442; CVE-2011-4940):
Patch151: python-2.6.6-CVE-2011-4940.patch

# Patch distutils to create ~/.pypirc securely
# (http://bugs.python.org/issue13512; CVE-2011-4944):
Patch152: python-2.6.6-CVE-2011-4944.patch

# If hash randomization is enabled, also enable it when using expat
# (http://bugs.python.org/issue14234; 2012-0876):
Patch153: python-2.6.6-CVE-2012-0876.patch
# ...and patch configure.in to verify that XML_SetHashSalt is present within
# the expat library:
Patch154: python-2.6.6-check-for-XML_SetHashSalt.patch

# Add an explicit RPATH to pyexpat.so pointing at the directory
# containing the system expat (which has the extra XML_SetHashSalt
# symbol), to avoid an ImportError with a link error if there's an
# LD_LIBRARY_PATH containing a "vanilla" build of expat (without the
# symbol) (rhbz#833271):
Patch155: python-2.6.6-add-RPATH-to-pyexpat.patch


%if %{main_python}
Obsoletes: Distutils
Provides: Distutils
Obsoletes: python2 
Provides: python2 = %{version}
Obsoletes: python-elementtree <= 1.2.6
Obsoletes: python-sqlite < 2.3.2
Provides: python-sqlite = 2.3.2
Obsoletes: python-ctypes < 1.0.1
Provides: python-ctypes = 1.0.1
Obsoletes: python-hashlib < 20081120
Provides: python-hashlib = 20081120
Obsoletes: python-uuid < 1.31
Provides: python-uuid = 1.31
# Python 2.6 onwards contains an "ssl" module:
Obsoletes: python-ssl
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: readline-devel, openssl-devel, gmp-devel
BuildRequires: ncurses-devel, gdbm-devel, zlib-devel

# CVE-2012-0876: we require a build of expat that contains the new symbol
# XML_SetHashSalt (added upstream in 2.1.0 without bumping SONAME, and
# backported in this version-release):
BuildRequires: expat-devel >= 2.0.1-10

BuildRequires: libGL-devel tk tix gcc-c++ libX11-devel glibc-devel
BuildRequires: bzip2 tar /usr/bin/find pkgconfig tcl-devel tk-devel
BuildRequires: tix-devel bzip2-devel sqlite-devel
BuildRequires: autoconf
BuildRequires: db4-devel >= 4.7
BuildRequires: libffi-devel
%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif # with_valgrind

%if 0%{?with_systemtap}
BuildRequires: systemtap-sdt-devel
%global tapsetdir      /usr/share/systemtap/tapset
%endif

URL: http://www.python.org/

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that need
a programmable interface. This package contains most of the standard
Python modules, as well as modules for interfacing to the Tix widget
set for Tk and RPM.

Note that documentation for Python is provided in the python-docs
package.

%package libs
Summary: The libraries for python runtime
Group: Applications/System
Requires: %{python} = %{version}-%{release}
# Needed for ctypes, to load libraries, worked around for Live CDs size
# Requires: binutils

# _Py_HashSecret was added to the public API of libpython2.6.so.1 when hash
# randomization was added (in python-libs-2.6.6-29.el6_2.1) so we provide this
# in case any other packages need to use this API extension:
Provides: _Py_HashSecret%{?_isa}

%description libs
The python interpreter can be embedded into applications wanting to 
use python as an embedded scripting language.  The python-libs package 
provides the libraries needed for this.

%package devel
Summary: The libraries and header files needed for Python development
Group: Development/Libraries
Requires: %{python}%{?_isa} = %{version}-%{release}
# Needed here because of the migration of Makefile from -devel to the main
# package
Conflicts: %{python} < %{version}-%{release}
%if %{main_python}
Obsoletes: python2-devel
Provides: python2-devel = %{version}-%{release}
%endif

%description devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install python-devel if you want to develop Python extensions.  The
python package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%package tools
Summary: A collection of development tools included with Python
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: %{tkinter} = %{version}-%{release}
%if %{main_python}
Obsoletes: python2-tools
Provides: python2-tools = %{version}
%endif

%description tools
This package includes several tools to help with the development of Python   
programs, including IDLE (an IDE with editing and debugging facilities), a 
color editor (pynche), and a python gettext program (pygettext.py).  

%package -n %{tkinter}
Summary: A graphical user interface for the Python scripting language
Group: Development/Languages
BuildRequires:  tcl, tk
Requires: %{name} = %{version}-%{release}
%if %{main_python}
Obsoletes: tkinter2
Provides: tkinter2 = %{version}
%endif

%description -n %{tkinter}

The Tkinter (Tk interface) program is an graphical user interface for
the Python scripting language.

You should install the tkinter package if you'd like to use a graphical
user interface for Python programming.

%package test
Summary: The test modules from the main python package
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description test

The test modules from the main python package: %{name}
These have been removed to save space, as they are never or almost
never used in production.

You might want to install the python-test package if you're developing python
code that uses more than just unittest and/or test_support.py.

%prep
%setup -q -n Python-%{version}

%if 0%{?with_systemtap}
# Provide an example of usage of the tapset:
cp -a %{SOURCE4} .
cp -a %{SOURCE5} .
%endif # with_systemtap

# Ensure that we're using the system copy of various libraries, rather than
# copies shipped by upstream in the tarball:
#   Remove embedded copy of expat:
rm -r Modules/expat || exit 1

#   Remove embedded copy of libffi:
for SUBDIR in darwin libffi libffi_arm_wince libffi_msvc libffi_osx ; do
  rm -r Modules/_ctypes/$SUBDIR || exit 1 ;
done

#   Remove embedded copy of zlib:
rm -r Modules/zlib || exit 1

#
# Apply patches:
#
%patch0 -p1 -b .rhconfig
%patch3 -p1 -b .expat
%patch1 -p1 -b .no_gui

%patch4 -p1 -b .cflags

%patch6 -p1 -b .plural
%patch7 -p1

%if "%{_lib}" == "lib64"
%patch101 -p1 -b .lib64-regex
%patch102 -p1 -b .lib64
%endif

%patch10 -p1 -b .binutils-no-dep
%patch11 -p1 -b .ascii-tolower

%patch13 -p1 -b .socketmodule
%patch14 -p1 -b .socketmodule2

%patch16 -p1 -b .rpath

%patch51 -p1 -b .brprpm
%if 0%{?with_valgrind}
%patch52 -p1 -b .disable-pymalloc-on-valgrind
%endif

%ifarch alpha ia64
# 64bit, but not lib64 arches need this too...
%patch101 -p1 -b .lib64-regex
%endif

%patch110 -p1 -b .selinux
%patch111 -p1 -b .no-static-lib

%patch112 -p1 -b .statvfs-f-flag-constants

%patch117 -p0 -b .fix-expat-issue9054

%patch119 -p1 -b .hashlib-fips

%patch120 -p0

%patch121 -p0 -b .fix-dbm-contains-on-64bit-bigendian

%patch122 -p1 

%patch123 -p1

%patch124 -p0

%patch125 -p1

%if 0%{?with_systemtap}
%patch126 -p1 -b .systemtap
%endif

%patch127 -p1

%patch128 -p1

%patch129 -p1

%patch130 -p1

%patch131 -p1

%patch132 -p1

%patch133 -p1

%patch134 -p1

%patch135 -p0

%patch136 -p1
mv Modules/cryptmodule.c Modules/_cryptmodule.c

%patch137 -p1 -b .fix-parallel-make

%patch138 -p1

%patch139 -p1

%patch140 -p1

%patch141 -p1

%patch142 -p1

%patch143 -p1

%patch144 -p1 -b .readline-introduce-py-free-history-entry
%patch145 -p1 -b .readline-introduce-get-history-length

%patch146 -p1

%patch147 -p1

%patch148 -p1

%patch149 -p1

%patch150 -p1

%patch151 -p1

%patch152 -p1

%patch153 -p1
%patch154 -p1 -b .check-for-XML_SetHashSalt

%patch155 -p1 -b .add-RPATH-to-pyexpat

# Don't build these crypto algorithms; instead rely on _hashlib and OpenSSL:
for f in md5module.c md5.c shamodule.c sha256module.c sha512module.c; do
    rm Modules/$f
done

# This shouldn't be necesarry, but is right now (2.2a3)
find -name "*~" |xargs rm -f

%build
topdir=`pwd`
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="`pkg-config --cflags-only-I libffi`"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
if pkg-config openssl ; then
  export CFLAGS="$CFLAGS `pkg-config --cflags openssl`"
  export LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi
# Force CC
export CC=gcc
# For patches 3, 4, 52 and 154 need to get a newer configure generated out
# of configure.in
autoconf
%configure \
    --enable-ipv6 \
    --enable-unicode=%{unicode} \
    --enable-shared \
    --with-system-ffi \
    --with-system-expat \
    %{with_valgrind_config_opt} \
%if 0%{?with_systemtap}
  --with-dtrace \
  --with-tapset-install-dir=%{tapsetdir} \
%endif
   %{nil}

make OPT="$CFLAGS" %{?_smp_mflags}
LD_LIBRARY_PATH=$topdir $topdir/python Tools/scripts/pathfix.py -i "%{_bindir}/env python%{pybasever}" .
# Rebuild with new python
# We need a link to a versioned python in the build directory
ln -s python python%{pybasever}
LD_LIBRARY_PATH=$topdir PATH=$PATH:$topdir make -s OPT="$CFLAGS" %{?_smp_mflags}



%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT%{_mandir}

# Clean up patched .py files that are saved as .lib64
for f in distutils/command/install distutils/sysconfig; do
    rm -f Lib/$f.py.lib64
done

make install DESTDIR=$RPM_BUILD_ROOT
# Fix the interpreter path in binaries installed by distutils 
# (which changes them by itself)
# Make sure we preserve the file permissions
for fixed in $RPM_BUILD_ROOT%{_bindir}/pydoc; do
    sed 's,#!.*/python$,#!%{_bindir}/env python%{pybasever},' $fixed > $fixed- \
        && cat $fixed- > $fixed && rm -f $fixed-
done

# Junk, no point in putting in -test sub-pkg
rm -f $RPM_BUILD_ROOT/%{pylibdir}/idlelib/testcode.py*

# don't include tests that are run at build time in the package
# This is documented, and used: rhbz#387401
if /bin/false; then
 # Move this to -test subpackage.
mkdir save_bits_of_test
for i in test_support.py __init__.py; do
  cp -a $RPM_BUILD_ROOT/%{pylibdir}/test/$i save_bits_of_test
done
rm -rf $RPM_BUILD_ROOT/%{pylibdir}/test
mkdir $RPM_BUILD_ROOT/%{pylibdir}/test
cp -a save_bits_of_test/* $RPM_BUILD_ROOT/%{pylibdir}/test
fi

%if %{main_python}
ln -s python $RPM_BUILD_ROOT%{_bindir}/python2
%else
mv $RPM_BUILD_ROOT%{_bindir}/python $RPM_BUILD_ROOT%{_bindir}/%{python}
mv $RPM_BUILD_ROOT/%{_mandir}/man1/python.1 $RPM_BUILD_ROOT/%{_mandir}/man1/python%{pybasever}.1
%endif

# tools

mkdir -p ${RPM_BUILD_ROOT}%{site_packages}

#modulator
cat > ${RPM_BUILD_ROOT}%{_bindir}/modulator << EOF
#!/bin/bash
exec %{site_packages}/modulator/modulator.py
EOF
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/modulator
cp -r Tools/modulator \
  ${RPM_BUILD_ROOT}%{site_packages}/

#pynche
cat > ${RPM_BUILD_ROOT}%{_bindir}/pynche << EOF
#!/bin/bash
exec %{site_packages}/pynche/pynche
EOF
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/pynche
rm -f Tools/pynche/*.pyw
cp -r Tools/pynche \
  ${RPM_BUILD_ROOT}%{site_packages}/

mv Tools/modulator/README Tools/modulator/README.modulator
mv Tools/pynche/README Tools/pynche/README.pynche

#gettext
install -m755  Tools/i18n/pygettext.py $RPM_BUILD_ROOT%{_bindir}/
install -m755  Tools/i18n/msgfmt.py $RPM_BUILD_ROOT%{_bindir}/

# Useful development tools
install -m755 -d $RPM_BUILD_ROOT%{tools_dir}/scripts
install Tools/README $RPM_BUILD_ROOT%{tools_dir}/
install Tools/scripts/*py $RPM_BUILD_ROOT%{tools_dir}/scripts/

# Documentation tools
install -m755 -d $RPM_BUILD_ROOT%{doc_tools_dir}
#install -m755 Doc/tools/mkhowto $RPM_BUILD_ROOT%{doc_tools_dir}

# Useful demo scripts
install -m755 -d $RPM_BUILD_ROOT%{demo_dir}
cp -ar Demo/* $RPM_BUILD_ROOT%{demo_dir}

# Get rid of crap
find $RPM_BUILD_ROOT/ -name "*~"|xargs rm -f
find $RPM_BUILD_ROOT/ -name ".cvsignore"|xargs rm -f
find $RPM_BUILD_ROOT/ -name "*.bat"|xargs rm -f
find . -name "*~"|xargs rm -f
find . -name ".cvsignore"|xargs rm -f
#zero length
rm -f $RPM_BUILD_ROOT%{site_packages}/modulator/Templates/copyright

rm -f $RPM_BUILD_ROOT%{pylibdir}/LICENSE.txt


#make the binaries install side by side with the main python
%if !%{main_python}
pushd $RPM_BUILD_ROOT%{_bindir}
mv idle idle%{__python_ver}
mv modulator modulator%{__python_ver}
mv pynche pynche%{__python_ver}
mv pygettext.py pygettext%{__python_ver}.py
mv msgfmt.py msgfmt%{__python_ver}.py
mv smtpd.py smtpd%{__python_ver}.py
mv pydoc pydoc%{__python_ver}
popd
%endif

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Fix for bug #136654
rm -f $RPM_BUILD_ROOT%{pylibdir}/email/test/data/audiotest.au $RPM_BUILD_ROOT%{pylibdir}/test/audiotest.au

# Fix bug #143667: python should own /usr/lib/python2.x on 64-bit machines
%if "%{_lib}" == "lib64"
install -d $RPM_BUILD_ROOT/usr/lib/python%{pybasever}/site-packages
%endif

# Make python-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch ppc64 s390x x86_64 ia64 alpha sparc64
%global _pyconfig_h %{_pyconfig64_h}
%else
%global _pyconfig_h %{_pyconfig32_h}
%endif
mv $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/pyconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/%{_pyconfig_h}
cat > $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%{_pyconfig32_h}"
#elif __WORDSIZE == 64
#include "%{_pyconfig64_h}"
#else
#error "Unknown word size"
#endif
EOF
ln -s ../../libpython%{pybasever}.so $RPM_BUILD_ROOT%{pylibdir}/config/libpython%{pybasever}.so

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" $RPM_BUILD_ROOT%{pylibdir}/distutils/sysconfig.py

# Get rid of egg-info files (core python modules are installed through rpms)
rm $RPM_BUILD_ROOT%{pylibdir}/*.egg-info

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd $RPM_BUILD_ROOT/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

# Copy up the gdb hooks into place; the python file will be autoloaded by gdb
# when visiting libpython.so, provided that the python file is installed to the
# same path as the library (or its .debug file) plus a "-gdb.py" suffix, e.g:
#  /usr/lib/debug/usr/lib64/libpython2.6.so.1.0.debug-gdb.py
# (note that the debug path is /usr/lib/debug for both 32/64 bit)
# 
# Initially I tried:
#  /usr/lib/libpython2.6.so.1.0-gdb.py
# but doing so generated noise when ldconfig was rerun (rhbz:562980)
#
%if 0%{?with_gdb_hooks}
%global dir_holding_gdb_py %{_prefix}/lib/debug/%{_libdir}
%global path_of_gdb_py %{dir_holding_gdb_py}/%{py_INSTSONAME}.debug-gdb.py

mkdir -p %{buildroot}%{dir_holding_gdb_py}
cp %{SOURCE1} %{buildroot}%{path_of_gdb_py}

# Manually byte-compile the file, in case find-debuginfo.sh is run before
# brp-python-bytecompile, so that the .pyc/.pyo files are properly listed in
# the debuginfo manifest:
LD_LIBRARY_PATH=. ./python -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"

LD_LIBRARY_PATH=. ./python -O -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"
%endif # with_gdb_hooks

#
# Systemtap hooks:
#
%if 0%{?with_systemtap}
# Install a tapset for this libpython into tapsetdir, fixing up the path to the
# library:
mkdir -p %{buildroot}%{tapsetdir}
%ifarch ppc64 s390x x86_64 ia64 alpha sparc64
%global libpython_stp libpython%{pybasever}-64.stp
%else
%global libpython_stp libpython%{pybasever}-32.stp
%endif

sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME}|" \
   %{SOURCE3} \
   > %{buildroot}%{tapsetdir}/%{libpython_stp}

%endif # with_systemtap

%clean
rm -fr $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc LICENSE README
%{_bindir}/pydoc*
%{_bindir}/%{python}
%if %{main_python}
%{_bindir}/python2
%endif # main_python
%{_bindir}/python%{pybasever}
%{_mandir}/*/*

%dir %{pylibdir}
%dir %{dynload_dir}
%{dynload_dir}/Python-%{version}-py%{pybasever}.egg-info
%{dynload_dir}/_bisectmodule.so
%{dynload_dir}/_bsddb.so
%{dynload_dir}/_bytesio.so
%{dynload_dir}/_codecs_cn.so
%{dynload_dir}/_codecs_hk.so
%{dynload_dir}/_codecs_iso2022.so
%{dynload_dir}/_codecs_jp.so
%{dynload_dir}/_codecs_kr.so
%{dynload_dir}/_codecs_tw.so
%{dynload_dir}/_collectionsmodule.so
%{dynload_dir}/_csv.so
%{dynload_dir}/_ctypes.so
%{dynload_dir}/_curses.so
%{dynload_dir}/_curses_panel.so
%{dynload_dir}/_elementtree.so
%{dynload_dir}/_fileio.so
%{dynload_dir}/_functoolsmodule.so
%{dynload_dir}/_hashlib.so
%{dynload_dir}/_heapq.so
%{dynload_dir}/_hotshot.so
%{dynload_dir}/_json.so
%{dynload_dir}/_localemodule.so
%{dynload_dir}/_lsprof.so
%{dynload_dir}/_multibytecodecmodule.so
%{dynload_dir}/_multiprocessing.so
%{dynload_dir}/_randommodule.so
%{dynload_dir}/_socketmodule.so
%{dynload_dir}/_sqlite3.so
%{dynload_dir}/_ssl.so
%{dynload_dir}/_struct.so
%{dynload_dir}/_weakref.so
%{dynload_dir}/arraymodule.so
%{dynload_dir}/audioop.so
%{dynload_dir}/binascii.so
%{dynload_dir}/bz2.so
%{dynload_dir}/cPickle.so
%{dynload_dir}/cStringIO.so
%{dynload_dir}/cmathmodule.so
%{dynload_dir}/_cryptmodule.so
%{dynload_dir}/datetime.so
%{dynload_dir}/dbm.so
%{dynload_dir}/dlmodule.so
%{dynload_dir}/fcntlmodule.so
%{dynload_dir}/future_builtins.so
%{dynload_dir}/gdbmmodule.so
%{dynload_dir}/grpmodule.so
%{dynload_dir}/imageop.so
%{dynload_dir}/itertoolsmodule.so
%{dynload_dir}/linuxaudiodev.so
%{dynload_dir}/mathmodule.so
%{dynload_dir}/mmapmodule.so
%{dynload_dir}/nismodule.so
%{dynload_dir}/operator.so
%{dynload_dir}/ossaudiodev.so
%{dynload_dir}/parsermodule.so
%{dynload_dir}/pyexpat.so
%{dynload_dir}/readline.so
%{dynload_dir}/resource.so
%{dynload_dir}/selectmodule.so
%{dynload_dir}/spwdmodule.so
%{dynload_dir}/stropmodule.so
%{dynload_dir}/syslog.so
%{dynload_dir}/termios.so
%{dynload_dir}/timemodule.so
%{dynload_dir}/timingmodule.so
%{dynload_dir}/unicodedata.so
%{dynload_dir}/xxsubtype.so
%{dynload_dir}/zlibmodule.so

%dir %{site_packages}
%{site_packages}/README
%{pylibdir}/*.py*
%{pylibdir}/*.doc
%dir %{pylibdir}/bsddb
%{pylibdir}/bsddb/*.py*
%{pylibdir}/compiler
%dir %{pylibdir}/ctypes
%{pylibdir}/ctypes/*.py*
%{pylibdir}/ctypes/macholib
%{pylibdir}/curses
%dir %{pylibdir}/distutils
%{pylibdir}/distutils/*.py*
%{pylibdir}/distutils/README
%{pylibdir}/distutils/command
%dir %{pylibdir}/email
%{pylibdir}/email/*.py*
%{pylibdir}/email/mime
%{pylibdir}/encodings
%{pylibdir}/hotshot
%{pylibdir}/idlelib
%dir %{pylibdir}/json
%{pylibdir}/json/*.py*
%{pylibdir}/lib2to3
%exclude %{pylibdir}/lib2to3/tests
%{pylibdir}/logging
%{pylibdir}/multiprocessing
%{pylibdir}/plat-linux2
%dir %{pylibdir}/sqlite3
%{pylibdir}/sqlite3/*.py*
%dir %{pylibdir}/test
%{pylibdir}/test/test_support.py*
%{pylibdir}/test/__init__.py*
%{pylibdir}/wsgiref
%{pylibdir}/xml
%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}/site-packages
%endif
# "Makefile" and the config-32/64.h file are needed by
# distutils/sysconfig.py:_init_posix(), so we include them in the core
# package, along with their parent directories (bug 531901):
%dir %{pylibdir}/config
%{pylibdir}/config/Makefile
%dir %{_includedir}/python%{pybasever}
%{_includedir}/python%{pybasever}/%{_pyconfig_h}

%if 0%{?with_systemtap}
%{tapsetdir}/%{libpython_stp}
%doc systemtap-example.stp pyfuntop.stp
%endif

%files libs
%defattr(-,root,root, -)
%doc LICENSE README
%{_libdir}/%{py_INSTSONAME}

%files devel
%defattr(-,root,root, -)
%{pylibdir}/config/*
%exclude %{pylibdir}/config/Makefile
%{_includedir}/python%{pybasever}/*.h
%exclude %{_includedir}/python%{pybasever}/%{_pyconfig_h}
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%{_bindir}/python-config
%{_bindir}/python%{pybasever}-config
%{_libdir}/libpython%{pybasever}.so

%files tools
%defattr(-,root,root,755)
%doc Tools/modulator/README.modulator
%doc Tools/pynche/README.pynche
%{site_packages}/modulator
%{site_packages}/pynche
%{_bindir}/smtpd*.py*
%{_bindir}/2to3*
%{_bindir}/idle*
%{_bindir}/modulator*
%{_bindir}/pynche*
%{_bindir}/pygettext*.py*
%{_bindir}/msgfmt*.py*
%{tools_dir}
%{demo_dir}
%{pylibdir}/Doc

%files -n %{tkinter}
%defattr(-,root,root,755)
%{pylibdir}/lib-tk
%{dynload_dir}/_tkinter.so

%files test
%defattr(-, root, root, -)
%{pylibdir}/bsddb/test
%{pylibdir}/ctypes/test
%{pylibdir}/distutils/tests
%{pylibdir}/email/test
%{pylibdir}/json/tests
%{pylibdir}/lib2to3/tests
%{pylibdir}/sqlite3/test
%{pylibdir}/test
%{dynload_dir}/_ctypes_test.so
%{dynload_dir}/_testcapimodule.so

# We put the debug-gdb.py file inside /usr/lib/debug to avoid noise from
# ldconfig (rhbz:562980).
# 
# The /usr/lib/rpm/redhat/macros defines %__debug_package to use
# debugfiles.list, and it appears that everything below /usr/lib/debug and
# (/usr/src/debug) gets added to this file (via LISTFILES) in
# /usr/lib/rpm/find-debuginfo.sh
# 
# Hence by installing it below /usr/lib/debug we ensure it is added to the
# -debuginfo subpackage
# (if it doesn't, then the rpmbuild ought to fail since the debug-gdb.py 
# payload file would be unpackaged)

%changelog
* Sun Dec  9 2012 Alan Iwi <alan.iwi@stfc.ac.uk> - 2.7.3.1.ceda
- put in 2.7 sources

* Tue Aug 28 2012 David Malcolm <dmalcolm@redhat.com> - 2.6.6-29.el6_3.3
- add an RPATH to pyexpat.so to avoid ImportError on XML_SetHashSalt when a
vanilla build of expat is present in LD_LIBRARY_PATH
Resolves: rhbz#833271

* Tue May  1 2012 David Malcolm <dmalcolm@redhat.com> - 2.6.6-29.el6_2.2
- if hash randomization is enabled, also enable it within pyexpat
Resolves: CVE-2012-0876

* Wed Mar 28 2012 David Malcolm <dmalcolm@redhat.com> - 2.6.6-29.el6_2.1
- distutils.config: create ~/.pypirc securely
Resolves: CVE-2011-4944
- fix endless loop in SimpleXMLRPCServer upon malformed POST request
Resolves: CVE-2012-0845
- send encoding in SimpleHTTPServer.list_directory to protect IE7 against
potential XSS attacks
Resolves: CVE-2011-4940
- oCERT-2011-003: add -R command-line option and PYTHONHASHSEED environment
variable, to provide an opt-in way to protect against denial of service
attacks due to hash collisions within the dict and set types
Resolves: CVE-2012-1150

* Mon Sep 12 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-29
- protect GIL detection within gdb debug hooks against C stack frames that
lack a name (source 1)
Related: rhbz#711818
Resolves: rhbz#736085

* Mon Aug 15 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-28
- avoid truncating the compilation flags of extension modules that have CFLAGS
set in their environment
Resolves: rhbz#727364

* Fri Aug 12 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-27
- update "py-bt" in gdb debug hooks to avoiding printing stray <function>
frames on non-C functions
Related: rhbz#711818

* Fri Aug 12 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-26
- update patch 147 to cover the pwd and grp modules
Related: rhbz#697470

* Fri Jul 22 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-25
- remove -b from application of patch 147, to avoid adding files to payload
Related: rhbz#697470

* Fri Jul 22 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-24
- update uid/gid handling to avoid int overflows seen with uid/gid
values >= 2^31 on 32-bit architectures
Resolves: rhbz#697470

* Thu Jul 21 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-23
- update gdb debug hooks, showing when a thread is waiting on the GIL, calls
to C functions and methods, and garbage collections.  Also, better handle the
case when "f" is optimized out within PyEval_EvalFrameEx, to at least give
file and function name, even if the line number and locals won't be available
Resolves: rhbz#711818

* Fri Jul  1 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-22
- backport fix for failures seen with subprocess module when supplying stdin
to short-lived subprocesses
Resolves: rhbz#667431

* Thu Jun 30 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-21
- backport fix for occasional failures in multiprocessing's Process.start()
Resolves: rhbz#685234
- port multiprocessing to use the "poll" syscall, rather than "select"
Resolves: rhbz#713082
- backport fix allowing getpass.getpass() to be interrupted with Ctrl-C
or Ctrl-Z
Resolves: rhbz#689794
- backport memory leak fixes for the readline module
Resolves: rhbz#699740

* Mon Apr 11 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-20
Resolves: CVE-2010-3493

* Fri Apr  8 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-19
Resolves: CVE-2011-1015

* Thu Apr  7 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-18
Resolves: CVE-2011-1521

* Fri Mar 25 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-17
- recompile against systemtap 1.4
Related: rhbz#569695

* Wed Mar 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-16
- recompile against systemtap 1.4
Related: rhbz#569695

* Wed Mar 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-15
- fix race condition that sometimes breaks the build with parallel make
Resolves: rhbz#690315

* Wed Mar 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-14
- backport pre-canned ways of salting a password to the "crypt" module
Resolves: rhbz#681878

* Mon Mar 21 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-13
- move lib2to3/tests to the python-test subpackage
Related: rhbz#625395

* Mon Mar 21 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-12
- fix a new test in 2.6.6 that was failing on 64-bit big-endian architectures
Resolves: rhbz#677392

* Mon Mar 21 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-11
- fix incompatibility between 2.6.6 and our non-standard M2Crypto.SSL.SSLTimeoutError
Resolves: rhbz#681811

* Mon Mar 21 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-10
- add workaround for bug in rhythmbox-0.12 exposed by python 2.6.6
Resolves: rhbz#684991

* Wed Jan 19 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-9
- prevent tracebacks for the "py-bt" gdb command on x86_64
Resolves: rhbz#639392

* Wed Jan 19 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-8
- fix a regression in 2.6.6 relative to 2.6.5 in urllib2
Resolves: rhbz#669847

* Wed Jan 19 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-7
- add an optional "timeout" argument to the subprocess module (patch 131)
Resolves: rhbz#567229

* Mon Jan 17 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-6
- prevent _sqlite3.so being built with a redundant RPATH of _libdir (patch 130)
- remove DOS batch file "idle.bat"
- remove shebang lines from .py files that aren't executable, and remove
executability from .py files that don't have a shebang line
Related: rhbz#634944
- add "Obsoletes: python-ssl" to core package, as 2.6 contains the ssl module
Resolves: rhbz#529274

* Tue Jan 11 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-5
- allow the "no_proxy" environment variable to override "ftp_proxy" in
urllib2 (patch 128)
Resolves: rhbz#637895
- make garbage-collection assertion failures more informative (patch 129)
Resolves: rhbz#614680

* Tue Jan 11 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-4
- backport subprocess fixes to use the "poll" system call, rather than "select"
Resolves: rhbz#650588

* Mon Jan 10 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-3
- use an ephemeral port for IDLE, enabling multiple instances to be run
Resolves: rhbz#639222
- add systemtap static markers, tapsets, and example scripts
Resolves: rhbz#569695

* Mon Jan 10 2011 David Malcolm <dmalcolm@redhat.com> - 2.6.6-2
- fix dbm.release on ppc64/s390x
Resolves: rhbz#626756
- fix missing lib2to3 test files
Resolves: rhbz#625395
- fix test.test_commands SELinux incompatibility
Resolves: rhbz#625393
- make "pydoc -k" more robust in the face of broken modules
Resolves: rhbz#603073

* Mon Nov 29 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.6-1
- rebase to 2.6.6: (which contains the big whitespace cleanup of r81031)
  http://www.python.org/download/releases/2.6.6/
  - fixup patch 102, patch 11, patch 52, patch 110
  - drop upstreamed patches: patch 113 (CVE-2010-1634), patch 114
  (CVE-2010-2089), patch 115 (CVE-2008-5983), patch 116 (rhbz598564),
  patch 118 (rhbz540518)
  - add fix for upstream bug in test_posix.py introduced in 2.6.6 (patch 120)
Resolves: rhbz#627301

* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-3
- slightly rework patch 119 to fix the hashlib selftests in FIPS mode
Resolves: rhbz#563986

* Tue Jul 13 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-2
- support OpenSSL FIPS mode in _hashlib and hashlib
Resolves: rhbz#563986
- don't build the _md5 and _sha* modules: rely on _hashlib in hashlib

* Mon Jul 12 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-1
- 2.6.5
- remove upstream patch 53
- fixup selinux patch to apply cleanly against 2.6.5 (patch 110)
Resolves: rhbz#611607
- remove commented-out, out-of-date patches

* Tue Jun 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-11
- Stop python bailing out with an assertion failure when UnicodeDecodeErrors
occur on very large buffers (patch 118, upstream issue 9058)
Resolves: rhbz#540518

* Mon Jun 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-10
- Fix an incompatibility between pyexpat and the system expat-2.0.1 that led to
a segfault running test_pyexpat.py (patch 117)
Resolves: rhbz#583931

* Tue Jun  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-9
- cherrypick upstream fix for fatal error creating threads when memory is
low (patch 116)
Resolves: rhbz#598564

* Thu Jun  3 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-8
- ensure that the compiler is invoked with "-fwrapv" (rhbz#594819)
- CVE-2010-1634: fix various integer overflow checks in the audioop
module (patch 113)
- CVE-2010-2089: further checks within the audioop module (patch 114)
- CVE-2008-5983: the new PySys_SetArgvEx entry point from r81399 (patch 115)

* Wed May 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-7
- add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
(patch 112)

* Thu Apr 29 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-6
- add gdb hooks for easier debugging (rhbz:569696)
- supply fourth parameter (default permissions) in all usage of "defattr" in
subpackage manifests
- remove trailing periods from package "Summary" fields
- fix typo in the description of the "test" subpackage

* Mon Jan 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-5
- update python-2.6.2-config.patch to remove downstream customization of build
of pyexpat and elementtree modules
- add patch adapted from upstream (patch 3) to add support for building against
system expat; add --with-system-expat to "configure" invocation (patch 3)
- remove embedded copy of expat from source tree during "prep"

* Mon Jan 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-4
- introduce %%{with_valgrind} macro, to only use the valgrind patch on archs
where valgrind-devel is available

* Tue Jan 19 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.2-3
- replace usage of %%define with %%global
- introduce macros for 3 directories, replacing expanded references throughout:
%%{pylibdir}, %%{dynload_dir}, %%{site_packages}
- split up the "configure" invocation flags onto individual lines
- move lib2to3 from -tools subpackage to main package (bug 556667)
- "Makefile" and the config-32/64.h file are needed by distutils/sysconfig.py
_init_posix(), so we include them in the core package, along with their parent
directories (bug 531901)
- fixup the build when __python_ver is set (Zach Sadecki; bug 533989); use
pybasever in the files section
- automatically disable arena allocator when run under valgrind (upstream
issue 2422; patch 52)
- fix Lib/SocketServer.py to avoid trying to use non-existant keyword args
for os.waitpid (patch 53, rhbz:552404, Adrian Reber)
- use the %%{_isa} macro to ensure that the python-devel dependency on python
is for the correct multilib arch (#555943)
- patch Makefile.pre.in to avoid building static library (patch111, bug 556092)
- delete bundled copies of libffi and zlib to make sure we use the system ones
- replace references to /usr with %%{_prefix}; replace references to
/usr/include with %%{_includedir}
- change python-2.6.2-config.patch to remove our downstream change to curses
configuration in Modules/Setup.dist, so that the curses modules are built using
setup.py with the downstream default (linking against libncursesw.so, rather
than libncurses.so), rather than within the Makefile; add a test to %%install
to verify the dso files that the curses module is linked against the correct
DSO (bug 539917; changes _cursesmodule.so -> _curses.so)
- explicitly list all lib-dynload files, rather than dynamically gathering the
payload into a temporary text file, so that we can be sure what we are
shipping; remove now-redundant testing for presence of certain .so files

* Mon Nov 23 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.6.2-2.1
- Rebuilt for RHEL 6

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.6.2-2
- rebuilt with new openssl

* Mon Jul 27 2009 James Antill <james.antill@redhat.com> - 2.6.2-1
- Update to 2.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 4 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.6-10
- Move python-config to devel subpackage (#506153)
- Update BuildRoot for new standard

* Sun Jun 28 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.6-9
- Update python-tools description (#448940)

* Wed Apr 15 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.6-8
- Replace python-hashlib and python-uuid (#484715)

* Tue Mar 17 2009 James Antill <james@fedoraproject.org> - 2.6-7
- Use system libffi
- Resolves: bug#490573
- Fix SELinux execmem problems
- Resolves: bug#488396

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.6-4
- rebuild with new openssl

* Tue Jan  6 2009 James Antill <james.antill@redhat.com> - 2.6-3
- Fix distutils generated rpms.
- Resolves: bug#236535

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.6-2
- Enable -lcrypt for cryptmodule

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.6-1
- Update to 2.6

* Tue Sep 30 2008 James Antill <james.antill@redhat.com> - 2.5.2-1
- Move to 2.5.2
- Fix CVE-2008-2316 hashlib overflow.

* Thu Jul 17 2008 Jeremy Katz <katzj@redhat.com> - 2.5.1-30
- Fix up the build for new rpm
- And actually build against db4-4.7 (#455170)

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-27
- fix license tag
- enable support for db4-4.7

* Sun Jun 15 2008 James Antill <jantill@redhat.com> - 2.5.1-26
- Fix sporadic listdir problem
- Resolves: bug#451494

* Mon Apr  7 2008 James Antill <jantill@redhat.com> - 2.5.1-25
- Rebuild to re-gen autoconf file due to glibc change.
- Resolves: bug#441003

* Tue Mar 25 2008 James Antill <jantill@redhat.com> - 2.5.1-24
- Add more constants to socketmodule

* Sat Mar  8 2008 James Antill <jantill@redhat.com> - 2.5.1-22
- Add constants to socketmodule
- Resolves: bug#436560

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.1-22
- Autorebuild for GCC 4.3

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-21
- rebuild for new tk in rawhide

* Mon Jan  7 2008 James Antill <jantill@redhat.com> - 2.5.1-20
- Add valgrind support files, as doc, to python-devel
- Relates: rhbz#418621
- Add new API from 2.6, set_wakeup_fd ... use at own risk, presumably won't
- change but I have no control to guarantee that.
- Resolves: rhbz#427794
- Add gdbinit support file, as doc, to python-devel

* Fri Jan  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-19
- rebuild for new tcl/tk in rawhide

* Fri Dec  7 2007 James Antill <jantill@redhat.com> - 2.5.1-18
- Create a python-test sub-module, over 3MB of stuff noone wants.
- Don't remove egginfo files, try this see what happens ... may revert.
- Resolves: rhbz#414711

* Mon Dec  3 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-17
- rebuild for new libssl

* Fri Nov 30 2007 James Antill <jantill@redhat.com> - 2.5.1-16
- Fix pyconfig.h comment typo.
- Add back test_support.py and the __init__.py file.
- Resolves: rhbz#387401

* Tue Oct 30 2007 James Antill <jantill@redhat.com> - 2.5.1-15
- Do codec lowercase in C Locale.
- Resolves: 207134 191096
- Fix stupid namespacing in pysqlite, minimal upgrade to 2.3.3 pysqlite
- Resolves: 263221

* Wed Oct 24 2007 James Antill <jantill@redhat.com> - 2.5.1-14
- Remove bintuils dep. for live CD ... add work around for ctypes

* Mon Oct 22 2007 James Antill <jantill@redhat.com> - 2.5.1-13
- Add tix buildprereq
- Add tkinter patch
- Resolves: #281751
- Fix ctypes loading of libraries, add requires on binutils
- Resolves: #307221
- Possible fix for CVE-2007-4965 possible exploitable integer overflow
- Resolves: #295971

* Tue Oct 16 2007 Mike Bonnet <mikeb@redhat.com> - 2.5.1-12
- fix marshalling of objects in xmlrpclib (python bug #1739842)

* Fri Sep 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-11
- fix encoding of sqlite .py files to work around weird encoding problem 
  in Turkish (#283331)

* Mon Sep 10 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-10
- work around problems with multi-line plural specification (#252136)

* Tue Aug 28 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-9
- rebuild against new expat

* Tue Aug 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-8
- build against db4.6

* Tue Aug 14 2007 Dennis Gilmore <dennis@ausil.us> - 2.5.1-7
- add sparc64 to the list of archs for _pyconfig64_h

* Fri Aug 10 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-6
- fix ctypes again on some arches (Hans de Goede, #251637)

* Fri Jul  6 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-5
- link curses modules with ncursesw (#246385)

* Wed Jun 27 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-4
- fix _elementtree.so build (#245703)
- ensure that extension modules we expect are actually built rather than 
  having them silently fall out of the package

* Tue Jun 26 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-3
- link with system expat (#245703)

* Thu Jun 21 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-2
- rebuild to take advantage of hardlinking between identical pyc/pyo files

* Thu May 31 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-1
- update to python 2.5.1

* Mon Mar 19 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-12
- fix alpha build (#231961)

* Tue Feb 13 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-11
- tcl/tk was reverted; rebuild again

* Thu Feb  1 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-10
- rebuild for new tcl/tk

* Tue Jan 16 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.5.3-9
- link with ncurses

* Sat Jan  6 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-8
- fix extensions to use shared libpython (#219564)
- all 64bit platforms need the regex fix (#122304)

* Wed Jan  3 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-7
- fix ctypes to not require execstack (#220669)

* Fri Dec 15 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-6
- don't link against compat-db (Robert Scheck)

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> - 2.5.3-5
- fix invalid assert in debug mode (upstream changeset 52622)

* Tue Dec 12 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-4
- obsolete/provide python-ctypes (#219256)

* Mon Dec 11 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-3
- fix atexit traceback with failed syslog logger (#218214)
- split libpython into python-libs subpackage for multilib apps 
  embedding python interpreters

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-2
- disable installation of .egg-info files for now

* Tue Dec  5 2006 Jeremy Katz <katzj@redhat.com>
- support db 4.5
- obsolete python-elementtree; since it requires some code tweaks, don't 
  provide it
- obsolete old python-sqlite; provide the version that's actually included

* Mon Oct 30 2006 Jeremy Katz <katzj@redhat.com>
- fix _md5 and _sha modules (Robert Sheck)
- no longer provide optik compat; it's been a couple of years now
- no longer provide the old shm module; if this is still needed, let's 
  build it separately
- no longer provide japanese codecs; should be a separate package

* Mon Oct 23 2006 Jeremy Katz <katzj@redhat.com> - 2.5-0
- update to 2.5.0 final

* Fri Aug 18 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.c1
- Updated to 2.5c1. Merged fixes from FC6 too:
- Fixed bug #199373 (on some platforms CFLAGS is needed when linking)
- Fixed bug #198971 (case conversion not locale safe in logging library)
- Verified bug #201434 (distutils.sysconfig is confused by the change to make
  python-devel multilib friendly) is fixed upstream

* Sun Jul 16 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.b2
- Updated to 2.5b2 (which for comparison reasons is re-labeled 2.4.99.b2)

* Fri Jun 23 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.b1
- Updated to 2.5b1 (which for comparison reasons is re-labeled 2.4.99.b1)

* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-11.FC6
- and fix it for real

* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-10.FC6
- fix python-devel on ia64

* Tue Jun 13 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-9
- Fixed python-devel to be multilib friendly (bug #192747, #139911)

* Tue Jun 13 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-8
- Only copying mkhowto from the Docs - we don't need perl dependencies from
  python-tools.

* Mon Jun 12 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-7
- Fixed bug #121198 (webbrowser.py should use the user's preferences first)

* Mon Jun 12 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-6
- Fixed bug #192592 (too aggressive assertion fails) - SF#1257960
- Fixed bug #167468 (Doc/tools not included) - added in the python-tools package

* Thu Jun  8 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-5
- Fixed bug #193484 (added pydoc in the main package)

* Mon Jun  5 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-4
- Added dist in the release

* Mon May 15 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-3
- rebuilt to fix broken libX11 dependency

* Wed Apr 12 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-2
- rebuild with new gcc to fix #188649

* Thu Apr  6 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-1
- Updated to 2.4.3

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-3.2.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-3.2
- rebuilt for newer tix

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 20 2006 Mihai Ibanescu <misa@redhat.com> 2.4.2-3
- fixed #136654 for another instance of audiotest.au

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 19 2005 Bill Nottingham <notting@redhat.com> 2.4.2-2
- fix build for modular X, remove X11R6 path references

* Tue Nov 15 2005 Mihai Ibanescu <misa@redhat.com> 2.4.2-1
- Upgraded to 2.4.2
- BuildRequires autoconf

* Wed Nov  9 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-16
- Rebuilding against newer openssl.
- XFree86-devel no longer exists

* Mon Sep 26 2005 Peter Jones <pjones@redhat.com> 2.4.1-14
- Once more -- this time, to fix -EPERM when you run it in a directory
  you can't read from.

* Mon Sep 26 2005 Peter Jones <pjones@redhat.com> 2.4.1-13
- So, 5 or 6 people have said it works for them with this patch...

* Sun Sep 25 2005 Peter Jones <pjones@redhat.com> 2.4.1-12
- Fixed bug #169159 (check for argc>0 and argv[0] == NULL, not just
    argv[0][0]='\0')
  Reworked the patch from -8 a bit more.

* Fri Sep 23 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-10
- Fixed bug #169159 (don't let python core dump if no arguments are passed in)
  Reworked the patch from -8 a bit more.

* Thu Sep 22 2005 Peter Jones <pjones@redhat.com> 2.4.1-8
- Fix bug #169046 more correctly.

* Thu Sep 22 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-7
- Fixed bug #169046 (realpath is unsafe); thanks to 
  Peter Jones <pjones@redhat.com> and Arjan van de Ven <arjanv@redhat.com> for
  diagnosing and the patch.

* Tue Sep 20 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-4
- Fixed bug #168655 (fixes for building as python24)

* Tue Jul 26 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-3
- Fixed bug #163435 (pynche doesn't start))

* Wed Apr 20 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-2
- Fixed bug #143667 (python should own /usr/lib/python* on 64-bit systems, for
  noarch packages)
- Fixed bug #143419 (BuildRequires db4 is not versioned)

* Wed Apr  6 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-1
- updated to 2.4.1

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 2.4-6
- building the docs from a different source rpm, to decouple bootstrapping
  python from having tetex installed

* Fri Mar 11 2005 Dan Williams <dcbw@redhat.com> 2.4-5
- Rebuild to pick up new libssl.so.5

* Wed Feb  2 2005 Mihai Ibanescu <misa@redhat.com> 2.4-4
- Fixed security issue in SimpleXMLRPCServer.py (#146647)

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 2.4-3
- Rebuilt for new readline.

* Mon Dec  6 2004 Jeff Johnson <jbj@jbj.org> 2.4-2
- db-4.3.21 returns DB_BUFFER_SMALL rather than ENOMEM (#141994).
- add Provide: python(abi) = 2.4
- include msgfmt/pygettext *.pyc and *.pyo from brp-python-bytecompile.

* Fri Dec  3 2004 Mihai Ibanescu <misa@redhat.com> 2.4-1
- Python-2.4.tar.bz2 (final)

* Fri Nov 19 2004 Mihai Ibanescu <misa@redhat.com> 2.4-0.c1.1
- Python-2.4c1.tar.bz2 (release candidate 1)

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 2.4-0.b2.4
- rebuild against db-4.3.21.

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 2.4-0.b2.3
- fix the lib64 patch so that 64bit arches still look in /usr/lib/python...

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 2.4-0.b2.2
- cryptmodule still needs -lcrypt (again)

* Thu Nov  4 2004 Mihai Ibanescu <misa@redhat.com> 2.4-0.b2.1
- Updated to python 2.4b2 (and labeled it 2.4-0.b2.1 to avoid breaking rpm's
  version comparison)

* Thu Nov  4 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-13
- Fixed bug #138112 (python overflows stack buffer) - SF bug 105470

* Tue Nov  2 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-12
- Fixed bugs #131439 #136023 #137863 (.pyc/.pyo files had the buildroot added)

* Tue Oct 26 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-11
- Fixed bug #136654 (python has sketchy audio clip)

* Tue Aug 31 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-10
- Fixed bug #77418 (Demo dir not packaged)
- More tweaking on #19347 (Moved Tools/ under /usr/lib/python2.3/Tools)

* Fri Aug 13 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-8
- Fixed bug #129769: Makefile in new python conflicts with older version found
  in old python-devel
- Reorganized the spec file to get rid of the aspython2 define; __python_ver
  is more powerful.

* Tue Aug  3 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-7
- Including html documentation for non-i386 arches
- Fixed #125362 (python-doc html files have japanese character encoding)
- Fixed #128923 (missing dependency between python and python-devel)

* Fri Jul 30 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-6
- Fixed #128030 (help() not printing anything)
- Fixed #125472 (distutils.sysconfig.get_python_lib() not returning the right
  path on 64-bit systems)
- Fixed #127357 (building python as a shared library)
- Fixed  #19347 (including the contents of Tools/scripts/ in python-tools)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  8 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-3
- Added an optik.py that provides the same interface from optparse for
  backward compatibility; obsoleting python-optik

* Mon Jun  7 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-2
- Patched bdist_rpm to allow for builds of multiple binary rpms (bug #123598)

* Fri Jun  4 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-1
- Updated to 2.3.4-1 with Robert Scheck's help (bug #124764)
- Added BuildRequires: tix-devel (bug #124918)

* Fri May  7 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-6
- Correct fix for #122304 from upstream:
  http://sourceforge.net/tracker/?func=detail&atid=105470&aid=931848&group_id=5470

* Thu May  6 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-4
- Fix for bug #122304 : splitting the domain name fails on 64-bit arches
- Fix for bug #120879 : including Makefile into the main package

- Requires XFree86-devel instead of -libs (see bug #118442)

* Tue Mar 16 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-3
- Requires XFree86-devel instead of -libs (see bug #118442)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Dec 19 2003 Jeff Johnson <jbj@jbj.org> 2.3.3-1
- upgrade to 2.3.3.

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 2.3.2-9
- rebuild against db-4.2.52.

* Fri Dec 12 2003 Jeremy Katz <katzj@redhat.com> 2.3.2-8
- more rebuilding for new tcl/tk

* Wed Dec  3 2003 Jeff Johnson <jbj@jbj.org> 2.3.2-7.1
- rebuild against db-4.2.42.

* Fri Nov 28 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-7
- rebuilt against newer tcl/tk

* Mon Nov 24 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-6
- added a Provides: python-abi

* Wed Nov 12 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-5
- force CC (#109268)

* Sun Nov  9 2003 Jeremy Katz <katzj@redhat.com> 2.3.2-4
- cryptmodule still needs -lcrypt

* Wed Nov  5 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-2
- Added patch for missing mkhowto

* Thu Oct 16 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-1
- Updated to 2.3.2

* Thu Sep 25 2003 Mihai Ibanescu <misa@redhat.com> 2.3.1-1
- 2.3.1 final

* Tue Sep 23 2003 Mihai Ibanescu <misa@redhat.com> 2.3.1-0.8.RC1
- Building the python 2.3.1 release candidate
- Updated the lib64 patch

* Wed Jul 30 2003 Mihai Ibanescu <misa@redhat.com> 2.3-0.2
- Building python 2.3
- Added more BuildRequires
- Updated the startup files for modulator and pynche; idle installs its own
  now.

* Thu Jul  3 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-4
- Rebuilt against newer db4 packages (bug #98539)

* Mon Jun 9 2003 Elliot Lee <sopwith@redhat.com> 2.2.3-3
- rebuilt

* Wed Jun  7 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-2
- Rebuilt

* Tue Jun  6 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-1
- Upgraded to 2.2.3

* Wed Apr  2 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-28
- Rebuilt

* Wed Apr  2 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-27
- Modified the ftpuri patch conforming to http://ietf.org/rfc/rfc1738.txt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-25
- Fixed bug #84886: pydoc dies when run w/o arguments
- Fixed bug #84205: add python shm module back (used to be shipped with 1.5.2)
- Fixed bug #84966: path in byte-compiled code still wrong

* Thu Feb 20 2003 Jeremy Katz <katzj@redhat.com> 2.2.2-23
- ftp uri's should be able to specify being rooted at the root instead of 
  where you login via ftp (#84692)

* Mon Feb 10 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-22
- Using newer Japanese codecs (1.4.9). Thanks to 
  Peter Bowen <pzb@datastacks.com> for pointing this out.

* Thu Feb  6 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-21
- Rebuild

* Wed Feb  5 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-20
- Release number bumped really high: turning on UCS4 (ABI compatibility
  breakage)

* Fri Jan 31 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-13
- Attempt to look both in /usr/lib64 and /usr/lib/python2.2/site-packages/:
  some work on python-2.2.2-lib64.patch

* Thu Jan 30 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-12
- Rebuild to incorporate the removal of .lib64 and - files.

* Thu Jan 30 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-11.7.3
- Fixed bug #82544: Errata removes most tools
- Fixed bug #82435: Python 2.2.2 errata breaks redhat-config-users
- Removed .lib64 and - files that get installed after we fix the multilib
  .py files.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Jens Petersen <petersen@redhat.com> 2.2.2-10
- rebuild to update tkinter's tcltk deps
- convert changelog to utf-8

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 2.2.2-9
- rebuild

* Fri Jan  3 2003 Nalin Dahyabhai <nalin@redhat.com>
- pick up OpenSSL cflags and ldflags from pkgconfig if available

* Thu Jan  2 2003 Jeremy Katz <katzj@redhat.com> 2.2.2-8
- urllib2 didn't support non-anonymous ftp.  add support based on how 
  urllib did it (#80676, #78168)

* Mon Dec 16 2002 Mihai Ibanescu <misa@redhat.com> 2.2.2-7
- Fix bug #79647 (Rebuild of SRPM fails if python isn't installed)
- Added a bunch of missing BuildRequires found while fixing the
  above-mentioned bug

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 2.2.2-6
- rebuild to fix broken tcltk deps for tkinter

* Fri Nov 22 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-3.7.3
- Recompiled for 7.3 (to fix the -lcrypt bug)
- Fix for the spurious error message at the end of the build (build-requires
  gets confused by executable files starting with """"): make the tests
  non-executable.

* Wed Nov 20 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-5
- Fixed configuration patch to add -lcrypt when compiling cryptmodule.c

2.2.2-4
- Spec file change from Matt Wilson <msw@redhat.com> to disable linking 
  with the C++ compiler.

* Mon Nov 11 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-3.*
- Merged patch from Karsten Hopp <karsten@redhat.de> from 2.2.1-17hammer to
  use %%{_libdir}
- Added XFree86-libs as BuildRequires (because of tkinter)
- Fixed duplicate listing of plat-linux2
- Fixed exclusion of lib-dynload/japanese
- Added lib64 patch for the japanese codecs
- Use setup magic instead of using tar directly on JapaneseCodecs

* Tue Nov  5 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-2
- Fix #76912 (python-tools contains idle, which uses tkinter, but there is no
  requirement of tkinter from python-tools).
- Fix #74013 (rpm is missing the /usr/lib/python2.2/test directory)

* Mon Nov  4 2002 Mihai Ibanescu <misa@redhat.com>
- builds as python2 require a different libdb
- changed the buildroot name of python to match python2 builds

* Fri Nov  1 2002 Mihai Ibanescu <misa@redhat.com>
- updated python to 2.2.2 and adjusted the patches accordingly

* Mon Oct 21 2002 Mihai Ibanescu <misa@redhat.com>
- Fix #53930 (Python-2.2.1-buildroot-bytecode.patch)
- Added BuildPrereq dependency on gcc-c++

* Fri Aug 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-17
- security fix for _execvpe

* Tue Aug 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-16
- Fix  #71011,#71134, #58157

* Wed Aug  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-15
- Resurrect tkinter
- Fix for distutils (#67671)
- Fix #69962

* Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-14
- Obsolete tkinter/tkinter2 (#69838)

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-13
- Doc fixes (#53951) - not on alpha at the momemt

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-12
- fix pydoc (#68082)

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-11
- Add db4-devel as a BuildPrereq

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.2.1-10
- automated rebuild

* Mon Jun 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-9
- Add Japanese codecs (#66352)

* Tue Jun 11 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-8
- No more tkinter...

* Wed May 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-7
- Rebuild

* Tue May 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-6
- Add the email subcomponent (#65301)

* Fri May 10 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-5
- Rebuild

* Thu May 02 2002 Than Ngo <than@redhat.com> 2.2.1-4
- rebuild i new enviroment

* Tue Apr 23 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Use ucs2, not ucs4, to avoid breaking tkinter (#63965)

* Mon Apr 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-2
- Make it use db4

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-1
- 2.2.1 - a bugfix-only release

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-16
- the same, but in builddirs - this will remove them from the 
  docs package, which doesn't look in the buildroot for files.

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-15
- Get rid of temporary files and .cvsignores included 
  in the tarball and make install

* Fri Apr  5 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-14
- Don't own lib-tk in main package, only in tkinter (#62753)

* Mon Mar 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-13
- rebuild

* Mon Mar 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-12
- rebuild

* Fri Mar  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-11
- Add a not to the Distutils obsoletes test (doh!)

* Fri Mar  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-10
- Rebuild

* Mon Feb 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-9
- Only obsolete Distutils when built as python

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-8
- Make files in /usr/bin install side by side with python 1.5 when
- Drop explicit requirement of db4
  built as python2

* Thu Jan 31 2002 Elliot Lee <sopwith@redhat.com> 2.2-7
- Use version and pybasever macros to make updating easy
- Use _smp_mflags macro

* Tue Jan 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-6
- Add db4-devel to BuildPrereq

* Fri Jan 25 2002 Nalin Dahyabhai <nalin@redhat.com> 2.2-5
- disable ndbm support, which is db2 in disguise (really interesting things
  can happen when you mix db2 and db4 in a single application)

* Thu Jan 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-4
- Obsolete subpackages if necesarry 
- provide versioned python2
- build with db4

* Wed Jan 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-3
- Alpha toolchain broken. Disable build on alpha.
- New openssl

* Wed Dec 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-1
- 2.2 final

* Fri Dec 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.11c1
- 2.2 RC 1
- Don't include the _tkinter module in the main package - it's 
  already in the tkiter packace
- Turn off the mpzmodule, something broke in the buildroot

* Wed Nov 28 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.10b2
- Use -fPIC for OPT as well, in lack of a proper libpython.so

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com> 2.2-0.9b2
- changed DESTDIR to point to / so that distutils will install dynload
  modules properly in the installroot

* Fri Nov 16 2001 Matt Wilson <msw@redhat.com> 2.2-0.8b2
- 2.2b2

* Fri Oct 26 2001 Matt Wilson <msw@redhat.com> 2.2-0.7b1
- python2ify

* Fri Oct 19 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.5b1
- 2.2b1

* Sun Sep 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.4a4
- 2.2a4
- Enable UCS4 support
- Enable IPv6
- Provide distutils
- Include msgfmt.py and pygettext.py

* Fri Sep 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.3a3
- Obsolete Distutils, which is now part of the main package
- Obsolete python2

* Thu Sep 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.2a3
- Add docs, tools and tkinter subpackages, to match the 1.5 layout

* Wed Sep 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.1a3
- 2.2a3
- don't build tix and blt extensions

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add tk and tix to build dependencies

* Sat Jul 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.1.1 bugfix release - with a GPL compatible license

* Fri Jul 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add new build dependencies (#49753)

* Tue Jun 26 2001 Nalin Dahyabhai <nalin@redhat.com>
- build with -fPIC

* Fri Jun  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.1
- reorganization of file includes

* Wed Dec 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix the "requires" clause, it lacked a space causing problems
- use %%{_tmppath}
- don't define name, version etc
- add the available patches from the Python home page

* Fri Dec 15 2000 Matt Wilson <msw@redhat.com>
- added devel subpackage

* Fri Dec 15 2000 Matt Wilson <msw@redhat.com>
- modify all files to use "python2.0" as the intrepter
- don't build the Expat bindings
- build against db1

* Mon Oct 16 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for 2.0 final

* Mon Oct  9 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for 2.0c1
- build audioop, imageop, and rgbimg extension modules
- include xml.parsers subpackage
- add test.xml.out to files list

* Thu Oct  5 2000 Jeremy Hylton <jeremy@beopen.com>
- added bin/python2.0 to files list (suggested by Martin v. L?)

* Tue Sep 26 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for release 1 of 2.0b2
- use .bz2 version of Python source

* Tue Sep 12 2000 Jeremy Hylton <jeremy@beopen.com>
- Version 2 of 2.0b1
- Make the package relocatable.  Thanks to Suchandra Thapa.
- Exclude Tkinter from main RPM.  If it is in a separate RPM, it is
  easier to track Tk releases.
