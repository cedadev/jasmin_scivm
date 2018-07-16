%define commit_id 5f35ec3e07f7
Summary: The International Land Model Benchmarking Package
Name: python27-ilamb
Version: 2.3
Release: 1.ceda%{?dist}
Source0: ilamb-v%{version}.tar.bz2
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Nathan Collier <nathaniel.collier@gmail.com>
Url: https://bitbucket.org/ncollier/ilamb
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-sympy python27-cf-units >= 2.0.2 
BuildRequires: python27
BuildArch: noarch

%description

The International Land Model Benchmarking (ILAMB) project is a
model-data intercomparison and integration project designed to improve
the performance of land models and, in parallel, improve the design of
new measurement campaigns to reduce uncertainties associated with key
land surface processes. Building upon past model evaluation studies,
the goals of ILAMB are to:

* develop internationally accepted benchmarks for land model
  performance, promote the use of these benchmarks by the
  international community for model intercomparison,
* strengthen linkages between experimental, remote sensing, and
  climate modeling communities in the design of new model tests and
  new measurement programs, and
* support the design and development of a new, open source,
  benchmarking software system for use by the international community.

It is the last of these goals to which this repository is
concerned. We have developed a python-based generic benchmarking
system, initially focused on assessing land model performance.
  

%prep
%setup -n ncollier-ilamb-%{commit_id}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Jul 16 2018  <builderdev@builder.jc.rl.ac.uk> - 2.3-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
