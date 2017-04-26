%define version_in_r 4-6
%define version_for_rpm 4.6

Summary: R interface to the JAGS library
Name: rjags
Version: %{version_for_rpm}
Release: 1.ceda%{dist}
License: GPLv2
Group: Applications/Engineering
URL: http://cran.r-project.org/web/packages/ncdf/index.html
Source0: https://cran.r-project.org/src/contrib/rjags_%{version_in_r}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
Requires: R, coda
BuildRequires: R, coda

%description

The rjags package provides an interface from R to the JAGS library for
Bayesian data analysis.  JAGS uses Markov Chain Monte Carlo (MCMC) to
generate a sequence of dependent samples from the posterior
distribution of the parameters.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

export R_LIBS=%{buildroot}/usr/lib64/R/library
mkdir -p $R_LIBS
echo "install.packages('%{SOURCE0}', repo=NULL)" | R --no-save

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rjags

%changelog

* Sun Oct 16 2016  <builderdev@builder.jc.rl.ac.uk> - 4-6-1.ceda%{dist}
- initial version


