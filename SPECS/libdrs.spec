Name: libdrs
Version: 20130102
Release: 2.ceda%{?dist}
License: check with PCMDI
Group: Scientific support	
Source: drs-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
			#used with non-root builds of RPM files
BuildRequires: gcc, gcc-gfortran
Summary: Data Retrieval and Storage System library
Prefix: /usr

%description					
The PCI Data Retrieval and Storage library developed at PCMDI.

This package is compiled from a snapshot of the source code taken from
Jeff Cole's directory (~jeff/software/drs) on the Reading Meteorology 
systems.

%prep

%setup -n new

%build				
#
# there is no makefile for GNU, so override some variables in the 
# Intel one
#
fc=gfortran
cc=gcc
# in fflags (below), -D__linux used in d_floor.F, -Df90func used in midate.F,
# to include replacement routines for d_floor() and itime() respectively,
# not provided in GNU Fortran rtl
fflags="-O -fPIC -fcray-pointer -D__linux -Df90func"
cflags="-O -fPIC"
fflagsr8="-fdefault-real-8 -Dalign8"
fflagsri8="$fflagsr8 -fdefault-integer-8"
defsr8="-Dreal8"
defsri8="$defsr8 -Dint8"

rm -f *.o
mf=Makefile.LINUX_64_intel
make -f $mf FC=$fc CC=$cc FFLAGS="$fflags" CFLAGS="$cflags"

rm -f *.o
mf=Makefile.LINUX_64_intel_R8
make -f $mf FC=$fc CC=$cc FFLAGS="$fflags $fflagsr8 $defsr8" CFLAGS="$cflags $defsr8"

rm -f *.o
mf=Makefile.LINUX_64_intel_RI8
make -f $mf FC=$fc CC=$cc FFLAGS="$fflags $fflagsri8 $defsri8" CFLAGS="$cflags $defsri8"

rm -f *.o


%install			

rm -rf $RPM_BUILD_ROOT		

dir=$RPM_BUILD_ROOT/%{_libdir}
mkdir -p $dir
install -m 644 *.a $dir

dir=$RPM_BUILD_ROOT/%{_includedir}
mkdir -p $dir
install -m 644 drsdef.h drscdf.h $dir


%clean				
rm -rf $RPM_BUILD_ROOT

%files				

%defattr(0644,root,root)			
%{_libdir}/libdrs.a
%{_libdir}/libdrsR8.a
%{_libdir}/libdrsRI8.a
%{_includedir}/drscdf.h
%{_includedir}/drsdef.h

%changelog
* Thu Jan  3 2013  <builderdev@builder.jc.rl.ac.uk> - 20130102-2.ceda
- add defines needed to avoid unresolved external symbols

* Wed Jan  2 2013 Alan Iwi
alan.iwi@stfc.ac.uk 20130102
- Created initial RPM
