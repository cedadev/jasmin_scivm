%define pname wxPython
Summary: Cross platform GUI toolkit for Python
Name: python27-%{pname}
Version: 3.0.2.0
%define tarname %{pname}-src-%{version}
Release: 1.ceda%{?dist}
Source0: %{tarname}.tar.bz2
License: wxWidgets Library License (LGPL derivative)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Robin Dunn <robin@alldunn.com>
Url: http://wxPython.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

wxPython is a GUI toolkit for Python that is a wrapper around the
wxWidgets C++ GUI library.  wxPython provides a large variety of
window types and controls, all implemented with a native look and
feel (by using the native widgets) on the platforms upon which it is
supported.


%prep
%setup -n %{tarname}

%build
cd wxPython
python2.7 setup.py build

%install
cd wxPython
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Aug 24 2015  <builderdev@builder.jc.rl.ac.uk> - 3.0.2.0-1.ceda
- initial version

%files -f wxPython/INSTALLED_FILES
%defattr(-,root,root)
/usr/include/wx-3.0/wx/wxPython/i_files/*.pyc
/usr/include/wx-3.0/wx/wxPython/i_files/*.pyo
/usr/lib/python2.7/site-packages/wxversion.py
/usr/lib/python2.7/site-packages/wxversion.pyc
/usr/lib/python2.7/site-packages/wxversion.pyo
/usr/lib/python2.7/site-packages/*.egg-info
/usr/lib/python2.7/site-packages/wx.pth
