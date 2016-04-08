Summary: Software for building and coupling weather, climate, and related models
Name: esmf-lotus
Version: 7.0.0b57
Release: 1.ceda%{?dist}
License: MIT
Group: Scientific support
URL: https://www.earthsystemcog.org/projects/esmf/
Source0: esmf_7_0_0beta_snapshot_57.tar.gz
Source1: ESMF-license
Source2: ESMF_6_3_0rp1_doc.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
# Noting that sct-platform-mpi is an STFC package that adds some scripts 
# around platform_mpi.  Only really needed for bits in /etc/profile.d and 
# /etc/ld.so.conf; the alternative is to set some environment variables
# at run-time: MPI_ROOT and LD_LIBRARY_PATH.
Requires: python27 sct-platform-mpi platform_mpi
Requires: netcdf-c++ netcdf-fortran lapack blas xerces-c
BuildRequires: python27 platform_mpi
BuildRequires: netcdf-c++-devel netcdf-fortran-devel lapack-devel blas-devel xerces-c-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: esmf

%define mpi_lib_dir /opt/platform_mpi/lib/linux_amd64

%description

The Earth System Modeling Framework (ESMF) collaboration is
high-performance, flexible software infrastructure for building and
coupling weather, climate, and related Earth science applications. The
ESMF defines an architecture for composing complex, coupled modeling
systems and includes data structures and utilities for developing
individual models.

The basic idea behind ESMF is that complicated applications should be
broken up into coherent pieces, or components, with standard calling
interfaces. In ESMF, a component may be a physical domain, or a
function such as a coupler or I/O system. ESMF also includes toolkits
for building components and applications, such as regridding software,
calendar management, logging and error handling, and parallel
communications.

=======================================================================
  This package was built to use platform_mpi for its parallelisation,
  for use on the STFC Lotus cluster.

  If attempting to use elsewhere, note that dynamic libraries from
     %{mpi_lib_dir}
  are used at run-time, so LD_LIBRARY_PATH may need to be set if 
  this directory has not been added to ld.so.conf.
=======================================================================

%package python27
Summary: Python 2.7 bindings for ESMF
Group: Scientific support
Requires: python27
Requires: %{name} = %{version}-%{release}
Provides: esmf-python27

%description python27
Python 2.7 bindings for the Earth System Modeling Framework software.
For more information see description of base package esmf.

%package doc
Summary: HTML documentation for ESMF
Group: Scientific support

%description doc
Documentation for the Earth System Modeling Framework software.


# in autoreqs, exclude libraries that platform_mpi provides 
# but which do not appear in the Provides metadata for platform_mpi
%filter_from_requires /libmpi\.so/d;/libmpiCC\.so/d;/libmpio\.so/d
%filter_setup


%prep
%setup -n esmf
perl -p -i -e 's,python ,python2.7 ,' src/addon/ESMPy/setup.py

%build

cat > envvars.sh <<EOF
export ESMF_OS="Linux"
export ESMF_COMM="user"

export ESMF_F90=/opt/platform_mpi/bin/mpif90
export ESMF_CXX=/opt/platform_mpi/bin/mpiCC
export ESMF_MPIRUN=/usr/local/bin/mpirun.lotus
export ESMF_MPIMPMDRUN=/opt/platform_mpi/bin/mpiexec

export ESMF_CXXCOMPILEOPTS=-fPIC
export ESMF_CXXLINKOPTS=-fPIC
export ESMF_CXXOPTFLAG=-O2
export ESMF_F90COMPILEOPTS=-fPIC
export ESMF_F90LINKOPTS=-fPIC
export ESMF_F90OPTFLAG=-O2

export ESMF_DIR=`pwd`
export ESMF_INSTALL_PREFIX=$RPM_BUILD_ROOT/usr/lib/esmf

export ESMF_NETCDF=split
export ESMF_NETCDF_INCLUDE=/usr/include
export ESMF_NETCDF_LIBPATH=/usr/lib64

export ESMF_LAPACK=netlib
export ESMF_LAPACK_LIBPATH=/usr/lib64

export ESMF_XERCES=standard
export ESMF_XERCES_INCLUDE=/usr/include
export ESMF_XERCES_LIBPATH=/usr/lib64
export ESMF_XERCES_LIBS=-lxerces-c


# LD_LIBRARY_PATH is needed here in the build (for use on the builder machine).
# At run-time, it should work without because nodes on Lotus have it set up 
# via /etc/ld.so.conf.d/pmpi.conf
export LD_LIBRARY_PATH=%{mpi_lib_dir} 
EOF

. ./envvars.sh

# build the main package
make

# and the python bindings
pushd ./src/addon/ESMPy/
python2.7 setup.py build --ESMFMKFILE=../../../lib/libO/Linux.gfortran.64.user.default/esmf.mk 
popd


%install
rm -rf $RPM_BUILD_ROOT

. ./envvars.sh

# install the main package
make install | tee install.log

# relink the executables that use -rpath so this points to the final destination without $RPM_BUILD_ROOT
rflag="-Wl,-rpath,"
rpath="$rflag$RPM_BUILD_ROOT"
grep -- $rpath install.log | sed "s@$rpath@$rflag@g" | sh -ex

# similarly fix esmf.mk
find $RPM_BUILD_ROOT/usr/lib -name esmf.mk | xargs perl -p -i -e "s,$RPM_BUILD_ROOT,,g"


# and the python
pushd src/addon/ESMPy/
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=../../../PYTHON_INSTALLED_FILES
popd

# and fix the relative path
mfpy=`find $RPM_BUILD_ROOT/usr/lib/python* -name esmfmkfile.py`
perl -p -i -e "s,\.\./\.\./\.\./lib/libO,/usr/lib/esmf/lib/libO,g" $mfpy

# and in the .pyc file
pushd `dirname $mfpy`
echo import esmfmkfile | python2.7
popd

# symlink the binaries into /usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
ln -s ../lib/esmf/bin/binO/*/* .
popd

# docs
mkdir -p $RPM_BUILD_ROOT/%{_docdir}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_docdir}/
tar xvfz %{SOURCE2} -C $RPM_BUILD_ROOT/%{_docdir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib/esmf
%{_bindir}/ESMF_*
%doc %{_docdir}/ESMF-license

%files doc
%doc %{_docdir}/ESMF_refdoc
%doc %{_docdir}/ESMF_usrdoc

%files python27 -f PYTHON_INSTALLED_FILES 


%changelog
* Fri Nov 20 2015  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.

