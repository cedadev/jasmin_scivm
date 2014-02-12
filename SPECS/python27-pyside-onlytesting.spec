%define pname pyside
Summary: Python bindings for 0MQ.
Name: python27-%{pname}
Version: 1.2.1
Release: 1.ceda%{?dist}
Source0: PySide-%{version}.tar.gz
Patch0: pyside-qt-phonon.patch
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: PySide Team <contact@pyside.org>
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Url: http://www.pyside.org
Requires: python27 >= 2.7.3-2.ceda qt
BuildRequires: python27 >= 2.7.3-2.ceda qt-devel dos2unix
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%define qmake_path /usr/lib64/qt4/bin/qmake
%define ld_so_conf_file /etc/ld.so.conf.d/python27-pyside.conf

%description

PySide is the Python Qt bindings project, providing access the
complete Qt 4.8 framework as well as to generator tools for rapidly
generating bindings for any C++ libraries.

The PySide project is developed in the open, with all facilities you'd
expect from any modern OSS project such as all code in a git
repository, an open Bugzilla for reporting bugs, and an open design
process.

%prep
%setup -n PySide-%{version}
%patch0 -p0
find . -type f \( -name '*.txt' -or -name '*.cmake' \) | xargs dos2unix

%build
#TMP #export QT_PHONON_INCLUDE_DIR=/usr/include/phonon
#TMP #env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build --qmake=%{qmake_path}

%install
rm -fr $RPM_BUILD_ROOT
#TMP #python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES1 --qmake=%{qmake_path}

mkdir -p $RPM_BUILD_ROOT  # TMP
cp -r /tmp/usr $RPM_BUILD_ROOT/usr  #TMP 
cp /tmp/INSTALLED_FILES ./INSTALLED_FILES1  #TMP 

# stuff for ld.so.conf - see also %post and %postun
build_conf_file=$RPM_BUILD_ROOT/%{ld_so_conf_file}
mkdir -p `dirname $build_conf_file`
echo /usr/lib/python2.7/site-packages/PySide > $build_conf_file

# .so files that are meant to be a symlinks are copies as regular files.
# ldconfig doesn't like it, so fix it.
for lib in $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages/PySide/*.so.%{version}
do
   link=${lib%.*}
   rm $link
   ln -s `basename $lib` $link
done

# Remove from the list a couple of installed files that don't really exist
# (the .py file uses python 3 metaclass syntax, so it cannot be byte-compiled
# using python 2.7, but somehow setup.py still adds their names to the list)
# Also remove dups.
egrep -v 'port_v3/proxy_base.py[co]' INSTALLED_FILES1 | sort -u > INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%postun
if test `whoami` == root; then
   echo "Running /sbin/ldconfig"
   /sbin/ldconfig
fi

%changelog

* Thu Oct 17 2013  <builderdev@builder.jc.rl.ac.uk> - 1.2.1-1.ceda
- initial version (including QT_PHONON_INCLUDE_DIR stuff; see patch and env var)

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{ld_so_conf_file}
