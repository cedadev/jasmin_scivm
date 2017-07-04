%define pname requests
Summary: Python HTTP for Humans.
Name: python27-%{pname}
Version: 2.18.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Kenneth Reitz <me@kennethreitz.org>
Url: http://python-requests.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 python27-urllib3 python27-certifi python27-chardet python27-idna
BuildRequires: python27
BuildArch: noarch

%description

Requests: HTTP for Humans
=========================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/l/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/pyversions/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://codecov.io/github/requests/requests/coverage.svg?branch=master
    :target: https://codecov.io/github/requests/requests
    :alt: codecov.io

.. image:: https://img.shields.io/github/contributors/requests/requests.svg
    :target: https://github.com/requests/requests/graphs/contributors

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/kennethreitz



Requests is the only *Non-GMO* HTTP library for Python, safe for human
consumption.

**Warning:** Recreational use of the Python standard library for HTTP may result in dangerous side-effects,
including: security vulnerabilities, verbose code, reinventing the wheel,
constantly reading documentation, depression, headaches, or even death.

Behold, the power of Requests:

.. code-block:: python

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'disk_usage': 368627, u'private_gists': 484, ...}

See `the similar code, sans Requests <https://gist.github.com/973705>`_.

.. image:: https://raw.githubusercontent.com/requests/requests/master/docs/_static/requests-logo-small.png
    :target: http://docs.python-requests.org/


Requests allows you to send *organic, grass-fed* HTTP/1.1 requests, without the
need for manual labor. There's no need to manually add query strings to your
URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling
are 100% automatic, thanks to `urllib3 <https://github.com/shazow/urllib3>`_.

Besides, all the cool kids are doing it. Requests is one of the most
downloaded Python packages of all time, pulling in over 11,000,000 downloads
every month. You don't want to be left out!

Feature Support
---------------

Requests is ready for today's web.

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Automatic Content Decoding
- Unicode Response Bodies
- Multipart File Uploads
- HTTP(S) Proxy Support
- Connection Timeouts
- Streaming Downloads
- ``.netrc`` Support
- Chunked Requests

Requests officially supports Python 2.6–2.7 & 3.3–3.7, and runs great on PyPy.

Documentation
-------------

Fantastic documentation is available at http://docs.python-requests.org/, for a limited time only.

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
