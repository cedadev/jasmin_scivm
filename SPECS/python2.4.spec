Summary: An old unsupported Python version
Name: %{python}
Version: 2.4.6
Release: 1.ceda%{?dist}
License: Python
Group: Development/Languages
Provides: python-abi = %{pybasever}
Provides: python(abi) = %{pybasever}
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: readline-devel, openssl-devel, gmp-devel
BuildRequires: ncurses-devel, gdbm-devel, zlib-devel

BuildRequires: expat-devel >= 2.0.1-10

BuildRequires: libGL-devel tk tix gcc-c++ libX11-devel glibc-devel
BuildRequires: bzip2 tar /usr/bin/find pkgconfig tcl-devel tk-devel
BuildRequires: tix-devel bzip2-devel sqlite-devel
BuildRequires: autoconf
BuildRequires: db4-devel >= 4.7
BuildRequires: libffi-devel

URL: http://www.python.org/

%description
Python 2.4 basic package, for use on JASMIN without support.
Please use 2.7 for supported version.

%prep
%setup -q -n Python-%{version}

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc LICENSE README
%if %{main_python}
%{_bindir}/pydoc*
%{_bindir}/%{python}
%{_bindir}/python2
%{_bindir}/python2-config
%else
%exclude %{_bindir}/pydoc*
%exclude %{_bindir}/%{python}
%exclude %{_bindir}/python2
%exclude %{_bindir}/python2-config
%endif # main_python
%{_bindir}/python%{pybasever}
%{_mandir}/*/*

%dir %{pylibdir}
%dir %{dynload_dir}
%{dynload_dir}/Python-%{version}-py%{pybasever}.egg-info
%{dynload_dir}/*.so
#%{dynload_dir}/_bisectmodule.so
#%{dynload_dir}/_bsddb.so
#%{dynload_dir}/_bytesio.so
#%{dynload_dir}/_codecs_cn.so
#%{dynload_dir}/_codecs_hk.so
#%{dynload_dir}/_codecs_iso2022.so
#%{dynload_dir}/_codecs_jp.so
#%{dynload_dir}/_codecs_kr.so
#%{dynload_dir}/_codecs_tw.so
#%{dynload_dir}/_collectionsmodule.so
#%{dynload_dir}/_csv.so
#%{dynload_dir}/_ctypes.so
#%{dynload_dir}/_curses.so
#%{dynload_dir}/_curses_panel.so
#%{dynload_dir}/_elementtree.so
#%{dynload_dir}/_fileio.so
#%{dynload_dir}/_functoolsmodule.so
#%{dynload_dir}/_hashlib.so
#%{dynload_dir}/_heapq.so
#%{dynload_dir}/_hotshot.so
#%{dynload_dir}/_json.so
#%{dynload_dir}/_localemodule.so
#%{dynload_dir}/_lsprof.so
#%{dynload_dir}/_multibytecodecmodule.so
#%{dynload_dir}/_multiprocessing.so
#%{dynload_dir}/_randommodule.so
#%{dynload_dir}/_socketmodule.so
#%{dynload_dir}/_sqlite3.so
#%{dynload_dir}/_ssl.so
#%{dynload_dir}/_struct.so
#%{dynload_dir}/_weakref.so
#%{dynload_dir}/arraymodule.so
#%{dynload_dir}/audioop.so
#%{dynload_dir}/binascii.so
#%{dynload_dir}/bz2.so
#%{dynload_dir}/cPickle.so
#%{dynload_dir}/cStringIO.so
#%{dynload_dir}/cmathmodule.so
#%{dynload_dir}/_cryptmodule.so
#%{dynload_dir}/datetime.so
#%{dynload_dir}/dbm.so
#%{dynload_dir}/dlmodule.so
#%{dynload_dir}/fcntlmodule.so
#%{dynload_dir}/future_builtins.so
#%{dynload_dir}/gdbmmodule.so
#%{dynload_dir}/grpmodule.so
#%{dynload_dir}/imageop.so
#%{dynload_dir}/itertoolsmodule.so
#%{dynload_dir}/linuxaudiodev.so
#%{dynload_dir}/mathmodule.so
#%{dynload_dir}/mmapmodule.so
#%{dynload_dir}/nismodule.so
#%{dynload_dir}/operator.so
#%{dynload_dir}/ossaudiodev.so
#%{dynload_dir}/parsermodule.so
#%{dynload_dir}/pyexpat.so
#%{dynload_dir}/readline.so
#%{dynload_dir}/resource.so
#%{dynload_dir}/selectmodule.so
#%{dynload_dir}/spwdmodule.so
#%{dynload_dir}/stropmodule.so
#%{dynload_dir}/syslog.so
#%{dynload_dir}/termios.so
#%{dynload_dir}/timemodule.so
#%{dynload_dir}/timingmodule.so
#%{dynload_dir}/unicodedata.so
#%{dynload_dir}/xxsubtype.so
#%{dynload_dir}/zlibmodule.so

%if %{main_python}
%{_libdir}/pkgconfig/*
%else
%exclude %{_libdir}/pkgconfig/*
%endif

%{pylibdir}/LICENSE.txt
%dir %{pylibdir}/importlib
%{pylibdir}/importlib/*
%dir %{pylibdir}/pydoc_data
%{pylibdir}/pydoc_data/*
%dir %{pylibdir}/unittest
%{pylibdir}/unittest/*
%{pylibdir}/wsgiref.egg-info


%dir %{site_packages}
%{site_packages32}/README
%{pylibdir}/*.py*
%{pylibdir}/*.doc
%dir %{pylibdir}/bsddb
%{pylibdir}/bsddb/*.py*
%{pylibdir}/compiler
%dir %{pylibdir}/ctypes
%{pylibdir}/ctypes/*.py*
%{pylibdir}/ctypes/macholib
%{pylibdir}/curses
%dir %{pylibdir}/distutils
%{pylibdir}/distutils/*.py*
%{pylibdir}/distutils/README
%{pylibdir}/distutils/command
%dir %{pylibdir}/email
%{pylibdir}/email/*.py*
%{pylibdir}/email/mime
%{pylibdir}/encodings
%{pylibdir}/hotshot
%{pylibdir}/idlelib
%dir %{pylibdir}/json
%{pylibdir}/json/*.py*
%{pylibdir}/lib2to3
%exclude %{pylibdir}/lib2to3/tests
%{pylibdir}/logging
%{pylibdir}/multiprocessing
%{pylibdir}/plat-linux2
%dir %{pylibdir}/sqlite3
%{pylibdir}/sqlite3/*.py*
%dir %{pylibdir}/test
%{pylibdir}/test/test_support.py*
%{pylibdir}/test/__init__.py*
%{pylibdir}/wsgiref
%{pylibdir}/xml
%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}/site-packages
%endif
# "Makefile" and the config-32/64.h file are needed by
# distutils/sysconfig.py:_init_posix(), so we include them in the core
# package, along with their parent directories (bug 531901):
%dir %{pylibdir}/config
%{pylibdir}/config/Makefile
%dir %{_includedir}/python%{pybasever}
%{_includedir}/python%{pybasever}/%{_pyconfig_h}

%if 0%{?with_systemtap}
%{tapsetdir}/%{libpython_stp}
%doc systemtap-example.stp pyfuntop.stp
%endif

%files libs
%defattr(-,root,root, -)
%doc LICENSE README
%{_libdir}/%{py_INSTSONAME}

%files devel
%defattr(-,root,root, -)
%{pylibdir}/config/*
%exclude %{pylibdir}/config/Makefile
%{_includedir}/python%{pybasever}/*.h
%exclude %{_includedir}/python%{pybasever}/%{_pyconfig_h}
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%if %{main_python}
%{_bindir}/python-config
%else
%exclude %{_bindir}/python-config
%endif
%{_bindir}/python%{pybasever}-config
%{_libdir}/libpython%{pybasever}.so

%files tools
%defattr(-,root,root,755)
# %doc Tools/modulator/README.modulator
%doc Tools/pynche/README.pynche
# %{site_packages}/modulator
%{site_packages}/pynche
%if %{main_python}
%{_bindir}/smtpd*.py*
%{_bindir}/2to3*
%{_bindir}/idle*
# %{_bindir}/modulator*
%{_bindir}/pynche*
%{_bindir}/pygettext*.py*
%{_bindir}/msgfmt*.py*
%else
%exclude %{_bindir}/smtpd*.py*
%exclude %{_bindir}/2to3*
%exclude %{_bindir}/idle*
#%exclude %{_bindir}/modulator*
%exclude %{_bindir}/pynche*
%exclude %{_bindir}/pygettext*.py*
%exclude %{_bindir}/msgfmt*.py*
%endif

%{tools_dir}
%{demo_dir}
%{pylibdir}/Doc

%files -n %{tkinter}
%defattr(-,root,root,755)
%{pylibdir}/lib-tk
%{dynload_dir}/_tkinter.so

%files test
%defattr(-, root, root, -)
%{pylibdir}/bsddb/test
%{pylibdir}/ctypes/test
%{pylibdir}/distutils/tests
%{pylibdir}/email/test
%{pylibdir}/json/tests
%{pylibdir}/lib2to3/tests
%{pylibdir}/sqlite3/test
%{pylibdir}/test
%{dynload_dir}/_ctypes_test.so
#%{dynload_dir}/_testcapimodule.so

# We put the debug-gdb.py file inside /usr/lib/debug to avoid noise from
# ldconfig (rhbz:562980).
# 
# The /usr/lib/rpm/redhat/macros defines %__debug_package to use
# debugfiles.list, and it appears that everything below /usr/lib/debug and
# (/usr/src/debug) gets added to this file (via LISTFILES) in
# /usr/lib/rpm/find-debuginfo.sh
# 
# Hence by installing it below /usr/lib/debug we ensure it is added to the
# -debuginfo subpackage
# (if it doesn't, then the rpmbuild ought to fail since the debug-gdb.py 
# payload file would be unpackaged)

# ALAN - I don't understand this stuff above, and there are unpackaged files under 
# /usr/lib/debug so I'm going to ignore them...
%exclude /usr/lib/debug/*


