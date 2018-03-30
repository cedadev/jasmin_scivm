%define pname statsmodels
Summary: Statistical computations and models for Python
Name: python27-%{pname}
Version: 0.8.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Skipper Seabold, Josef Perktold <pystatsmodels@googlegroups.com>
Url: http://www.statsmodels.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

About Statsmodels
=================

Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.


Documentation
=============

The documentation for the latest release is at

   http://www.statsmodels.org/stable/

The documentation for the development version is at

   http://www.statsmodels.org/dev/

Recent improvements are highlighted in the release notes

   http://www.statsmodels.org/stable/release/version0.8.html

Backups of documentation are available at http://statsmodels.github.io/stable/
and http://statsmodels.github.io/dev/.



Main Features
=============

* Linear regression models:

  - Ordinary least squares
  - Generalized least squares
  - Weighted least squares
  - Least squares with autoregressive errors
  - Quantile regression

* Mixed Linear Model with mixed effects and variance components
* GLM: Generalized linear models with support for all of the one-parameter
  exponential family distributions
* GEE: Generalized Estimating Equations for one-way clustered or longitudinal data
* Discrete models:

  - Logit and Probit
  - Multinomial logit (MNLogit)
  - Poisson regression
  - Negative Binomial regression

* RLM: Robust linear models with support for several M-estimators.
* Time Series Analysis: models for time series analysis

  - Complete StateSpace modeling framework

    - Seasonal ARIMA and ARIMAX models
    - VARMA and VARMAX models
    - Dynamic Factor models

  - Markov switching models (MSAR), also known as Hidden Markov Models (HMM)
  - Univariate time series analysis: AR, ARIMA
  - Vector autoregressive models, VAR and structural VAR
  - Hypothesis tests for time series: unit root, cointegration and others
  - Descriptive statistics and process models for time series analysis

* Survival analysis:

  - Proportional hazards regression (Cox models)
  - Survivor function estimation (Kaplan-Meier)
  - Cumulative incidence function estimation

* Nonparametric statistics: (Univariate) kernel density estimators
* Datasets: Datasets used for examples and in testing
* Statistics: a wide range of statistical tests

  - diagnostics and specification tests
  - goodness-of-fit and normality tests
  - functions for multiple testing
  - various additional statistical tests

* Imputation with MICE and regression on order statistic
* Mediation analysis
* Principal Component Analysis with missing data
* I/O

  - Tools for reading Stata .dta files into numpy arrays.
  - Table output to ASCII, LaTeX, and HTML

* Miscellaneous models
* Sandbox: statsmodels contains a sandbox folder with code in various stages of
  development and testing which is not considered "production ready".   This covers
  among others

  - Generalized method of moments (GMM) estimators
  - Kernel regression
  - Various extensions to scipy.stats.distributions
  - Panel data models
  - Information theoretic measures


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
