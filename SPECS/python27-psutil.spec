%define pname psutil
Summary: psutil is a cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python.
Name: python27-%{pname}
Version: 3.1.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Giampaolo Rodola <g.rodola <at> gmail <dot> com>
Url: https://github.com/giampaolo/psutil
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description

psutil (python system and process utilities) is a cross-platform
library for retrieving information on running processes and system
utilization (CPU, memory, disks, network) in Python. It is useful
mainly for system monitoring, profiling and limiting process resources
and management of running processes. It implements many
functionalities offered by command line tools such as: ps, top, lsof,
netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop,
uptime, pidof, tty, taskset, pmap.

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
