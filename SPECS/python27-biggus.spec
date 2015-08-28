%define pname biggus
Summary: Virtual large arrays and lazy evaluation
Name: python27-%{pname}
Version: 0.11.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Richard Hattersley <rhattersley@gmail.com>
Url: https://github.com/SciTools/biggus
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Virtual large arrays and lazy evaluation.

For example, we can combine multiple array data sources into a single virtual array::

    >>> first_time_series = OrthoArrayAdapter(hdf_var_a)
    >>> second_time_series = OrthoArrayAdapater(hdf_var_b)
    >>> print first_time_series.shape, second_time_series.shape
    (52000, 800, 600) (56000, 800, 600)
    >>> time_series = biggus.LinearMosaic([first_time_series, second_time_series], axis=0)
    >>> time_series
    <LinearMosaic shape=(108000, 800, 600) dtype=dtype('float32')>

*Any* biggus Array can then be indexed, independent of underlying data sources::

    >>> time_series[51999:52001, 10, 12]
    <LinearMosaic shape=(2,) dtype=dtype('float32')>
    
And an Array can be converted to a numpy ndarray on demand::

    >>> time_series[51999:52001, 10, 12].ndarray()
    array([ 0.72151309,  0.54654914], dtype=float32)

%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Jul 13 2015  <builderdev@builder.jc.rl.ac.uk> - 0.11.0-1.ceda
- upgrade to 0.11.0

%files -f INSTALLED_FILES
%defattr(-,root,root)
