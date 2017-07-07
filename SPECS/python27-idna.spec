%define pname idna
Summary: Internationalized Domain Names in Applications (IDNA)
Name: python27-%{pname}
Version: 2.5
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD-like
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Kim Davies <kim@cynosure.com.au>
Url: https://github.com/kjd/idna
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalised Domain Names in Applications
(IDNA) protocol as specified in `RFC 5891 <http://tools.ietf.org/html/rfc5891>`_.
This is the latest version of the protocol and is sometimes referred to as
“IDNA 2008”.

This library also provides support for Unicode Technical Standard 46,
`Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_.

This acts as a suitable replacement for the “encodings.idna” module that
comes with the Python standard library, but only supports the
old, deprecated IDNA specification (`RFC 3490 <http://tools.ietf.org/html/rfc3490>`_).

Basic functions are simply executed:

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode('ドメイン.テスト')
    b'xn--eckwd4c7c.xn--zckzah'
    >>> print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
    ドメイン.テスト

    # Python 2
    >>> import idna
    >>> idna.encode(u'ドメイン.テスト')
    'xn--eckwd4c7c.xn--zckzah'
    >>> print idna.decode('xn--eckwd4c7c.xn--zckzah')
    ドメイン.テスト

Packages
--------

The latest tagged release version is published in the PyPI repository:

.. image:: https://badge.fury.io/py/idna.svg
   :target: http://badge.fury.io/py/idna


Installation
------------

To install this library, you can use pip:

.. code-block:: bash

    $ pip install idna

Alternatively, you can install the package using the bundled setup script:

.. code-block:: bash

    $ python setup.py install

This library works with Python 2.6 or later, and Python 3.3 or later.


Usage
-----

For typical usage, the ``encode`` and ``decode`` functions will take a domain
name argument and perform a conversion to A-labels or U-labels respectively.

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode('ドメイン.テスト')
    b'xn--eckwd4c7c.xn--zckzah'
    >>> print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
    ドメイン.テスト

You may use the codec encoding and decoding methods using the
``idna.codec`` module:

.. code-block:: pycon

    # Python 2
    >>> import idna.codec
    >>> print u'домена.испытание'.encode('idna')
    xn--80ahd1agd.xn--80akhbyknj4f
    >>> print 'xn--80ahd1agd.xn--80akhbyknj4f'.decode('idna')
    домена.испытание

Conversions can be applied at a per-label basis using the ``ulabel`` or ``alabel``
functions if necessary:

.. code-block:: pycon

    # Python 2
    >>> idna.alabel(u'测试')
    'xn--0zwm56d'

Compatibility Mapping (UTS #46)
+++++++++++++++++++++++++++++++

As described in `RFC 5895 <http://tools.ietf.org/html/rfc5895>`_, the IDNA
specification no longer normalizes input from different potential ways a user
may input a domain name. This functionality, known as a “mapping”, is now
considered by the specification to be a local user-interface issue distinct
from IDNA conversion functionality.

This library provides one such mapping, that was developed by the Unicode
Consortium. Known as `Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_,
it provides for both a regular mapping for typical applications, as well as
a transitional mapping to help migrate from older IDNA 2003 applications.

For example, “Königsgäßchen” is not a permissible label as *LATIN CAPITAL
LETTER K* is not allowed (nor are capital letters in general). UTS 46 will
convert this into lower case prior to applying the IDNA conversion.

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode(u'Königsgäßchen')
    ...
    idna.core.InvalidCodepoint: Codepoint U+004B at position 1 of 'Königsgäßchen' not allowed
    >>> idna.encode('Königsgäßchen', uts46=True)
    b'xn--knigsgchen-b4a3dun'
    >>> print(idna.decode('xn--knigsgchen-b4a3dun'))
    königsgäßchen

Transitional processing provides conversions to help transition from the older
2003 standard to the current standard. For example, in the original IDNA
specification, the *LATIN SMALL LETTER SHARP S* (ß) was converted into two
*LATIN SMALL LETTER S* (ss), whereas in the current IDNA specification this
conversion is not performed.

.. code-block:: pycon

    # Python 2
    >>> idna.encode(u'Königsgäßchen', uts46=True, transitional=True)
    'xn--knigsgsschen-lcb0w'

Implementors should use transitional processing with caution, only in rare
cases where conversion from legacy labels to current labels must be performed
(i.e. IDNA implementations that pre-date 2008). For typical applications
that just need to convert labels, transitional processing is unlikely to be
beneficial and could produce unexpected incompatible results.

``encodings.idna`` Compatibility
++++++++++++++++++++++++++++++++

Function calls from the Python built-in ``encodings.idna`` module are
mapped to their IDNA 2008 equivalents using the ``idna.compat`` module.
Simply substitute the ``import`` clause in your code to refer to the
new module name.

Exceptions
----------

All errors raised during the conversion following the specification should
raise an exception derived from the ``idna.IDNAError`` base class.

More specific exceptions that may be generated as ``idna.IDNABidiError``
when the error reflects an illegal combination of left-to-right and right-to-left
characters in a label; ``idna.InvalidCodepoint`` when a specific codepoint is
an illegal character in an IDN label (i.e. INVALID); and ``idna.InvalidCodepointContext``
when the codepoint is illegal based on its positional context (i.e. it is CONTEXTO
or CONTEXTJ but the contextual requirements are not satisfied.)

Testing
-------

The library has a test suite based on each rule of the IDNA specification, as
well as tests that are provided as part of the Unicode Technical Standard 46,
`Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_.

The tests are run automatically on each commit at Travis CI:

.. image:: https://travis-ci.org/kjd/idna.svg?branch=master
   :target: https://travis-ci.org/kjd/idna



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
