%define pname Theano
Summary: Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Name: python27-%{pname}
Version: 1.0.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: LISA laboratory, University of Montreal <theano-dev@googlegroups.com>
Url: http://deeplearning.net/software/theano/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-numpy >= 1.9.1 python27-scipy >= 0.14 python27-six >= 1.9.0
BuildRequires: python27
BuildArch: noarch

%description

Theano is a Python library that allows you to define, optimize, and efficiently evaluate mathematical expressions involving multi-dimensional arrays. It is built on top of NumPy_. Theano features:

 * **tight integration with NumPy:** a similar interface to NumPy's. numpy.ndarrays are also used internally in Theano-compiled functions.
 * **transparent use of a GPU:** perform data-intensive computations up to 140x faster than on a CPU (support for float32 only).
 * **efficient symbolic differentiation:** Theano can compute derivatives for functions of one or many inputs.
 * **speed and stability optimizations:** avoid nasty bugs when computing expressions such as log(1 + exp(x)) for large values of x.
 * **dynamic C code generation:** evaluate expressions faster.
 * **extensive unit-testing and self-verification:** includes tools for detecting and diagnosing bugs and/or potential problems.

Theano has been powering large-scale computationally intensive scientific
research since 2007, but it is also approachable enough to be used in the
classroom (IFT6266 at the University of Montreal).

.. _NumPy: http://numpy.scipy.org/


=============
Release Notes
=============


Theano 1.0.1 (6th of December, 2017)
====================================

This is a maintenance release of Theano, version ``1.0.1``, with no new features, but some important bug fixes.

We recommend that everybody update to this version.

Highlights (since 1.0.0):

 - Fixed compilation and improved float16 support for topK on GPU

   - **NB**: topK support on GPU is experimental and may not work for large input sizes on certain GPUs

 - Fixed cuDNN reductions when axes to reduce have size ``1``
 - Attempted to prevent re-initialization of the GPU in a child process
 - Fixed support for temporary paths with spaces in Theano initialization
 - Spell check pass on the documentation

A total of 6 people contributed to this release since ``1.0.0``:

 - Frederic Bastien
 - Steven Bocco
 - Arnaud Bergeron
 - Sam Johnson
 - Edward Betts
 - Simon Lefrancois




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
