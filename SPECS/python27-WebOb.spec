%define pname WebOb
Summary: WSGI request and response object
Name: python27-%{pname}
Version: 1.7.3
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Pylons Project <ianb@colorstudy.com>
Url: http://webob.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27
BuildArch: noarch

%description

WebOb
=====

.. image:: https://travis-ci.org/Pylons/webob.png?branch=master
        :target: https://travis-ci.org/Pylons/webob

.. image:: https://readthedocs.org/projects/webob/badge/?version=latest
        :target: http://docs.pylonsproject.org/projects/webob/en/latest/
        :alt: Documentation Status

WebOb provides objects for HTTP requests and responses.  Specifically
it does this by wrapping the `WSGI <http://wsgi.org>`_ request
environment and response status/headers/app_iter(body).

The request and response objects provide many conveniences for parsing
HTTP request and forming HTTP responses.  Both objects are read/write:
as a result, WebOb is also a nice way to create HTTP requests and
parse HTTP responses.

Support and Documentation
-------------------------

See the `WebOb Documentation website <https://webob.readthedocs.io/>`_ to view
documentation, report bugs, and obtain support.

License
-------

WebOb is offered under the `MIT-license
<https://webob.readthedocs.io/en/latest/license.html>`_.

Authors
-------

WebOb was authored by Ian Bicking and is currently maintained by the `Pylons
Project <http://pylonsproject.org/>`_ and a team of contributors.



1.7.3 (2017-06-30)
------------------

Bugfix
~~~~~~

- Request.host_url, Request.host_port and Request.domain now all understand and
  know how to parse IPv6 Host headers sent by browsers. See
  https://github.com/Pylons/webob/pull/332

1.7.2 (2017-03-15)
------------------

Bugfix
~~~~~~

- Allow unnamed fields in form data to be properly transcoded when calling
  request.decode with an alternate encoding. See
  https://github.com/Pylons/webob/pull/309

1.7.1 (2017-01-16)
------------------

Bugfix
~~~~~~

- ``Response.__init__`` would discard ``app_iter`` when a ``Response`` had no
  body, this would cause issues when ``app_iter`` was an object that was tied
  to the life-cycle of a web application and had to be properly closed.
  ``app_iter`` is more advanced API for ``Response`` and thus even if it
  contains a body and is thus against the HTTP RFC's, we should let the users
  shoot themselves by returning a body. See
  https://github.com/Pylons/webob/issues/305


1.7.0 (2016-12-22)
------------------

Compatibility
~~~~~~~~~~~~~

- WebOb is no longer supported on Python 2.6 and PyPy3 (due to pip no longer
  supporting Python 3.2 even on PyPy)

Backwards Incompatibility
~~~~~~~~~~~~~~~~~~~~~~~~~

- ``Response.content_type`` removes all existing Content-Type parameters, and
  if the new Content-Type is "texty" it adds a new charset (unless already
  provided) using the ``default_charset``. See
  https://github.com/Pylons/webob/pull/301

- ``Response.set_cookie`` no longer accepts a key argument. This was deprecated
  in WebOb 1.5 and as mentioned in the deprecation, is being removed in 1.7

- ``Response.__init__`` will no longer set the default Content-Type, nor
  Content-Length on Responses that don't have a body. This allows WebOb to
  return proper responses for things like `Response(status='204 No Content')`.

- ``Response.text`` will no longer raise if the Content-Type does not have a
  charset, it will fall back to using the new ``default_body_encoding`. To get
  the old behaviour back please sub-class ``Response`` and set
  ``default_body_encoding`` to ``None``. See
  https://github.com/Pylons/webob/pull/287

- WebOb no longer supports Chunked Encoding, this means that if you are using
  WebOb and need Chunked Encoding you will be required to have a proxy that
  unchunks the request for you. Please read
  https://github.com/Pylons/webob/issues/279 for more background.

Feature
~~~~~~~

- ``Response`` has a new ``default_body_encoding`` which may be used to allow
  getting/setting ``Response.text`` when a Content-Type has no charset. See
  https://github.com/Pylons/webob/pull/287

- ``webob.Request`` with any HTTP method is now allowed to have a body. This
  allows DELETE to have a request body for passing extra information. See
  https://github.com/Pylons/webob/pull/283 and
  https://github.com/Pylons/webob/pull/274

- Add ``tell()`` to ``ResponseBodyFile`` so that it may be used for example for
  zipfile support. See https://github.com/Pylons/webob/pull/117

- Allow the return from ``wsgify.middleware`` to be used as a decorator. See
  https://github.com/Pylons/webob/pull/228

Bugfix
~~~~~~

- Fixup ``cgi.FieldStorage`` on Python 3.x to work-around issue reported in
  Python bug report 27777 and 24764. This is currently applied for Python
  versions less than 3.7. See https://github.com/Pylons/webob/pull/294 and
  https://github.com/Pylons/webob/pull/300

- ``Response.set_cookie`` now accepts ``datetime`` objects for the ``expires``
  kwarg and will correctly convert them to UTC with no tzinfo for use in
  calculating the ``max_age``. See https://github.com/Pylons/webob/issues/254
  and https://github.com/Pylons/webob/pull/292

- Fixes ``request.PATH_SAFE`` to contain all of the path safe characters
  according to RFC3986. See https://github.com/Pylons/webob/pull/291

- WebOb's exceptions will lazily read underlying variables when inserted into
  templates to avoid expensive computations/crashes when inserting into the
  template. This had a bad performance regression on Py27 because of the way
  the lazified class was created and returned. See
  https://github.com/Pylons/webob/pull/284

- ``wsgify.__call__`` raised a ``TypeError`` with an unhelpful message, it will
  now return the ``repr`` for the wrapped function:
  https://github.com/Pylons/webob/issues/119

- ``Response.json``'s ``json.dumps``/``json.loads`` are now always UTF-8. It no
  longer tries to use the charset.

- The ``Response.__init__`` will by default no longer set the Content-Type to
  the default if a ``headerlist`` is provided. This fixes issues whereby
  ``Request.get_response()`` would return a Response that didn't match the
  actual response. See https://github.com/Pylons/webob/pull/261 and
  https://github.com/Pylons/webob/issues/205

- Cleans up the remainder of the issues with the updated WebOb exceptions that
  were taught to return JSON in version 1.6. See
  https://github.com/Pylons/webob/issues/237 and
  https://github.com/Pylons/webob/issues/236

- ``Response.from_file`` now parses the status line correctly when the status
  line contains an HTTP with version, as well as a status text that contains
  multiple white spaces (e.g HTTP/1.1 404 Not Found). See
  https://github.com/Pylons/webob/issues/250

- ``Response`` now has a new property named ``has_body`` that may be used to
  interrogate the ``Response`` to find out if ``Response.body`` is or isn't
  set.

  This is used in the exception handling code so that if you use a WebOb HTTP
  Exception and pass a generator to ``app_iter`` WebOb won't attempt to read
  the whole thing and instead allows it to be returned to the WSGI server. See
  https://github.com/Pylons/webob/pull/259




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
