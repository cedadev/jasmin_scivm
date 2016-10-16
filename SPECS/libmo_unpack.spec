Summary: A library for handling the WGDOS and RLE compression schemes used in UM files.
Name: mo_unpack
Version: 3.1.2
Release: 1.ceda%{?dist}
Source0: libmo_unpack.%{version}.tar.gz
License: http://opensource.org/licenses/BSD-3-Clause
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Met Office
Url: https://github.com/SciTools/libmo_unpack
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
#Requires: 
BuildRequires: cmake

%description

A library for handling the WGDOS and RLE compression schemes used in UM files.

%prep
%setup -n libmo_unpack-%{version}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
rm -fr $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64

%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 3.1.2-1.ceda
- update with completely new build procedure, licence, URL, everything really

* Thu Oct 31 2013  <builderdev@builder.jc.rl.ac.uk> - 2.0.1-1.ceda%{dist}
- initial version

%files
%defattr(-,root,root)
%{_libdir}/libmo_unpack.so
%{_libdir}/libmo_unpack.so.3
%{_includedir}/logerrors.h  
%{_includedir}/rlencode.h
%{_includedir}/wgdosstuff.h

