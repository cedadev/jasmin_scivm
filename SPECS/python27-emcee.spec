%define pname emcee
Summary: Kick ass affine-invariant ensemble MCMC sampling
Name: python27-%{pname}
Version: 2.2.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Daniel Foreman-Mackey <danfm@nyu.edu>
Url: http://dan.iel.fm/emcee/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

emcee
=====

**The Python ensemble sampling toolkit for affine-invariant MCMC**

emcee is a stable, well tested Python implementation of the affine-invariant
ensemble sampler for Markov chain Monte Carlo (MCMC)
proposed by
`Goodman & Weare (2010) <http://cims.nyu.edu/~weare/papers/d13.pdf>`_.
The code is open source and has
already been used in several published projects in the Astrophysics
literature.

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
