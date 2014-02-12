%define tarname unpack-030712
Summary: Met Office PP unpacking library
Name: mo_unpack
Version: 2.0.1
Release: 1.ceda%{dist}
License: Copyright Met Office (see contained /usr/share/mo_unpack/licence)
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Group: Scientific support
URL: https://puma.nerc.ac.uk/trac/UM_TOOLS/wiki/unpack
Source0: %{tarname}.tgz
Source1: mo_unpack-licence
Patch1: mo_unpack-lib64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description

A library from the Met Office, callable from C programs, for reading 
packed PP files.

%prep
%setup -n %{tarname}
%patch1 -p1

%build
cd libmo_unpack
./make_library
ln -s lib lib64  # allows make_unpack build before libmo_unpack installation
cd ../unpack
./make_unpack ../libmo_unpack
cd ..

%install
%define docdir %{_datadir}/mo_unpack
%define tmp_docdir $RPM_BUILD_ROOT/%{docdir}

rm -rf $RPM_BUILD_ROOT
cd libmo_unpack
./distribute.sh $RPM_BUILD_ROOT/usr
mkdir -p %{tmp_docdir}
cp Document.txt %{tmp_docdir}
cp %{SOURCE1} %{tmp_docdir}/licence
cd ../unpack
./distribute.sh $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

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

%files
%defattr(-,root,root,-)
%{_libdir}/libmo_unpack.a
%{_libdir}/libmo_unpack.so
%{_libdir}/libmo_unpack.so.2
%{_libdir}/libmo_unpack.so.2.0
%{_libdir}/libmo_unpack.so.2.0.1
%{_includedir}/logerrors.h  
%{_includedir}/rlencode.h
%{_includedir}/wgdosstuff.h
%{_bindir}/unpack

%doc %{docdir}/licence
%doc %{docdir}/Document.txt


%changelog
* Thu Oct 31 2013  <builderdev@builder.jc.rl.ac.uk> - 2.0.1-1.ceda%{dist}
- initial version
