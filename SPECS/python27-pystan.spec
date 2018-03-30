%define pname pystan
Summary: Python interface to Stan, a package for Bayesian inference
Name: python27-%{pname}
Version: 2.17.1.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: PyStan Developers <stan-users@googlegroups.com>
Url: https://github.com/stan-dev/pystan
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

PyStan: The Python Interface to Stan
====================================


**PyStan** provides a Python interface to Stan, a package for Bayesian inference
using the No-U-Turn sampler, a variant of Hamiltonian Monte Carlo.

For more information on `Stan <http://mc-stan.org>`_ and its modeling language,
see the Stan User's Guide and Reference Manual at `http://mc-stan.org/
<http://mc-stan.org/>`_.

Important links
---------------

- HTML documentation: https://pystan.readthedocs.org
- Issue tracker: https://github.com/stan-dev/pystan/issues
- Source code repository: https://github.com/stan-dev/pystan
- Stan: http://mc-stan.org/
- Stan User's Guide and Reference Manual (pdf) available at http://mc-stan.org

Related projects
----------------

- Scikit-learn integration: `pystan-sklearn <https://github.com/rgerkin/pystan-sklearn>`_ by @rgerkin.

Similar projects
----------------

- PyMC: http://pymc-devs.github.io/pymc/

Example
-------

::

    import pystan
    import numpy as np
    import matplotlib.pyplot as plt

    schools_code = """
    data {
        int<lower=0> J; // number of schools
        real y[J]; // estimated treatment effects
        real<lower=0> sigma[J]; // s.e. of effect estimates
    }
    parameters {
        real mu;
        real<lower=0> tau;
        real eta[J];
    }
    transformed parameters {
        real theta[J];
        for (j in 1:J)
            theta[j] = mu + tau * eta[j];
    }
    model {
        eta ~ normal(0, 1);
        y ~ normal(theta, sigma);
    }
    """

    schools_dat = {'J': 8,
                   'y': [28,  8, -3,  7, -1,  1, 18, 12],
                   'sigma': [15, 10, 16, 11,  9, 11, 10, 18]}

    sm = pystan.StanModel(model_code=schools_code)
    fit = sm.sampling(data=schools_dat, iter=1000, chains=4)

    print(fit)

    eta = fit.extract(permuted=True)['eta']
    np.mean(eta, axis=0)

    # if matplotlib is installed (optional, not required), a visual summary and
    # traceplot are available
    fit.plot()
    plt.show()

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
