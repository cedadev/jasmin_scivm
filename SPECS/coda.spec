%define version_in_r 0.18-1
%define version_for_rpm 0.18.1

Summary: Output Analysis and Diagnostics for MCMC
Name: coda
Version: %{version_for_rpm}
Release: 1.ceda%{dist}
License: GPLv2
Group: Applications/Engineering
URL: http://cran.r-project.org/web/packages/ncdf/index.html
Source0: https://cran.r-project.org/src/contrib/coda_%{version_in_r}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: alan.iwi@stfc.ac.uk
Requires: R
BuildRequires: R

%description

Provides functions for summarizing and plotting the output from Markov
Chain Monte Carlo (MCMC) simulations, as well as diagnostic tests of
convergence to the equilibrium distribution of the Markov chain

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
/usr/lib64/R/library/coda

%changelog

* Sun Oct 16 2016  <builderdev@builder.jc.rl.ac.uk> - 4-6-1.ceda%{dist}
- initial version


