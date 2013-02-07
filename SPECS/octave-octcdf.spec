%global octpkg octcdf

Name:           octave-%{octpkg}
Version:        1.1.5
Release:        1.ceda%{?dist}
Summary:        A NetCDF interface for octave
Group:          Applications/Engineering
License:        GPLv2+
URL:            http://octave.sourceforge.net/octcdf/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  octave-devel >= 3.6.1
BuildRequires:  netcdf-devel >= 4.2.1

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Obsoletes:      octave-forge <= 20090607


%description
A NetCDF interface for octave.

%prep
%setup -q -n %{octpkg}

%build
%octave_pkg_build

%install
rm -fr %{buildroot}
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%defattr(-,root,root,-)
%{octpkglibdir}
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/@ncatt/
%{octpkgdir}/@ncdim/
%{octpkgdir}/@ncfile/
%{octpkgdir}/@ncvar/


%changelog
* Thu Dec 20 2012  <builderdev@builder.jc.rl.ac.uk> - 1.1.2-1.ceda
- graft in changes based on 1.1.5 spec file for fedora
- specify octave, netcdf versions from ceda build

* Mon Aug 8 2011 Orion Poplawski <orion@cora.nwra.com> 1.1.2-2
- Rebuild for octave 3.4.2

* Tue Apr 05 2011 Orion Poplawski <orion@cora.nwra.com> 1.1.2-1
- initial package for Fedora
