Name:		JAGS
Version:	4.2.0
Release:	1.ceda%{?dist}
Summary:	Just Another Gibbs Sampler

Group:		Scientific support
License:	GPLv2
URL:		http://mcmc-jags.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	blas-devel, lapack-devel
Requires:	blas, lapack

%description

JAGS is Just Another Gibbs Sampler.  It is a program for analysis of
Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC)
simulation not wholly unlike BUGS.  JAGS was written with three aims
in mind:

To have a cross-platform engine for the BUGS language

To be extensible, allowing users to write their own functions,
distributions and samplers.

To be a plaftorm for experimentation with ideas in Bayesian modelling

%prep
%setup -q 

%build
%configure --with-pic --with-blas --with-lapack
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/jags
%{_libdir}/JAGS/modules-4/*.so
%{_libdir}/JAGS/modules-4/*.la
%{_libdir}/libjags*
%{_libdir}/libjrmath*
%{_libdir}/pkgconfig/jags.pc
%{_includedir}/JAGS
/usr/libexec/jags-terminal
%doc
%{_mandir}/man1/jags.1.gz


%changelog

* Sun Oct 16 2016  <builderdev@builder.jc.rl.ac.uk> - 4.2.0-1.ceda
- initial version
