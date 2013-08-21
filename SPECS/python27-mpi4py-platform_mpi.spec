%define pname mpi4py
%define version 1.3

Summary: MPI for Python
Name: python27-%{pname}-platform_mpi
Version: %{version}
Release: 1.ceda
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Libraries/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: CIMEC <http://www.cimec.org.ar>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://mpi4py.googlecode.com/
Requires: python27 sct-platform-mpi 
BuildRequires: python27 sct-platform-mpi
AutoReq: no

# note AutoReq turned off because platform_mpi package 
# provides libmpio.so.1()(64bit) but does not properly
# record that in the RPM metadata, and we want to use 
# this without rebuilding that RPM.  The dependency on 
# sct-platform-mpi (which depends on platform_mpi) is 
# sufficient dependency. The only other dependencies
# found by AutoReq are libraries provided by glibc.


%description
This package provides Python bindings for the **Message Passing
Interface** (MPI) standard. It is implemented on top of the
MPI-1/MPI-2 specification and exposes an API which grounds on the
standard MPI-2 C++ bindings.

This package supports:

+ Convenient communication of any *picklable* Python object

  - point-to-point (send & receive)
  - collective (broadcast, scatter & gather, reduction)

+ Fast communication of Python object exposing the *Python buffer
  interface* (NumPy arrays, builtin bytes/string/array objects)

  - point-to-point (blocking/nonbloking/persistent send & receive)
  - collective (broadcast, block/vector scatter & gather, reduction)

+ Process groups and communication domains

  - Creation of new intra/inter communicators
  - Cartesian & graph topologies

+ Parallel input/output:

  - read & write
  - blocking/nonbloking & collective/noncollective
  - individual/shared file pointers & explicit offset

+ Dynamic process management

  - spawn & spawn multiple
  - accept/connect
  - name publishing & lookup

+ One-sided operations (put, get, accumulate)

You can install the `in-development version
<hg+http://code.google.com/p/mpi4py#egg=mpi4py-dev>`_
of mpi4py with::

  $ pip install mpi4py==dev

or::

  $ easy_install mpi4py==dev

%prep
%setup -n %{pname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build --mpicc=/opt/platform_mpi/bin/mpicc

%install
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt HISTORY.txt LICENSE.txt THANKS.txt
