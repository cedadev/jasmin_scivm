Summary: IPython: Productive Interactive Computing
Name: python27-ipython
Version: 0.14_dev_ceda.1
Release: 3
Source0: ipython-0.14.dev-ceda.1.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: The IPython Development Team <ipython-dev@scipy.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://ipython.org
Requires: python27
BuildRequires: python27

%description

IPython provides a rich toolkit to help you make the most out of using Python
interactively.  Its main components are:

* Powerful interactive Python shells (terminal- and Qt-based).
* A web-based interactive notebook environment with all shell features plus
  support for embedded figures, animations and rich media.
* Support for interactive data visualization and use of GUI toolkits.
* Flexible, embeddable interpreters to load into your own projects.
* A high-performance library for high level and interactive parallel computing
  that works in multicore systems, clusters, supercomputing and cloud scenarios.

The enhanced interactive Python shells have the following main features:

* Comprehensive object introspection.

* Input history, persistent across sessions.

* Caching of output results during a session with automatically generated
  references.

* Extensible tab completion, with support by default for completion of python
  variables and keywords, filenames and function keywords.

* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.

* A rich configuration system with easy switching between different setups
  (simpler than changing $PYTHONSTARTUP environment variables every time).

* Session logging and reloading.

* Extensible syntax processing for special purpose situations.

* Access to the system shell with user-extensible alias system.

* Easily embeddable in other Python programs and GUIs.

* Integrated access to the pdb debugger and the Python profiler.

The parallel computing architecture has the following main features:

* Quickly parallelize Python code from an interactive Python/IPython session.

* A flexible and dynamic process model that be deployed on anything from
  multicore workstations to supercomputers.

* An architecture that supports many different styles of parallelism, from
  message passing to task farming.

* Both blocking and fully asynchronous interfaces.

* High level APIs that enable many things to be parallelized in a few lines
  of code.

* Share live parallel jobs with other users securely.

* Dynamically load balanced task farming system.

* Robust error handling in parallel code.

The latest development version is always available from IPython's `GitHub
site <http://github.com/ipython>`_.


%prep
%setup -n ipython-0.14.dev-ceda.1

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# replace any man pages with .gz version in file list (Alan)
perl -p -i -e 's/$/.gz/ if m{^/usr/share/man/man(.*?)/.*\.\1$}' INSTALLED_FILES

# put any filenames containing spaces in quotes (Alan)
perl -p -i -e 's/^(.*)$/"\1"/g if /\s/' INSTALLED_FILES

## renaming of executables - now deprecated
## for i in ipcluster ipcontroller ipengine iplogger iptest ipython irunner pycolor
## do
##   path=%{_bindir}/$i
##   tmppath=$RPM_BUILD_ROOT$path
##   mv $tmppath ${tmppath}_py27
##   perl -p -i -e "s,$path,${path}_py27," INSTALLED_FILES
## done
## 

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Fri Jun  7 2013  <builderdev@builder.jc.rl.ac.uk> - 0.14_dev_ceda.1-3
- don't rename executables as _py27

%files -f INSTALLED_FILES
%defattr(-,root,root)
