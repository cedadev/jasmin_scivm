%define pname virtualenv
%define snapshot 74b1e5b
Summary: Virtual Python Environment builder
Name: python27-%{pname}
Version: 1.8.2
Release: 2.ceda%{?dist}
#Source0: %{pname}-%{version}.tar.gz
Source0: pypa-virtualenv-1.8.1-6-g%{snapshot}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jannis Leidel, Carl Meyer and Brian Rosner <python-virtualenv@groups.google.com>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.virtualenv.org
Requires: python27
BuildRequires: python27

%description


Installation
------------

You can install virtualenv with ``pip install virtualenv``, or the `latest
development version <https://github.com/pypa/virtualenv/tarball/develop>`_
with ``pip install https://github.com/pypa/virtualenv/tarball/develop``.

You can also use ``easy_install``, or if you have no Python package manager
available at all, you can just grab the single file `virtualenv.py`_ and run
it with ``python virtualenv.py``.

.. _virtualenv.py: https://raw.github.com/pypa/virtualenv/master/virtualenv.py

What It Does
------------

``virtualenv`` is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions,
and indirectly permissions.  Imagine you have an application that
needs version 1 of LibFoo, but another application requires version
2.  How can you use both these applications?  If you install
everything into ``/usr/lib/python2.7/site-packages`` (or whatever your
platform's standard location is), it's easy to end up in a situation
where you unintentionally upgrade an application that shouldn't be
upgraded.

Or more generally, what if you want to install an application *and
leave it be*?  If an application works, any change in its libraries or
the versions of those libraries can break the application.

Also, what if you can't install packages into the global
``site-packages`` directory?  For instance, on a shared host.

In all these cases, ``virtualenv`` can help you.  It creates an
environment that has its own installation directories, that doesn't
share libraries with other virtualenv environments (and optionally
doesn't access the globally installed libraries either).

Usage
-----

The basic usage is::

    $ python virtualenv.py ENV

If you install it you can also just do ``virtualenv ENV``.

This creates ``ENV/lib/pythonX.X/site-packages``, where any libraries you
install will go.  It also creates ``ENV/bin/python``, which is a Python
interpreter that uses this environment.  Anytime you use that interpreter
(including when a script has ``#!/path/to/ENV/bin/python`` in it) the libraries
in that environment will be used.

It also installs either `Setuptools
<http://peak.telecommunity.com/DevCenter/setuptools>`_ or `distribute
<http://pypi.python.org/pypi/distribute>`_ into the environment. To use
Distribute instead of setuptools, just call virtualenv like this::

    $ python virtualenv.py --distribute ENV

You can also set the environment variable VIRTUALENV_DISTRIBUTE.

A new virtualenv also includes the `pip <http://pypi.python.org/pypi/pip>`_
installer, so you can use ``ENV/bin/pip`` to install additional packages into
the environment.


activate script
~~~~~~~~~~~~~~~

In a newly created virtualenv there will be a ``bin/activate`` shell
script. For Windows systems, activation scripts are provided for CMD.exe
and Powershell.

On Posix systems you can do::

    $ source bin/activate

This will change your ``$PATH`` so its first entry is the virtualenv's
``bin/`` directory.  (You have to use ``source`` because it changes your
shell environment in-place.) This is all it does; it's purely a
convenience.  If you directly run a script or the python interpreter
from the virtualenv's ``bin/`` directory (e.g.  ``path/to/env/bin/pip``
or ``/path/to/env/bin/python script.py``) there's no need for
activation.

After activating an environment you can use the function ``deactivate`` to
undo the changes to your ``$PATH``.

The ``activate`` script will also modify your shell prompt to indicate
which environment is currently active.  You can disable this behavior,
which can be useful if you have your own custom prompt that already
displays the active environment name.  To do so, set the
``VIRTUAL_ENV_DISABLE_PROMPT`` environment variable to any non-empty
value before running the ``activate`` script.

On Windows you just do::

    > \path\to\env\Scripts\activate

And type `deactivate` to undo the changes.

Based on your active shell (CMD.exe or Powershell.exe), Windows will use
either activate.bat or activate.ps1 (as appropriate) to activate the
virtual environment. If using Powershell, see the notes about code signing
below.

.. note::

    If using Powershell, the ``activate`` script is subject to the
    `execution policies`_ on the system. By default on Windows 7, the system's
    excution policy is set to ``Restricted``, meaning no scripts like the
    ``activate`` script are allowed to be executed. But that can't stop us
    from changing that slightly to allow it to be executed.

    In order to use the script, you have to relax your system's execution
    policy to ``AllSigned``, meaning all scripts on the system must be
    digitally signed to be executed. Since the virtualenv activation
    script is signed by one of the authors (Jannis Leidel) this level of
    the execution policy suffices. As an administrator run::

        PS C:\> Set-ExecutionPolicy AllSigned

    Then you'll be asked to trust the signer, when executing the script.
    You will be prompted with the following::

        PS C:\> virtualenv .\foo
        New python executable in C:\foo\Scripts\python.exe
        Installing setuptools................done.
        Installing pip...................done.
        PS C:\> .\foo\scripts\activate

        Do you want to run software from this untrusted publisher?
        File C:\foo\scripts\activate.ps1 is published by E=jannis@leidel.info,
        CN=Jannis Leidel, L=Berlin, S=Berlin, C=DE, Description=581796-Gh7xfJxkxQSIO4E0
        and is not trusted on your system. Only run scripts from trusted publishers.
        [V] Never run  [D] Do not run  [R] Run once  [A] Always run  [?] Help
        (default is "D"):A
        (foo) PS C:\>

    If you select ``[A] Always Run``, the certificate will be added to the
    Trusted Publishers of your user account, and will be trusted in this
    user's context henceforth. If you select ``[R] Run Once``, the script will
    be run, but you will be prometed on a subsequent invocation. Advanced users
    can add the signer's certificate to the Trusted Publishers of the Computer
    account to apply to all users (though this technique is out of scope of this
    document).

    Alternatively, you may relax the system execution policy to allow running
    of local scripts without verifying the code signature using the following::

        PS C:\> Set-ExecutionPolicy RemoteSigned

    Since the ``activate.ps1`` script is generated locally for each virtualenv,
    it is not considered a remote script and can then be executed.

.. _`execution policies`: http://technet.microsoft.com/en-us/library/dd347641.aspx

The ``--system-site-packages`` Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you build with ``virtualenv --system-site-packages ENV``, your virtual
environment will inherit packages from ``/usr/lib/python2.7/site-packages``
(or wherever your global site-packages directory is).

This can be used if you have control over the global site-packages directory,
and you want to depend on the packages there.  If you want isolation from the
global system, do not use this flag.


Environment variables and configuration files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

virtualenv can not only be configured by passing command line options such as
``--distribute`` but also by two other means:

- Environment variables

  Each command line option is automatically used to look for environment
  variables with the name format ``VIRTUALENV_<UPPER_NAME>``. That means
  the name of the command line options are capitalized and have dashes
  (``'-'``) replaced with underscores (``'_'``).

  For example, to automatically install Distribute instead of setuptools
  you can also set an environment variable::

      $ export VIRTUALENV_DISTRIBUTE=true
      $ python virtualenv.py ENV

  It's the same as passing the option to virtualenv directly::

      $ python virtualenv.py --distribute ENV

  This also works for appending command line options, like ``--find-links``.
  Just leave an empty space between the passsed values, e.g.::

      $ export VIRTUALENV_EXTRA_SEARCH_DIR="/path/to/dists /path/to/other/dists"
      $ virtualenv ENV

  is the same as calling::

      $ python virtualenv.py --extra-search-dir=/path/to/dists --extra-search-dir=/path/to/other/dists ENV

- Config files

  virtualenv also looks for a standard ini config file. On Unix and Mac OS X
  that's ``$HOME/.virtualenv/virtualenv.ini`` and on Windows, it's
  ``%APPDATA%\virtualenv\virtualenv.ini``.

  The names of the settings are derived from the long command line option,
  e.g. the option ``--distribute`` would look like this::

      [virtualenv]
      distribute = true

  Appending options like ``--extra-search-dir`` can be written on multiple
  lines::

      [virtualenv]
      extra-search-dir =
          /path/to/dists
          /path/to/other/dists

Please have a look at the output of ``virtualenv --help`` for a full list
of supported options.

Windows Notes
~~~~~~~~~~~~~

Some paths within the virtualenv are slightly different on Windows: scripts and
executables on Windows go in ``ENV\Scripts\`` instead of ``ENV/bin/`` and
libraries go in ``ENV\Lib\`` rather than ``ENV/lib/``.

To create a virtualenv under a path with spaces in it on Windows, you'll need
the `win32api <http://sourceforge.net/projects/pywin32/>`_ library installed.

PyPy Support
~~~~~~~~~~~~

Beginning with virtualenv version 1.5 `PyPy <http://pypy.org>`_ is
supported. To use PyPy 1.4 or 1.4.1, you need a version of virtualenv >= 1.5.
To use PyPy 1.5, you need a version of virtualenv >= 1.6.1.

Creating Your Own Bootstrap Scripts
-----------------------------------

While this creates an environment, it doesn't put anything into the
environment.  Developers may find it useful to distribute a script
that sets up a particular environment, for example a script that
installs a particular web application.

To create a script like this, call
``virtualenv.create_bootstrap_script(extra_text)``, and write the
result to your new bootstrapping script.  Here's the documentation
from the docstring:

Creates a bootstrap script, which is like this script but with
extend_parser, adjust_options, and after_install hooks.

This returns a string that (written to disk of course) can be used
as a bootstrap script with your own customizations.  The script
will be the standard virtualenv.py script, with your extra text
added (your extra text should be Python code).

If you include these functions, they will be called:

``extend_parser(optparse_parser)``:
    You can add or remove options from the parser here.

``adjust_options(options, args)``:
    You can change options here, or change the args (if you accept
    different kinds of arguments, be sure you modify ``args`` so it is
    only ``[DEST_DIR]``).

``after_install(options, home_dir)``:

    After everything is installed, this function is called.  This
    is probably the function you are most likely to use.  An
    example would be::

        def after_install(options, home_dir):
            if sys.platform == 'win32':
                bin = 'Scripts'
            else:
                bin = 'bin'
            subprocess.call([join(home_dir, bin, 'easy_install'),
                             'MyPackage'])
            subprocess.call([join(home_dir, bin, 'my-package-script'),
                             'setup', home_dir])

    This example immediately installs a package, and runs a setup
    script from that package.

Bootstrap Example
~~~~~~~~~~~~~~~~~

Here's a more concrete example of how you could use this::

    import virtualenv, textwrap
    output = virtualenv.create_bootstrap_script(textwrap.dedent("""
    import os, subprocess
    def after_install(options, home_dir):
        etc = join(home_dir, 'etc')
        if not os.path.exists(etc):
            os.makedirs(etc)
        subprocess.call([join(home_dir, 'bin', 'easy_install'),
                         'BlogApplication'])
        subprocess.call([join(home_dir, 'bin', 'paster'),
                         'make-config', 'BlogApplication',
                         join(etc, 'blog.ini')])
        subprocess.call([join(home_dir, 'bin', 'paster'),
                         'setup-app', join(etc, 'blog.ini')])
    """))
    f = open('blog-bootstrap.py', 'w').write(output)

Another example is available `here
<https://github.com/socialplanning/fassembler/blob/master/fassembler/create-venv-script.py>`_.


Using Virtualenv without ``bin/python``
---------------------------------------

Sometimes you can't or don't want to use the Python interpreter
created by the virtualenv.  For instance, in a `mod_python
<http://www.modpython.org/>`_ or `mod_wsgi <http://www.modwsgi.org/>`_
environment, there is only one interpreter.

Luckily, it's easy.  You must use the custom Python interpreter to
*install* libraries.  But to *use* libraries, you just have to be sure
the path is correct.  A script is available to correct the path.  You
can setup the environment like::

    activate_this = '/path/to/env/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))

This will change ``sys.path`` and even change ``sys.prefix``, but also allow
you to use an existing interpreter.  Items in your environment will show up
first on ``sys.path``, before global items.  However, global items will
always be accessible (as if the ``--system-site-packages`` flag had been used
in creating the environment, whether it was or not).  Also, this cannot undo
the activation of other environments, or modules that have been imported.
You shouldn't try to, for instance, activate an environment before a web
request; you should activate *one* environment as early as possible, and not
do it again in that process.

Making Environments Relocatable
-------------------------------

Note: this option is somewhat experimental, and there are probably
caveats that have not yet been identified.  Also this does not
currently work on Windows.

Normally environments are tied to a specific path.  That means that
you cannot move an environment around or copy it to another computer.
You can fix up an environment to make it relocatable with the
command::

    $ virtualenv --relocatable ENV

This will make some of the files created by setuptools or distribute
use relative paths, and will change all the scripts to use ``activate_this.py``
instead of using the location of the Python interpreter to select the
environment.

**Note:** you must run this after you've installed *any* packages into
the environment.  If you make an environment relocatable, then
install a new package, you must run ``virtualenv --relocatable``
again.

Also, this **does not make your packages cross-platform**.  You can
move the directory around, but it can only be used on other similar
computers.  Some known environmental differences that can cause
incompatibilities: a different version of Python, when one platform
uses UCS2 for its internal unicode representation and another uses
UCS4 (a compile-time option), obvious platform changes like Windows
vs. Linux, or Intel vs. ARM, and if you have libraries that bind to C
libraries on the system, if those C libraries are located somewhere
different (either different versions, or a different filesystem
layout).

If you use this flag to create an environment, currently, the
``--system-site-packages`` option will be implied.

The ``--extra-search-dir`` option
---------------------------------

When it creates a new environment, virtualenv installs either
setuptools or distribute, and pip.  In normal operation, the latest
releases of these packages are fetched from the `Python Package Index
<http://pypi.python.org>`_ (PyPI). In some circumstances, this
behavior may not be wanted, for example if you are using virtualenv
during a deployment and do not want to depend on Internet access and
PyPI availability.

As an alternative, you can provide your own versions of setuptools,
distribute and/or pip on the filesystem, and tell virtualenv to use
those distributions instead of downloading them from the Internet.  To
use this feature, pass one or more ``--extra-search-dir`` options to
virtualenv like this::

    $ virtualenv --extra-search-dir=/path/to/distributions ENV

The ``/path/to/distributions`` path should point to a directory that
contains setuptools, distribute and/or pip distributions.  Setuptools
distributions must be ``.egg`` files; distribute and pip distributions
should be `.tar.gz` source distributions.

Virtualenv will still download these packages if no satisfactory local
distributions are found.

If you are really concerned about virtualenv fetching these packages
from the Internet and want to ensure that it never will, you can also
provide an option ``--never-download`` like so::

    $ virtualenv --extra-search-dir=/path/to/distributions --never-download ENV

If this option is provided, virtualenv will never try to download
setuptools/distribute or pip. Instead, it will exit with status code 1
if it fails to find local distributions for any of these required
packages. The local distribution lookup is done in this order and the
following locations:

    #. The current directory.
    #. The directory where virtualenv.py is located.
    #. A ``virtualenv_support`` directory relative to the directory where
       virtualenv.py is located.
    #. If the file being executed is not named virtualenv.py (i.e. is a boot
       script), a ``virtualenv_support`` directory relative to wherever
       virtualenv.py is actually installed.

Compare & Contrast with Alternatives
------------------------------------

There are several alternatives that create isolated environments:

* ``workingenv`` (which I do not suggest you use anymore) is the
  predecessor to this library.  It used the main Python interpreter,
  but relied on setting ``$PYTHONPATH`` to activate the environment.
  This causes problems when running Python scripts that aren't part of
  the environment (e.g., a globally installed ``hg`` or ``bzr``).  It
  also conflicted a lot with Setuptools.

* `virtual-python
  <http://peak.telecommunity.com/DevCenter/EasyInstall#creating-a-virtual-python>`_
  is also a predecessor to this library.  It uses only symlinks, so it
  couldn't work on Windows.  It also symlinks over the *entire*
  standard library and global ``site-packages``.  As a result, it
  won't see new additions to the global ``site-packages``.

  This script only symlinks a small portion of the standard library
  into the environment, and so on Windows it is feasible to simply
  copy these files over.  Also, it creates a new/empty
  ``site-packages`` and also adds the global ``site-packages`` to the
  path, so updates are tracked separately.  This script also installs
  Setuptools automatically, saving a step and avoiding the need for
  network access.

* `zc.buildout <http://pypi.python.org/pypi/zc.buildout>`_ doesn't
  create an isolated Python environment in the same style, but
  achieves similar results through a declarative config file that sets
  up scripts with very particular packages.  As a declarative system,
  it is somewhat easier to repeat and manage, but more difficult to
  experiment with.  ``zc.buildout`` includes the ability to setup
  non-Python systems (e.g., a database server or an Apache instance).

I *strongly* recommend anyone doing application development or
deployment use one of these tools.

Contributing
------------

Refer to the `contributing to pip`_ documentation - it applies equally to
virtualenv, except that virtualenv issues should filed on the `virtualenv
repo`_ at GitHub.

Virtualenv's release schedule is tied to pip's -- each time there's a new pip
release, there will be a new virtualenv release that bundles the new version of
pip.

.. _contributing to pip: http://www.pip-installer.org/en/latest/contributing.html
.. _virtualenv repo: https://github.com/pypa/virtualenv/

Running the tests
~~~~~~~~~~~~~~~~~

Virtualenv's test suite is small and not yet at all comprehensive, but we aim
to grow it.

The easy way to run tests (handles test dependencies automatically)::

    $ python2.7 setup.py test

If you want to run only a selection of the tests, you'll need to run them
directly with nose instead. Create a virtualenv, and install required
packages::

    $ pip install nose mock

Run nosetests::

    $ nosetests

Or select just a single test file to run::

    $ nosetests tests.test_virtualenv


Other Documentation and Links
-----------------------------

* James Gardner has written a tutorial on using `virtualenv with
  Pylons
  <http://wiki.pylonshq.com/display/pylonscookbook/Using+a+Virtualenv+Sandbox>`_.

* `Blog announcement
  <http://blog.ianbicking.org/2007/10/10/workingenv-is-dead-long-live-virtualenv/>`_.

* Doug Hellmann wrote a description of his `command-line work flow
  using virtualenv (virtualenvwrapper)
  <http://www.doughellmann.com/articles/CompletelyDifferent-2008-05-virtualenvwrapper/index.html>`_
  including some handy scripts to make working with multiple
  environments easier.  He also wrote `an example of using virtualenv
  to try IPython
  <http://www.doughellmann.com/articles/CompletelyDifferent-2008-02-ipython-and-virtualenv/index.html>`_.

* Chris Perkins created a `showmedo video including virtualenv
  <http://showmedo.com/videos/video?name=2910000&fromSeriesID=291>`_.

* `Using virtualenv with mod_wsgi
  <http://code.google.com/p/modwsgi/wiki/VirtualEnvironments>`_.

* `virtualenv commands
  <https://github.com/thisismedium/virtualenv-commands>`_ for some more
  workflow-related tools around virtualenv.

Status and License
------------------

``virtualenv`` is a successor to `workingenv
<http://cheeseshop.python.org/pypi/workingenv.py>`_, and an extension
of `virtual-python
<http://peak.telecommunity.com/DevCenter/EasyInstall#creating-a-virtual-python>`_.

It was written by Ian Bicking, sponsored by the `Open Planning
Project <http://openplans.org>`_ and is now maintained by a
`group of developers <https://github.com/pypa/virtualenv/raw/master/AUTHORS.txt>`_.
It is licensed under an
`MIT-style permissive license <https://github.com/pypa/virtualenv/raw/master/LICENSE.txt>`_.

Changes & News
--------------

.. warning::

   Python bugfix releases 2.6.8, 2.7.3, 3.1.5 and 3.2.3 include a change that
   will cause "import random" to fail with "cannot import name urandom" on any
   virtualenv created on a Unix host with an earlier release of Python
   2.6/2.7/3.1/3.2, if the underlying system Python is upgraded. This is due to
   the fact that a virtualenv uses the system Python's standard library but
   contains its own copy of the Python interpreter, so an upgrade to the system
   Python results in a mismatch between the version of the Python interpreter
   and the version of the standard library. It can be fixed by removing
   ``$ENV/bin/python`` and re-running virtualenv on the same target directory
   with the upgraded Python.


develop (unreleased)
~~~~~~~~~~~~~~~~~~~~

* Make it possible to create a virtualenv from within a Python
  3.3. pyvenv. Thanks Chris McDonough for the report.


1.8.2 (2012-09-06)
~~~~~~~~~~~~~~~~~~

* Updated the included pip version to 1.2.1 to fix regressions introduced
  there in 1.2.


1.8.1 (2012-09-03)
~~~~~~~~~~~~~~~~~~

* Fixed distribute version used with `--never-download`. Thanks michr for
  report and patch.

* Fix creating Python 3.3 based virtualenvs by unsetting the
  ``__PYVENV_LAUNCHER__`` environment variable in subprocesses.


1.8 (2012-09-01)
~~~~~~~~~~~~~~~~

* **Dropped support for Python 2.4** The minimum supported Python version is
  now Python 2.5.

* Fix `--relocatable` on systems that use lib64. Fixes #78. Thanks Branden
  Rolston.

* Symlink some additional modules under Python 3. Fixes #194. Thanks Vinay
  Sajip, Ian Clelland, and Stefan Holek for the report.

* Fix ``--relocatable`` when a script uses ``__future__`` imports. Thanks
  Branden Rolston.

* Fix a bug in the config option parser that prevented setting negative
  options with environemnt variables. Thanks Ralf Schmitt.

* Allow setting ``--no-site-packages`` from the config file.

* Use ``/usr/bin/multiarch-platform`` if available to figure out the include
  directory. Thanks for the patch, Mika Laitio.

* Fix ``install_name_tool`` replacement to work on Python 3.X.

* Handle paths of users' site-packages on Mac OS X correctly when changing
  the prefix.

* Updated the embedded version of distribute to 0.6.28 and pip to 1.2.


1.7.2 (2012-06-22)
~~~~~~~~~~~~~~~~~~

* Updated to distribute 0.6.27.

* Fix activate.fish on OS X. Fixes #8. Thanks David Schoonover.

* Create a virtualenv-x.x script with the Python version when installing, so
  virtualenv for multiple Python versions can be installed to the same
  script location. Thanks Miki Tebeka.

* Restored ability to create a virtualenv with a path longer than 78
  characters, without breaking creation of virtualenvs with non-ASCII paths.
  Thanks, Bradley Ayers.

* Added ability to create virtualenvs without having installed Apple's
  developers tools (using an own implementation of ``install_name_tool``).
  Thanks Mike Hommey.

* Fixed PyPy and Jython support on Windows. Thanks Konstantin Zemlyak.

* Added pydoc script to ease use. Thanks Marc Abramowitz. Fixes #149.

* Fixed creating a bootstrap script on Python 3. Thanks Raul Leal. Fixes #280.

* Fixed inconsistency when having set the ``PYTHONDONTWRITEBYTECODE`` env var
  with the --distribute option or the ``VIRTUALENV_USE_DISTRIBUTE`` env var.
  ``VIRTUALENV_USE_DISTRIBUTE`` is now considered again as a legacy alias.


1.7.1.2 (2012-02-17)
~~~~~~~~~~~~~~~~~~~~

* Fixed minor issue in `--relocatable`. Thanks, Cap Petschulat.


1.7.1.1 (2012-02-16)
~~~~~~~~~~~~~~~~~~~~

* Bumped the version string in ``virtualenv.py`` up, too.

* Fixed rST rendering bug of long description.


1.7.1 (2012-02-16)
~~~~~~~~~~~~~~~~~~

* Update embedded pip to version 1.1.

* Fix `--relocatable` under Python 3. Thanks Doug Hellmann.

* Added environ PATH modification to activate_this.py. Thanks Doug
  Napoleone. Fixes #14.

* Support creating virtualenvs directly from a Python build directory on
  Windows. Thanks CBWhiz. Fixes #139.

* Use non-recursive symlinks to fix things up for posix_local install
  scheme. Thanks michr.

* Made activate script available for use with msys and cygwin on Windows.
  Thanks Greg Haskins, Cliff Xuan, Jonathan Griffin and Doug Napoleone.
  Fixes #176.

* Fixed creation of virtualenvs on Windows when Python is not installed for
  all users. Thanks Anatoly Techtonik for report and patch and Doug
  Napoleone for testing and confirmation. Fixes #87.

* Fixed creation of virtualenvs using -p in installs where some modules
  that ought to be in the standard library (e.g. `readline`) are actually
  installed in `site-packages` next to `virtualenv.py`. Thanks Greg Haskins
  for report and fix. Fixes #167.

* Added activation script for Powershell (signed by Jannis Leidel). Many
  thanks to Jason R. Coombs.


1.7 (2011-11-30)
~~~~~~~~~~~~~~~~

* Gave user-provided ``--extra-search-dir`` priority over default dirs for
  finding setuptools/distribute (it already had priority for finding pip).
  Thanks Ethan Jucovy.

* Updated embedded Distribute release to 0.6.24. Thanks Alex Gronholm.

* Made ``--no-site-packages`` behavior the default behavior.  The
  ``--no-site-packages`` flag is still permitted, but displays a warning when
  used. Thanks Chris McDonough.

* New flag: ``--system-site-packages``; this flag should be passed to get the
  previous default global-site-package-including behavior back.

* Added ability to set command options as environment variables and options
  in a ``virtualenv.ini`` file.

* Fixed various encoding related issues with paths. Thanks Gunnlaugur Thor Briem.

* Made ``virtualenv.py`` script executable.


1.6.4 (2011-07-21)
~~~~~~~~~~~~~~~~~~

* Restored ability to run on Python 2.4, too.


1.6.3 (2011-07-16)
~~~~~~~~~~~~~~~~~~

* Restored ability to run on Python < 2.7.


1.6.2 (2011-07-16)
~~~~~~~~~~~~~~~~~~

* Updated embedded distribute release to 0.6.19.

* Updated embedded pip release to 1.0.2.

* Fixed #141 - Be smarter about finding pkg_resources when using the
  non-default Python intepreter (by using the ``-p`` option).

* Fixed #112 - Fixed path in docs.

* Fixed #109 - Corrected doctests of a Logger method.

* Fixed #118 - Fixed creating virtualenvs on platforms that use the
  "posix_local" install scheme, such as Ubuntu with Python 2.7.

* Add missing library to Python 3 virtualenvs (``_dummy_thread``).


1.6.1 (2011-04-30)
~~~~~~~~~~~~~~~~~~

* Start to use git-flow.

* Added support for PyPy 1.5

* Fixed #121 -- added sanity-checking of the -p argument. Thanks Paul Nasrat.

* Added progress meter for pip installation as well as setuptools. Thanks Ethan
  Jucovy.

* Added --never-download and --search-dir options. Thanks Ethan Jucovy.


1.6
~~~

* Added Python 3 support! Huge thanks to Vinay Sajip and Vitaly Babiy.

* Fixed creation of virtualenvs on Mac OS X when standard library modules
  (readline) are installed outside the standard library.

* Updated bundled pip to 1.0.


1.5.2
~~~~~

* Moved main repository to Github: https://github.com/pypa/virtualenv

* Transferred primary maintenance from Ian to Jannis Leidel, Carl Meyer and Brian Rosner

* Fixed a few more pypy related bugs.

* Updated bundled pip to 0.8.2.

* Handed project over to new team of maintainers.

* Moved virtualenv to Github at https://github.com/pypa/virtualenv


1.5.1
~~~~~

* Added ``_weakrefset`` requirement for Python 2.7.1.

* Fixed Windows regression in 1.5


1.5
~~~

* Include pip 0.8.1.

* Add support for PyPy.

* Uses a proper temporary dir when installing environment requirements.

* Add ``--prompt`` option to be able to override the default prompt prefix.

* Fix an issue with ``--relocatable`` on Windows.

* Fix issue with installing the wrong version of distribute.

* Add fish and csh activate scripts.


1.4.9
~~~~~

* Include pip 0.7.2


1.4.8
~~~~~

* Fix for Mac OS X Framework builds that use
  ``--universal-archs=intel``

* Fix ``activate_this.py`` on Windows.

* Allow ``$PYTHONHOME`` to be set, so long as you use ``source
  bin/activate`` it will get unset; if you leave it set and do not
  activate the environment it will still break the environment.

* Include pip 0.7.1


1.4.7
~~~~~

* Include pip 0.7


1.4.6
~~~~~

* Allow ``activate.sh`` to skip updating the prompt (by setting
  ``$VIRTUAL_ENV_DISABLE_PROMPT``).


1.4.5
~~~~~

* Include pip 0.6.3

* Fix ``activate.bat`` and ``deactivate.bat`` under Windows when
  ``PATH`` contained a parenthesis


1.4.4
~~~~~

* Include pip 0.6.2 and Distribute 0.6.10

* Create the ``virtualenv`` script even when Setuptools isn't
  installed

* Fix problem with ``virtualenv --relocate`` when ``bin/`` has
  subdirectories (e.g., ``bin/.svn/``); from Alan Franzoni.

* If you set ``$VIRTUALENV_DISTRIBUTE`` then virtualenv will use
  Distribute by default (so you don't have to remember to use
  ``--distribute``).


1.4.3
~~~~~

* Include pip 0.6.1


1.4.2
~~~~~

* Fix pip installation on Windows

* Fix use of stand-alone ``virtualenv.py`` (and boot scripts)

* Exclude ~/.local (user site-packages) from environments when using
  ``--no-site-packages``


1.4.1
~~~~~

* Include pip 0.6


1.4
~~~

* Updated setuptools to 0.6c11

* Added the --distribute option

* Fixed packaging problem of support-files


1.3.4
~~~~~

* Virtualenv now copies the actual embedded Python binary on
  Mac OS X to fix a hang on Snow Leopard (10.6).

* Fail more gracefully on Windows when ``win32api`` is not installed.

* Fix site-packages taking precedent over Jython's ``__classpath__``
  and also specially handle the new ``__pyclasspath__`` entry in
  ``sys.path``.

* Now copies Jython's ``registry`` file to the virtualenv if it exists.

* Better find libraries when compiling extensions on Windows.

* Create ``Scripts\pythonw.exe`` on Windows.

* Added support for the Debian/Ubuntu
  ``/usr/lib/pythonX.Y/dist-packages`` directory.

* Set ``distutils.sysconfig.get_config_vars()['LIBDIR']`` (based on
  ``sys.real_prefix``) which is reported to help building on Windows.

* Make ``deactivate`` work on ksh

* Fixes for ``--python``: make it work with ``--relocatable`` and the
  symlink created to the exact Python version.


1.3.3
~~~~~

* Use Windows newlines in ``activate.bat``, which has been reported to help
  when using non-ASCII directory names.

* Fixed compatibility with Jython 2.5b1.

* Added a function ``virtualenv.install_python`` for more fine-grained
  access to what ``virtualenv.create_environment`` does.

* Fix `a problem <https://bugs.launchpad.net/virtualenv/+bug/241581>`_
  with Windows and paths that contain spaces.

* If ``/path/to/env/.pydistutils.cfg`` exists (or
  ``/path/to/env/pydistutils.cfg`` on Windows systems) then ignore
  ``~/.pydistutils.cfg`` and use that other file instead.

* Fix ` a problem
  <https://bugs.launchpad.net/virtualenv/+bug/340050>`_ picking up
  some ``.so`` libraries in ``/usr/local``.


1.3.2
~~~~~

* Remove the ``[install] prefix = ...`` setting from the virtualenv
  ``distutils.cfg`` -- this has been causing problems for a lot of
  people, in rather obscure ways.

* If you use a boot script it will attempt to import ``virtualenv``
  and find a pre-downloaded Setuptools egg using that.

* Added platform-specific paths, like ``/usr/lib/pythonX.Y/plat-linux2``


1.3.1
~~~~~

* Real Python 2.6 compatibility.  Backported the Python 2.6 updates to
  ``site.py``, including `user directories
  <http://docs.python.org/dev/whatsnew/2.6.html#pep-370-per-user-site-packages-directory>`_
  (this means older versions of Python will support user directories,
  whether intended or not).

* Always set ``[install] prefix`` in ``distutils.cfg`` -- previously
  on some platforms where a system-wide ``distutils.cfg`` was present
  with a ``prefix`` setting, packages would be installed globally
  (usually in ``/usr/local/lib/pythonX.Y/site-packages``).

* Sometimes Cygwin seems to leave ``.exe`` off ``sys.executable``; a
  workaround is added.

* Fix ``--python`` option.

* Fixed handling of Jython environments that use a
  jython-complete.jar.


1.3
~~~

* Update to Setuptools 0.6c9
* Added an option ``virtualenv --relocatable EXISTING_ENV``, which
  will make an existing environment "relocatable" -- the paths will
  not be absolute in scripts, ``.egg-info`` and ``.pth`` files.  This
  may assist in building environments that can be moved and copied.
  You have to run this *after* any new packages installed.
* Added ``bin/activate_this.py``, a file you can use like
  ``execfile("path_to/activate_this.py",
  dict(__file__="path_to/activate_this.py"))`` -- this will activate
  the environment in place, similar to what `the mod_wsgi example
  does <http://code.google.com/p/modwsgi/wiki/VirtualEnvironments>`_.
* For Mac framework builds of Python, the site-packages directory
  ``/Library/Python/X.Y/site-packages`` is added to ``sys.path``, from
  Andrea Rech.
* Some platform-specific modules in Macs are added to the path now
  (``plat-darwin/``, ``plat-mac/``, ``plat-mac/lib-scriptpackages``),
  from Andrea Rech.
* Fixed a small Bashism in the ``bin/activate`` shell script.
* Added ``__future__`` to the list of required modules, for Python
  2.3.  You'll still need to backport your own ``subprocess`` module.
* Fixed the ``__classpath__`` entry in Jython's ``sys.path`` taking
  precedent over virtualenv's libs.


1.2
~~~

* Added a ``--python`` option to select the Python interpreter.
* Add ``warnings`` to the modules copied over, for Python 2.6 support.
* Add ``sets`` to the module copied over for Python 2.3 (though Python
  2.3 still probably doesn't work).


1.1.1
~~~~~

* Added support for Jython 2.5.


1.1
~~~

* Added support for Python 2.6.
* Fix a problem with missing ``DLLs/zlib.pyd`` on Windows.  Create
* ``bin/python`` (or ``bin/python.exe``) even when you run virtualenv
  with an interpreter named, e.g., ``python2.4``
* Fix MacPorts Python
* Added --unzip-setuptools option
* Update to Setuptools 0.6c8
* If the current directory is not writable, run ez_setup.py in ``/tmp``
* Copy or symlink over the ``include`` directory so that packages will
  more consistently compile.


1.0
~~~

* Fix build on systems that use ``/usr/lib64``, distinct from
  ``/usr/lib`` (specifically CentOS x64).
* Fixed bug in ``--clear``.
* Fixed typos in ``deactivate.bat``.
* Preserve ``$PYTHONPATH`` when calling subprocesses.


0.9.2
~~~~~

* Fix include dir copying on Windows (makes compiling possible).
* Include the main ``lib-tk`` in the path.
* Patch ``distutils.sysconfig``: ``get_python_inc`` and
  ``get_python_lib`` to point to the global locations.
* Install ``distutils.cfg`` before Setuptools, so that system
  customizations of ``distutils.cfg`` won't effect the installation.
* Add ``bin/pythonX.Y`` to the virtualenv (in addition to
  ``bin/python``).
* Fixed an issue with Mac Framework Python builds, and absolute paths
  (from Ronald Oussoren).


0.9.1
~~~~~

* Improve ability to create a virtualenv from inside a virtualenv.
* Fix a little bug in ``bin/activate``.
* Actually get ``distutils.cfg`` to work reliably.


0.9
~~~

* Added ``lib-dynload`` and ``config`` to things that need to be
  copied over in an environment.
* Copy over or symlink the ``include`` directory, so that you can
  build packages that need the C headers.
* Include a ``distutils`` package, so you can locally update
  ``distutils.cfg`` (in ``lib/pythonX.Y/distutils/distutils.cfg``).
* Better avoid downloading Setuptools, and hitting PyPI on environment
  creation.
* Fix a problem creating a ``lib64/`` directory.
* Should work on MacOSX Framework builds (the default Python
  installations on Mac).  Thanks to Ronald Oussoren.


0.8.4
~~~~~

* Windows installs would sometimes give errors about ``sys.prefix`` that
  were inaccurate.
* Slightly prettier output.


0.8.3
~~~~~

* Added support for Windows.


0.8.2
~~~~~

* Give a better warning if you are on an unsupported platform (Mac
  Framework Pythons, and Windows).
* Give error about running while inside a workingenv.
* Give better error message about Python 2.3.


0.8.1
~~~~~

Fixed packaging of the library.


0.8
~~~

Initial release.  Everything is changed and new!


%prep
%setup -n pypa-virtualenv-%{snapshot}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES1

rm $RPM_BUILD_ROOT%{_bindir}/virtualenv
egrep -v "^%{_bindir}/virtualenv$" INSTALLED_FILES1 > INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)