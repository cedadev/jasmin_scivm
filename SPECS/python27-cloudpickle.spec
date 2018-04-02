%define pname cloudpickle
Summary: Extended pickling support for Python objects
Name: python27-%{pname}
Version: 0.2.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Cloudpipe <cloudpipe@googlegroups.com>
Url: https://github.com/cloudpipe/cloudpickle
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

# cloudpickle

[![Build Status](https://travis-ci.org/cloudpipe/cloudpickle.svg?branch=master
    )](https://travis-ci.org/cloudpipe/cloudpickle)
[![codecov.io](https://codecov.io/github/cloudpipe/cloudpickle/coverage.svg?branch=master)](https://codecov.io/github/cloudpipe/cloudpickle?branch=master)

`cloudpickle` makes it possible to serialize Python constructs not supported
by the default `pickle` module from the Python standard library.

`cloudpickle` is especially useful for cluster computing where Python
expressions are shipped over the network to execute on remote hosts, possibly
close to the data.

Among other things, `cloudpickle` supports pickling for lambda expressions,
functions and classes defined interactively in the `__main__` module.


Installation
------------

The latest release of `cloudpickle` is available from
[pypi](https://pypi.python.org/pypi/cloudpickle):

    pip install cloudpickle


Examples
--------

Pickling a lambda expression:

```python
>>> import cloudpickle
>>> squared = lambda x: x ** 2
>>> pickled_lambda = cloudpickle.dumps(squared)

>>> import pickle
>>> new_squared = pickle.loads(pickled_lambda)
>>> new_squared(2)
4
```

Pickling a function interactively defined in a Python shell session
(in the `__main__` module):

```python
>>> CONSTANT = 42
>>> def my_function(data):
...    return data + CONSTANT
...
>>> pickled_function = cloudpickle.dumps(my_function)
>>> pickle.loads(pickled_function)(43)
85
```

Running the tests
-----------------

- With `tox`, to test run the tests for all the supported versions of
  Python and PyPy:

      pip install tox
      tox

  or alternatively for a specific environment:

      tox -e py27


- With `py.test` to only run the tests for your current version of
  Python:

      pip install -r dev-requirements.txt
      PYTHONPATH='.:tests' py.test


History
-------

`cloudpickle` was initially developed by picloud.com and shipped as part of
the client SDK.

A copy of `cloudpickle.py` was included as part of PySpark, the Python
interface to [Apache Spark](https://spark.apache.org/). Davies Liu, Josh
Rosen, Thom Neale and other Apache Spark developers improved it significantly,
most notably to add support for PyPy and Python 3.

The aim of the `cloudpickle` project is to make that work available to a wider
audience outside of the Spark ecosystem and to make it easier to improve it
further notably with the help of a dedicated non-regression test suite.




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
