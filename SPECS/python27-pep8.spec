%define pname pep8
Summary: Python style guide checker
Name: python27-%{pname}
Version: 1.7.1
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: Expat license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Ian Lee <IanLee1521@gmail.com>
Url: http://pep8.readthedocs.org/
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

pep8 - Python style guide checker
=================================

pep8 is a tool to check your Python code against some of the style
conventions in `PEP 8`_.

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


Features
--------

* Plugin architecture: Adding new checks is easy.

* Parseable output: Jump to error location in your editor.

* Small: Just one Python file, requires only stdlib. You can use just
  the pep8.py file for this purpose.

* Comes with a comprehensive test suite.

Installation
------------

You can install, upgrade, uninstall pep8.py with these commands::

  $ pip install pep8
  $ pip install --upgrade pep8
  $ pip uninstall pep8

There's also a package for Debian/Ubuntu, but it's not always the
latest version.

Example usage and output
------------------------

::

  $ pep8 --first optparse.py
  optparse.py:69:11: E401 multiple imports on one line
  optparse.py:77:1: E302 expected 2 blank lines, found 1
  optparse.py:88:5: E301 expected 1 blank line, found 0
  optparse.py:222:34: W602 deprecated form of raising exception
  optparse.py:347:31: E211 whitespace before '('
  optparse.py:357:17: E201 whitespace after '{'
  optparse.py:472:29: E221 multiple spaces before operator
  optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

You can also make pep8.py show the source code for each error, and
even the relevant text from PEP 8::

  $ pep8 --show-source --show-pep8 testsuite/E40.py
  testsuite/E40.py:2:10: E401 multiple imports on one line
  import os, sys
           ^
      Imports should usually be on separate lines.

      Okay: import os\nimport sys
      E401: import sys, os


Or you can display how often each error was found::

  $ pep8 --statistics -qq Python-2.5/Lib
  232     E201 whitespace after '['
  599     E202 whitespace before ')'
  631     E203 whitespace before ','
  842     E211 whitespace before '('
  2531    E221 multiple spaces before operator
  4473    E301 expected 1 blank line, found 0
  4006    E302 expected 2 blank lines, found 1
  165     E303 too many blank lines (4)
  325     E401 multiple imports on one line
  3615    E501 line too long (82 characters)
  612     W601 .has_key() is deprecated, use 'in'
  1188    W602 deprecated form of raising exception

Links
-----

.. image:: https://api.travis-ci.org/PyCQA/pep8.png?branch=master
   :target: https://travis-ci.org/PyCQA/pep8
   :alt: Build status

.. image:: https://pypip.in/wheel/pep8/badge.png?branch=master
   :target: https://pypi.python.org/pypi/pep8
   :alt: Wheel Status

* `Read the documentation <http://pep8.readthedocs.org/>`_

* `Fork me on GitHub <http://github.com/PyCQA/pep8>`_


Changelog
=========

1.7.1 (2017-10-22)
------------------

Changes:

* Prominently note via warning message that the tool is no longer released as
  ``pep8`` and will only be fixed in the ``pycodestyle`` package

1.7.0 (2016-01-12)
------------------

Announcements:

* Repository moved to PyCQA Organization on GitHub:
  https://github.com/pycqa/pep8

Changes:

* Reverted the fix in #368, "options passed on command line are only ones
  accepted" feature. This has many unintended consequences in pep8 and flake8
  and needs to be reworked when I have more time.
* Added support for Python 3.5. (Issue #420 & #459)
* Added support for multi-line config_file option parsing. (Issue #429)
* Improved parameter parsing. (Issues #420 & #456)

Bugs:

* Fixed BytesWarning on Python 3. (Issue #459)

1.6.2 (2015-02-15)
------------------

Changes:

* Added check for breaking around a binary operator. (Issue #197, Pull #305)

Bugs:

* Restored config_file parameter in process_options(). (Issue #380)


1.6.1 (2015-02-08)
------------------

Changes:

* Assign variables before referenced. (Issue #287)

Bugs:

* Exception thrown due to unassigned ``local_dir`` variable. (Issue #377)


1.6.0 (2015-02-06)
------------------

News:

* Ian Lee <ianlee1521@gmail.com> joined the project as a maintainer.

Changes:

* Report E731 for lambda assignment. (Issue #277)

* Report E704 for one-liner def instead of E701.
  Do not report this error in the default configuration. (Issue #277)

* Replace codes E111, E112 and E113 with codes E114, E115 and E116
  for bad indentation of comments. (Issue #274)

* Report E266 instead of E265 when the block comment starts with
  multiple ``#``. (Issue #270)

* Report E402 for import statements not at the top of the file. (Issue #264)

* Do not enforce whitespaces around ``**`` operator. (Issue #292)

* Strip whitespace from around paths during normalization. (Issue #339 / #343)

* Update ``--format`` documentation. (Issue #198 / Pull Request #310)

* Add ``.tox/`` to default excludes. (Issue #335)

* Do not report E121 or E126 in the default configuration. (Issues #256 / #316)

* Allow spaces around the equals sign in an annotated function. (Issue #357)

* Allow trailing backslash if in an inline comment. (Issue #374)

* If ``--config`` is used, only that configuration is processed. Otherwise,
  merge the user and local configurations are merged. (Issue #368 / #369)

Bug fixes:

* Don't crash if Checker.build_tokens_line() returns None. (Issue #306)

* Don't crash if os.path.expanduser() throws an ImportError. (Issue #297)

* Missing space around keyword parameter equal not always reported, E251.
  (Issue #323)

* Fix false positive E711/E712/E713. (Issues #330 and #336)

* Do not skip physical checks if the newline is escaped. (Issue #319)

* Flush sys.stdout to avoid race conditions with printing. See flake8 bug:
  https://gitlab.com/pycqa/flake8/issues/17 for more details. (Issue #363)


1.5.7 (2014-05-29)
------------------

Bug fixes:

* Skip the traceback on "Broken pipe" signal. (Issue #275)

* Do not exit when an option in ``setup.cfg`` or ``tox.ini``
  is not recognized.

* Check the last line even if it does not end with a newline. (Issue #286)

* Always open files in universal newlines mode in Python 2. (Issue #288)


1.5.6 (2014-04-14)
------------------

Bug fixes:

* Check the last line even if it has no end-of-line. (Issue #273)


1.5.5 (2014-04-10)
------------------

Bug fixes:

* Fix regression with E22 checks and inline comments. (Issue #271)


1.5.4 (2014-04-07)
------------------

Bug fixes:

* Fix negative offset with E303 before a multi-line docstring.
  (Issue #269)


1.5.3 (2014-04-04)
------------------

Bug fixes:

* Fix wrong offset computation when error is on the last char
  of a physical line. (Issue #268)


1.5.2 (2014-04-04)
------------------

Changes:

* Distribute a universal wheel file.

Bug fixes:

* Report correct line number for E303 with comments. (Issue #60)

* Do not allow newline after parameter equal. (Issue #252)

* Fix line number reported for multi-line strings. (Issue #220)

* Fix false positive E121/E126 with multi-line strings. (Issue #265)

* Fix E501 not detected in comments with Python 2.5.

* Fix caret position with ``--show-source`` when line contains tabs.


1.5.1 (2014-03-27)
------------------

Bug fixes:

* Fix a crash with E125 on multi-line strings. (Issue #263)


1.5 (2014-03-26)
----------------

Changes:

* Report E129 instead of E125 for visually indented line with same
  indent as next logical line.  (Issue #126)

* Report E265 for space before block comment. (Issue #190)

* Report E713 and E714 when operators ``not in`` and ``is not`` are
  recommended. (Issue #236)

* Allow long lines in multiline strings and comments if they cannot
  be wrapped. (Issue #224).

* Optionally disable physical line checks inside multiline strings,
  using ``# noqa``. (Issue #242)

* Change text for E121 to report "continuation line under-indented
  for hanging indent" instead of indentation not being a
  multiple of 4.

* Report E131 instead of E121 / E126 if the hanging indent is not
  consistent within the same continuation block.  It helps when
  error E121 or E126 is in the ``ignore`` list.

* Report E126 instead of E121 when the continuation line is hanging
  with extra indentation, even if indentation is not a multiple of 4.

Bug fixes:

* Allow the checkers to report errors on empty files. (Issue #240)

* Fix ignoring too many checks when ``--select`` is used with codes
  declared in a flake8 extension. (Issue #216)

* Fix regression with multiple brackets. (Issue #214)

* Fix ``StyleGuide`` to parse the local configuration if the
  keyword argument ``paths`` is specified. (Issue #246)

* Fix a false positive E124 for hanging indent. (Issue #254)

* Fix a false positive E126 with embedded colon. (Issue #144)

* Fix a false positive E126 when indenting with tabs. (Issue #204)

* Fix behaviour when ``exclude`` is in the configuration file and
  the current directory is not the project directory. (Issue #247)

* The logical checks can return ``None`` instead of an empty iterator.
  (Issue #250)

* Do not report multiple E101 if only the first indentation starts
  with a tab. (Issue #237)

* Fix a rare false positive W602. (Issue #34)


1.4.6 (2013-07-02)
------------------

Changes:

* Honor ``# noqa`` for errors E711 and E712. (Issue #180)

* When both a ``tox.ini`` and a ``setup.cfg`` are present in the project
  directory, merge their contents.  The ``tox.ini`` file takes
  precedence (same as before). (Issue #182)

* Give priority to ``--select`` over ``--ignore``. (Issue #188)

* Compare full path when excluding a file. (Issue #186)

* New option ``--hang-closing`` to switch to the alternative style of
  closing bracket indentation for hanging indent.  Add error E133 for
  closing bracket which is missing indentation. (Issue #103)

* Accept both styles of closing bracket indentation for hanging indent.
  Do not report error E123 in the default configuration. (Issue #103)

Bug fixes:

* Do not crash when running AST checks and the document contains null bytes.
  (Issue #184)

* Correctly report other E12 errors when E123 is ignored. (Issue #103)

* Fix false positive E261/E262 when the file contains a BOM. (Issue #193)

* Fix E701, E702 and E703 not detected sometimes. (Issue #196)

* Fix E122 not detected in some cases. (Issue #201 and #208)

* Fix false positive E121 with multiple brackets. (Issue #203)


1.4.5 (2013-03-06)
------------------

* When no path is specified, do not try to read from stdin.  The feature
  was added in 1.4.3, but it is not supported on Windows.  Use ``-``
  filename argument to read from stdin.  This usage is supported
  since 1.3.4. (Issue #170)

* Do not require ``setuptools`` in setup.py.  It works around an issue
  with ``pip`` and Python 3. (Issue #172)

* Add ``__pycache__`` to the ignore list.

* Change misleading message for E251. (Issue #171)

* Do not report false E302 when the source file has a coding cookie or a
  comment on the first line. (Issue #174)

* Reorganize the tests and add tests for the API and for the command line
  usage and options. (Issues #161 and #162)

* Ignore all checks which are not explicitly selected when ``select`` is
  passed to the ``StyleGuide`` constructor.


1.4.4 (2013-02-24)
------------------

* Report E227 or E228 instead of E225 for whitespace around bitwise, shift
  or modulo operators. (Issue #166)

* Change the message for E226 to make clear that it is about arithmetic
  operators.

* Fix a false positive E128 for continuation line indentation with tabs.

* Fix regression with the ``--diff`` option. (Issue #169)

* Fix the ``TestReport`` class to print the unexpected warnings and
  errors.


1.4.3 (2013-02-22)
------------------

* Hide the ``--doctest`` and ``--testsuite`` options when installed.

* Fix crash with AST checkers when the syntax is invalid. (Issue #160)

* Read from standard input if no path is specified.

* Initiate a graceful shutdown on ``Control+C``.

* Allow to change the ``checker_class`` for the ``StyleGuide``.


1.4.2 (2013-02-10)
------------------

* Support AST checkers provided by third-party applications.

* Register new checkers with ``register_check(func_or_cls, codes)``.

* Allow to construct a ``StyleGuide`` with a custom parser.

* Accept visual indentation without parenthesis after the ``if``
  statement. (Issue #151)

* Fix UnboundLocalError when using ``# noqa`` with continued lines.
  (Issue #158)

* Re-order the lines for the ``StandardReport``.

* Expand tabs when checking E12 continuation lines. (Issue #155)

* Refactor the testing class ``TestReport`` and the specific test
  functions into a separate test module.


1.4.1 (2013-01-18)
------------------

* Allow sphinx.ext.autodoc syntax for comments. (Issue #110)

* Report E703 instead of E702 for the trailing semicolon. (Issue #117)

* Honor ``# noqa`` in addition to ``# nopep8``. (Issue #149)

* Expose the ``OptionParser`` factory for better extensibility.


1.4 (2012-12-22)
----------------

* Report E226 instead of E225 for optional whitespace around common
  operators (``*``, ``**``, ``/``, ``+`` and ``-``).  This new error
  code is ignored in the default configuration because PEP 8 recommends
  to "use your own judgement". (Issue #96)

* Lines with a ``# nopep8`` at the end will not issue errors on line
  length E501 or continuation line indentation E12*. (Issue #27)

* Fix AssertionError when the source file contains an invalid line
  ending ``"\r\r\n"``. (Issue #119)

* Read the ``[pep8]`` section of ``tox.ini`` or ``setup.cfg`` if present.
  (Issue #93 and #141)

* Add the Sphinx-based documentation, and publish it
  on http://pep8.readthedocs.org/. (Issue #105)


1.3.4 (2012-12-18)
------------------

* Fix false positive E124 and E128 with comments. (Issue #100)

* Fix error on stdin when running with bpython. (Issue #101)

* Fix false positive E401. (Issue #104)

* Report E231 for nested dictionary in list. (Issue #142)

* Catch E271 at the beginning of the line. (Issue #133)

* Fix false positive E126 for multi-line comments. (Issue #138)

* Fix false positive E221 when operator is preceded by a comma. (Issue #135)

* Fix ``--diff`` failing on one-line hunk. (Issue #137)

* Fix the ``--exclude`` switch for directory paths. (Issue #111)

* Use ``-`` filename to read from standard input. (Issue #128)


1.3.3 (2012-06-27)
------------------

* Fix regression with continuation line checker. (Issue #98)


1.3.2 (2012-06-26)
------------------

* Revert to the previous behaviour for ``--show-pep8``:
  do not imply ``--first``. (Issue #89)

* Add E902 for IO errors. (Issue #87)

* Fix false positive for E121, and missed E124. (Issue #92)

* Set a sensible default path for config file on Windows. (Issue #95)

* Allow ``verbose`` in the configuration file. (Issue #91)

* Show the enforced ``max-line-length`` in the error message. (Issue #86)


1.3.1 (2012-06-18)
------------------

* Explain which configuration options are expected.  Accept and recommend
  the options names with hyphen instead of underscore. (Issue #82)

* Do not read the user configuration when used as a module
  (except if ``config_file=True`` is passed to the ``StyleGuide`` constructor).

* Fix wrong or missing cases for the E12 series.

* Fix cases where E122 was missed. (Issue #81)


1.3 (2012-06-15)
----------------

.. warning::
   The internal API is backwards incompatible.

* Remove global configuration and refactor the library around
  a ``StyleGuide`` class; add the ability to configure various
  reporters. (Issue #35 and #66)

* Read user configuration from ``~/.config/pep8``
  and local configuration from ``./.pep8``. (Issue #22)

* Fix E502 for backslash embedded in multi-line string. (Issue #68)

* Fix E225 for Python 3 iterable unpacking (PEP 3132). (Issue #72)

* Enable the new checkers from the E12 series in the default
  configuration.

* Suggest less error-prone alternatives for E712 errors.

* Rewrite checkers to run faster (E22, E251, E27).

* Fixed a crash when parsed code is invalid (too many
  closing brackets).

* Fix E127 and E128 for continuation line indentation. (Issue #74)

* New option ``--format`` to customize the error format. (Issue #23)

* New option ``--diff`` to check only modified code.  The unified
  diff is read from STDIN.  Example: ``hg diff | pep8 --diff``
  (Issue #39)

* Correctly report the count of failures and set the exit code to 1
  when the ``--doctest`` or the ``--testsuite`` fails.

* Correctly detect the encoding in Python 3. (Issue #69)

* Drop support for Python 2.3, 2.4 and 3.0. (Issue #78)


1.2 (2012-06-01)
----------------

* Add E121 through E128 for continuation line indentation.  These
  checks are disabled by default.  If you want to force all checks,
  use switch ``--select=E,W``.  Patch by Sam Vilain. (Issue #64)

* Add E721 for direct type comparisons. (Issue #47)

* Add E711 and E712 for comparisons to singletons. (Issue #46)

* Fix spurious E225 and E701 for function annotations. (Issue #29)

* Add E502 for explicit line join between brackets.

* Fix E901 when printing source with ``--show-source``.

* Report all errors for each checker, instead of reporting only the
  first occurrence for each line.

* Option ``--show-pep8`` implies ``--first``.


1.1 (2012-05-24)
----------------

* Add E901 for syntax errors. (Issues #63 and #30)

* Add E271, E272, E273 and E274 for extraneous whitespace around
  keywords. (Issue #57)

* Add ``tox.ini`` configuration file for tests. (Issue #61)

* Add ``.travis.yml`` configuration file for continuous integration.
  (Issue #62)


1.0.1 (2012-04-06)
------------------

* Fix inconsistent version numbers.


1.0 (2012-04-04)
----------------

* Fix W602 ``raise`` to handle multi-char names. (Issue #53)


0.7.0 (2012-03-26)
------------------

* Now ``--first`` prints only the first occurrence of each error.
  The ``--repeat`` flag becomes obsolete because it is the default
  behaviour. (Issue #6)

* Allow to specify ``--max-line-length``. (Issue #36)

* Make the shebang more flexible. (Issue #26)

* Add testsuite to the bundle. (Issue #25)

* Fixes for Jython. (Issue #49)

* Add PyPI classifiers. (Issue #43)

* Fix the ``--exclude`` option. (Issue #48)

* Fix W602, accept ``raise`` with 3 arguments. (Issue #34)

* Correctly select all tests if ``DEFAULT_IGNORE == ''``.


0.6.1 (2010-10-03)
------------------

* Fix inconsistent version numbers. (Issue #21)


0.6.0 (2010-09-19)
------------------

* Test suite reorganized and enhanced in order to check more failures
  with fewer test files.  Read the ``run_tests`` docstring for details
  about the syntax.

* Fix E225: accept ``print >>sys.stderr, "..."`` syntax.

* Fix E501 for lines containing multibyte encoded characters. (Issue #7)

* Fix E221, E222, E223, E224 not detected in some cases. (Issue #16)

* Fix E211 to reject ``v = dic['a'] ['b']``. (Issue #17)

* Exit code is always 1 if any error or warning is found. (Issue #10)

* ``--ignore`` checks are now really ignored, especially in
  conjunction with ``--count``. (Issue #8)

* Blank lines with spaces yield W293 instead of W291: some developers
  want to ignore this warning and indent the blank lines to paste their
  code easily in the Python interpreter.

* Fix E301: do not require a blank line before an indented block. (Issue #14)

* Fix E203 to accept NumPy slice notation ``a[0, :]``. (Issue #13)

* Performance improvements.

* Fix decoding and checking non-UTF8 files in Python 3.

* Fix E225: reject ``True+False`` when running on Python 3.

* Fix an exception when the line starts with an operator.

* Allow a new line before closing ``)``, ``}`` or ``]``. (Issue #5)


0.5.0 (2010-02-17)
------------------

* Changed the ``--count`` switch to print to sys.stderr and set
  exit code to 1 if any error or warning is found.

* E241 and E242 are removed from the standard checks. If you want to
  include these checks, use switch ``--select=E,W``. (Issue #4)

* Blank line is not mandatory before the first class method or nested
  function definition, even if there's a docstring. (Issue #1)

* Add the switch ``--version``.

* Fix decoding errors with Python 3. (Issue #13 [1]_)

* Add ``--select`` option which is mirror of ``--ignore``.

* Add checks E261 and E262 for spaces before inline comments.

* New check W604 warns about deprecated usage of backticks.

* New check W603 warns about the deprecated operator ``<>``.

* Performance improvement, due to rewriting of E225.

* E225 now accepts:

  - no whitespace after unary operator or similar. (Issue #9 [1]_)

  - lambda function with argument unpacking or keyword defaults.

* Reserve "2 blank lines" for module-level logical blocks. (E303)

* Allow multi-line comments. (E302, issue #10 [1]_)


0.4.2 (2009-10-22)
------------------

* Decorators on classes and class methods are OK now.


0.4 (2009-10-20)
----------------

* Support for all versions of Python from 2.3 to 3.1.

* New and greatly expanded self tests.

* Added ``--count`` option to print the total number of errors and warnings.

* Further improvements to the handling of comments and blank lines.
  (Issue #1 [1]_ and others changes.)

* Check all py files in directory when passed a directory (Issue
  #2 [1]_). This also prevents an exception when traversing directories
  with non ``*.py`` files.

* E231 should allow commas to be followed by ``)``. (Issue #3 [1]_)

* Spaces are no longer required around the equals sign for keyword
  arguments or default parameter values.


.. [1] These issues refer to the `previous issue tracker`__.
.. __:  http://github.com/cburroughs/pep8.py/issues


0.3.1 (2009-09-14)
------------------

* Fixes for comments: do not count them when checking for blank lines between
  items.

* Added setup.py for pypi upload and easy_installability.


0.2 (2007-10-16)
----------------

* Loads of fixes and improvements.


0.1 (2006-10-01)
----------------

* First release.




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
