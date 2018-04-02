%define pname pymc3
Summary: PyMC3
Name: python27-%{pname}
Version: 3.3
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
Patch0: pymc3-req.diff
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: PyMC Developers <pymc.devs@gmail.com>
Url: http://github.com/pymc-devs/pymc3
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-theano>=1.0.0 python27-pandas>=0.18.0 python27-patsy>=0.4.0 python27-joblib>=0.9 python27-tqdm>=4.8.4 python27-six>=1.10.0 python27-h5py>=2.7.0 python27-enum34>=1.1.6
BuildRequires: python27
BuildArch: noarch

%description

Bayesian estimation, particularly using Markov chain Monte Carlo
(MCMC), is an increasingly relevant approach to statistical
estimation. However, few statistical software packages implement MCMC
samplers, and they are non-trivial to code by hand. ``pymc3`` is a
python package that implements the Metropolis-Hastings algorithm as a
python class, and is extremely flexible and applicable to a large
suite of problems. ``pymc3`` includes methods for summarizing output,
plotting, goodness-of-fit and convergence diagnostics.

%prep
%setup -n %{pname}-%{version}
%patch0 -p1

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
