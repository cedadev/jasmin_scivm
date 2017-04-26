%global octpkg netcdf

Name:           octave-%{octpkg}
Version:        1.0.7
Release:        2.ceda%{?dist}
Summary:        A MATLAB compatible NetCDF interface for Octave
Group:          Applications/Engineering
License:        GPLv2+
URL:            http://octave.sourceforge.net/%{octpkg}/
Source0:        octave-%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  netcdf-devel >= 4.4.0

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
A MATLAB compatible NetCDF interface for Octave.


%prep
%setup -q -n %{octpkg}


%build
# Need to rebuild netcdf_constants.h first
make -C src constants
%octave_pkg_build


%install
%octave_pkg_install
touch $RPM_BUILD_ROOT/%{octpkgdir}/packinfo/.autoload

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{octpkgdir}/private/


%changelog
* Thu Apr  7 2016  <builderdev@builder.jc.rl.ac.uk> - 1.0.7-1.ceda
- compile against netcdf 4.4.0

* Mon Dec  7 2015  <builderdev@builder.jc.rl.ac.uk> - 1.0.7-1.ceda
- rebuild against octave 4.0.0 and netcdf 4.3.3.1

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-1
- Update to 1.0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> 1.0.6-1
- Update to 1.0.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 8 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.5-1
- Update to 1.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.4-1
- Update to 1.0.4

* Thu May 8 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.3-1
- Update to 1.0.3

* Tue Feb 18 2014 Orion Poplawski <orion@cora.nwra.com> 1.0.2-1
- Initial Fedora package
