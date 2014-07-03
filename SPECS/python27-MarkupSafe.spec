%define pname MarkupSafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
Name: python27-%{pname}
Version: 0.18
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Armin Ronacher <armin.ronacher@active-4.com>
Url: http://github.com/mitsuhiko/markupsafe
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27
BuildRequires: python27

%description
MarkupSafe
==========

Implements a unicode subclass that supports HTML strings:

>>> from markupsafe import Markup, escape
>>> escape("<script>alert(document.cookie);</script>")
Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
>>> tmpl = Markup("<em>%s</em>")
>>> tmpl % "Peter > Lustig"
Markup(u'<em>Peter &gt; Lustig</em>')

If you want to make an object unicode that is not yet unicode
but don't want to lose the taint information, you can use the
`soft_unicode` function.  (On Python 3 you can also use `soft_str` which
is a different name for the same function).

>>> from markupsafe import soft_unicode
>>> soft_unicode(42)
u'42'
>>> soft_unicode(Markup('foo'))
Markup(u'foo')

Objects can customize their HTML markup equivalent by overriding
the `__html__` function:

>>> class Foo(object):
...  def __html__(self):
...   return '<strong>Nice</strong>'
...
>>> escape(Foo())
Markup(u'<strong>Nice</strong>')
>>> Markup(Foo())
Markup(u'<strong>Nice</strong>')

Since MarkupSafe 0.10 there is now also a separate escape function
called `escape_silent` that returns an empty string for `None` for
consistency with other systems that return empty strings for `None`
when escaping (for instance Pylons' webhelpers).

If you also want to use this for the escape method of the Markup
object, you can create your own subclass that does that::

    from markupsafe import Markup, escape_silent as escape

    class SilentMarkup(Markup):
        __slots__ = ()

        @classmethod
        def escape(cls, s):
            return cls(escape(s))


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

* Thu Feb 13 2014  <builderdev@builder.jc.rl.ac.uk> - 0.18-1.ceda
- initial version

%files -f INSTALLED_FILES
%defattr(-,root,root)
