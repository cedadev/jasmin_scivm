%define pname partd
Summary: Appendable key-value storage
Name: python27-%{pname}
Version: 0.3.8
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Matthew Rocklin <mrocklin@gmail.com>
Url: http://github.com/dask/partd/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-locket python27-toolz
BuildRequires: python27
BuildArch: noarch

%description

PartD
=====

|Build Status| |Version Status|

Key-value byte store with appendable values

    Partd stores key-value pairs.
    Values are raw bytes.
    We append on old values.

Partd excels at shuffling operations.

Operations
----------

PartD has two main operations, ``append`` and ``get``.


Example
-------

1.  Create a Partd backed by a directory::

        >>> import partd
        >>> p = partd.File('/path/to/new/dataset/')

2.  Append key-byte pairs to dataset::

        >>> p.append({'x': b'Hello ', 'y': b'123'})
        >>> p.append({'x': b'world!', 'y': b'456'})

3.  Get bytes associated to keys::

        >>> p.get('x')         # One key
        b'Hello world!'

        >>> p.get(['y', 'x'])  # List of keys
        [b'123456', b'Hello world!']

4.  Destroy partd dataset::

        >>> p.drop()

That's it.


Implementations
---------------

We can back a partd by an in-memory dictionary::

    >>> p = Dict()

For larger amounts of data or to share data between processes we back a partd
by a directory of files.  This uses file-based locks for consistency.::

    >>> p = File('/path/to/dataset/')

However this can fail for many small writes.  In these cases you may wish to buffer one partd with another, keeping a fixed maximum of data in the buffering partd.  This writes the larger elements of the first partd to the second partd when space runs low::

    >>> p = Buffer(Dict(), File(), available_memory=2e9)  # 2GB memory buffer

You might also want to have many distributed process write to a single partd
consistently.  This can be done with a server

*   Server Process::

        >>> p = Buffer(Dict(), File(), available_memory=2e9)  # 2GB memory buffer
        >>> s = Server(p, address='ipc://server')

*   Worker processes::

        >>> p = Client('ipc://server')  # Client machine talks to remote server


Encodings and Compression
-------------------------

Once we can robustly and efficiently append bytes to a partd we consider
compression and encodings.  This is generally available with the ``Encode``
partd, which accepts three functions, one to apply on bytes as they are
written, one to apply to bytes as they are read, and one to join bytestreams.
Common configurations already exist for common data and compression formats.

We may wish to compress and decompress data transparently as we interact with a
partd.  Objects like ``BZ2``, ``Blosc``, ``ZLib`` and ``Snappy`` exist and take
another partd as an argument.::

    >>> p = File(...)
    >>> p = ZLib(p)

These work exactly as before, the (de)compression happens automatically.

Common data formats like Python lists, numpy arrays, and pandas
dataframes are also supported out of the box.::

    >>> p = File(...)
    >>> p = NumPy(p)
    >>> p.append({'x': np.array([...])})

This lets us forget about bytes and think instead in our normal data types.

Composition
-----------

In principle we want to compose all of these choices together

1.  Write policy:  ``Dict``, ``File``, ``Buffer``, ``Client``
2.  Encoding:  ``Pickle``, ``Numpy``, ``Pandas``, ...
3.  Compression:  ``Blosc``, ``Snappy``, ...

Partd objects compose by nesting.  Here we make a partd that writes pickle
encoded BZ2 compressed bytes directly to disk::

    >>> p = Pickle(BZ2(File('foo')))

We could construct more complex systems that include compression,
serialization, buffering, and remote access.::

    >>> server = Server(Buffer(Dict(), File(), available_memory=2e0))

    >>> client = Pickle(Snappy(Client(server.address)))
    >>> client.append({'x': [1, 2, 3]})

.. |Build Status| image:: https://travis-ci.org/dask/partd.png
   :target: https://travis-ci.org/dask/partd
.. |Version Status| image:: https://img.shields.io/pypi/v/partd.svg
   :target: https://pypi.python.org/pypi/partd/




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
