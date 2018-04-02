%define pname locket
Summary: File-based locks for Python for Linux and Windows
Name: python27-%{pname}
Version: 0.2.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Michael Williamson <mike@zwobble.org>
Url: http://github.com/mwilliamson/locket.py
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

locket.py
=========

Locket implements a lock that can be used by multiple processes provided they use the same path.

.. code-block:: python

    import locket

    # Wait for lock
    with locket.lock_file("path/to/lock/file"):
        perform_action()

    # Raise error if lock cannot be acquired immediately
    with locket.lock_file("path/to/lock/file", timeout=0):
        perform_action()
        
    # Raise error if lock cannot be acquired after thirty seconds
    with locket.lock_file("path/to/lock/file", timeout=30):
        perform_action()
        
    # Without context managers:
    lock = locket.lock_file("path/to/lock/file")
    try:
        lock.acquire()
        perform_action()
    finally:
        lock.release()

Locks largely behave as (non-reentrant) `Lock` instances from the `threading`
module in the standard library. Specifically, their behaviour is:

* Locks are uniquely identified by the file being locked,
  both in the same process and across different processes.

* Locks are either in a locked or unlocked state.

* When the lock is unlocked, calling `acquire()` returns immediately and changes
  the lock state to locked.

* When the lock is locked, calling `acquire()` will block until the lock state
  changes to unlocked, or until the timeout expires.

* If a process holds a lock, any thread in that process can call `release()` to
  change the state to unlocked.

* Behaviour of locks after `fork` is undefined.




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
