Name: emos
Version: 000382
Release: 2.ceda%{?dist}
License: LGPL 3.0
Group: Scientific support	
Source0: %{name}_%{version}.tar.gz
Source1: emos_000382_build_library_noninteractive_with_fpic
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root	
			#used with non-root builds of RPM files
BuildRequires: gcc, gcc-gfortran
Url: http://www.ecmwf.int/products/data/software/download/interpolation.html
Summary: EMOSLIB interpolation software from ECMWF

Prefix: /usr

%description					
The EMOS library from ECMWF (32 and 64 bit versions).

Includes the "gribex" GRIB encoding/decoding software rather than the
newer grib_api.

%prep

%setup0 -n %{name}_%{version}
pwd
cp %{SOURCE1} my_build

%build

%define installdir %{_datadir}/emos

export CNAME=_gfortran
export A64=
if [ `uname -m` = x86_64 ] ; then A64=A64; fi
echo $A64
export GRIB_API=
export JASPER_DIR=
export INSTALL_DIR=%{installdir}

R64= sh my_build  # build 32-bit lib
make clean LIBRARY=""  # clean *.o but avoid deleting libemos.a
R64=R64 sh my_build  # build 64-bit lib

%install			

rm -rf $RPM_BUILD_ROOT		

tmpinstalldir=$RPM_BUILD_ROOT/%{installdir}
mkdir -p $tmpinstalldir
echo $tmpinstalldir > .emos

# ./install will install both the lib from last build (64-bit) 
# and the data files into installdir, leaving lib from previous
# build (i.e. 32-bit) in current directory.  Run it and then 
# move both libs into libdir.
./install
tmplibdir=$RPM_BUILD_ROOT/%{_libdir}/
mkdir -p $tmplibdir
mv libemos.a $tmpinstalldir/libemosR64.a $tmplibdir/
chmod 644 $tmplibdir/*.a

%clean				
rm -rf $RPM_BUILD_ROOT

%files				
# TODO - sort this out
%defattr(-,root,root)			
%dir %{installdir}
%{_libdir}/*.a
%{installdir}/bufrtables
%{installdir}/crextables
%{installdir}/gribtables
%{installdir}/gribtemplates
%{installdir}/land_sea_mask

%changelog
* Thu Jan 17 2013  <builderdev@builder.jc.rl.ac.uk> - 000382-2.ceda
- -fPIC

* Thu Jan  3 2013 Alan Iwi
alan.iwi@stfc.ac.uk 20130102
- Created initial RPM
