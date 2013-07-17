#TODO: g2clib and grib (said to be modified)
#TODO: Python 3 modules should be possible since 1.7
#TODO: Create script to make clean tarball
#TODO: msg needs to have PublicDecompWT.zip from EUMETSAT, which is not free;
#      Building without msg therefore
#TODO: e00compr bundled?
#TODO: There are tests for bindings -- at least for Perl
#TODO: Java has a directory with test data and a build target called test
#      It uses %{JAVA_RUN}; make test seems to work in the build directory
#TODO: e00compr source is the same in the package and bundled in GDAL
#TODO: Consider doxy patch from Suse, setting EXTRACT_LOCAL_CLASSES  = NO

# Soname should be bumped on API/ABI break
# http://trac.osgeo.org/gdal/ticket/4543

# Conditionals and structures for EL 5 are there
# to make life easier for downstream ELGIS.
# Sadly noarch doesn't work in EL 5, see
# http://fedoraproject.org/wiki/EPEL/GuidelinesAndPolicies

#TODO: EvenR suggested to drop Ruby bindings, as they are unmaintained
# He also suggest to use --with-static-proj4 to actually link to proj, instead of dlopen()ing it.


# Tests can be of a different version
%global testversion 1.9.0

# https://bugzilla.redhat.com/show_bug.cgi?id=663938
%ifnarch ppc ppc64
%global spatialite "--with-spatialite"
%endif

%global my_python /usr/bin/python2.7

Name:      gdal
Version:   1.9.2
Release:   1.ceda%{?dist}
Summary:   GIS file format library
Group:     System Environment/Libraries
License:   MIT
URL:       http://www.gdal.org
# Source0:   http://download.osgeo.org/gdal/gdal-%%{version}.tar.gz
# See PROVENANCE.TXT-fedora and the cleaner script for details!

Source0:   %{name}-%{version}-fedora.tar.gz
Source1:   http://download.osgeo.org/%{name}/%{name}autotest-%{testversion}.tar.gz
Source2:   %{name}.pom

# Cleaner script for the tarball
Source3:   %{name}-cleaner.sh

Source4:   PROVENANCE.TXT-fedora

# Patch to use system g2clib
Patch1:    %{name}-g2clib.patch

Patch4:    %{name}-1.9.1-dods-3.11.3.patch

# Fedora uses Alternatives for Java
Patch8:    %{name}-1.9.0-java.patch

# Make man a phony buildtarget; the directory otherwise blocks it
# Should be solved in 2.0
Patch9:    %{name}-1.9.0-man.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ant
# No armadillo in EL5
BuildRequires: armadillo-devel
BuildRequires: cfitsio-devel
# No CharLS in EL5
BuildRequires: CharLS-devel
BuildRequires: chrpath
BuildRequires: curl-devel
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
# No freexl in EL5
BuildRequires: freexl-devel
BuildRequires: g2clib-static
BuildRequires: geos-devel
BuildRequires: ghostscript
BuildRequires: hdf-devel >= 4.2.9-1.ceda
BuildRequires: hdf-static
BuildRequires: hdf5-devel
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jasper-devel
BuildRequires: jpackage-utils
BuildRequires: libgcj
BuildRequires: libgeotiff-devel
# No libgta in EL5
BuildRequires: libgta-devel

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel

%ifnarch ppc ppc64
BuildRequires: libspatialite-devel
%endif

BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: libtool
BuildRequires: giflib-devel
BuildRequires: netcdf-devel
BuildRequires: libdap-devel
BuildRequires: librx-devel
BuildRequires: mysql-devel
#BuildRequires: numpy
BuildRequires: python27-numpy
#BuildRequires: ogdi-devel
#BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: pkgconfig
BuildRequires: poppler-devel
BuildRequires: postgresql-devel
BuildRequires: proj-devel
#BuildRequires: python-devel
BuildRequires: python27
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: tetex-latex
BuildRequires: unixODBC-devel
BuildRequires: xerces-c-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel

# Run time dependency for gpsbabel driver
Requires: gpsbabel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# Enable/disable generating refmans
%global build_refman 1

# We have multilib triage
%if "%{_lib}" == "lib"
  %global cpuarch 32
%else
  %global cpuarch 64
%endif

# made these defines unconditional - may not work on all distros - for use with RHEL6 - Alan Iwi
%global python_sitelib %(%{my_python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python_sitearch %(%{my_python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

%if (0%{?fedora} < 17 || 0%{?rhel})
# https://fedoraproject.org/wiki/PackagingDrafts/Ruby
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}
%endif

#TODO: Description on the lib?
%description
Geospatial Data Abstraction Library (GDAL/OGR) is a cross platform
C++ translator library for raster and vector geospatial data formats.
As a library, it presents a single abstract data model to the calling
application for all supported formats. It also comes with a variety of
useful commandline utilities for data translation and processing.

It provides the primary data access engine for many applications.
GDAL/OGR is the most widely used geospatial data access library.


%package devel
Summary: Development files for the GDAL file format library
Group: Development/Libraries

# Old rpm didn't figure out
%if 0%{?rhel} < 6
Requires: pkgconfig
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-static < 1.9.0-1

%description devel
This package contains development files for GDAL.


%package libs
Summary: GDAL file format library
Group: System Environment/Libraries

%description libs
This package contains the GDAL file format library.


%package ruby
Summary: Ruby modules for the GDAL file format library
Group: Development/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%if (0%{?fedora} < 17 || 0%{?rhel})
Requires: ruby(abi) = 1.8
%else
%if 0%{?fedora} < 19
Requires: ruby(abi) = 1.9.1
%else
Requires: ruby(release)
%endif
%endif

%description ruby
The GDAL Ruby modules provide support to handle multiple GIS file formats.


%package java
Summary: Java modules for the GDAL file format library
Group: Development/Libraries
Requires: java >= 1:1.6.0

# Require maven2 for the poms and depmap frag parent dirs
# Fedora 15 has Maven3 and the package is called maven
# Notice, maven2 is seemingly not a package in EL, but
# directories are provided by ant

# Commenting out this dependency given the above comment.
# This is for use on EL, and building maven is going to be non-trivial
# because of a lot of build-time dependencies. Unless commented out, 
# this is going to require either maven or maven2, but we don't want either.
# -- Alan Iwi

#%if (0%{?fedora})
#Requires: maven
#%else
#Requires: maven2
#%endif

Requires: jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description java
The GDAL Java modules provide support to handle multiple GIS file formats.


%package javadoc
Summary: Javadocs for %{name}
Group: Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package perl
Summary: Perl modules for the GDAL file format library
Group:   Development/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description perl
The GDAL Perl modules provide support to handle multiple GIS file formats.


%package python27
Summary: Python 2.7 modules for the GDAL file format library
Group:   Development/Libraries
Requires: python27-numpy
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description python27
The GDAL Python 2.7 modules provide support to handle multiple GIS file formats.
The package also includes a couple of useful utilities in Python 2.7.


%package doc
Summary: Documentation for GDAL
Group:   Documentation
BuildArch: noarch

%description doc
This package contains HTML and PDF documentation for GDAL.

# We don't want to provide private Python extension libs
%global __provides_exclude_from ^%{python_sitearch}/.*\.so$

%prep
export PYTHON=%{my_python}
%setup -q -n %{name}-%{version}-fedora

# Unpack tests to the same directory
%setup -q -D -a 1 -n %{name}-%{version}-fedora

# Delete bundled libraries
rm -rf frmts/zlib
rm -rf frmts/png/libpng
rm -rf frmts/gif/giflib
rm -rf frmts/jpeg/libjpeg \
    frmts/jpeg/libjpeg12
rm -rf frmts/gtiff/libgeotiff \
    frmts/gtiff/libtiff
rm -r frmts/grib/degrib18/g2clib-1.0.4

%patch1 -p1 -b .g2clib~
%patch4 -p1 -b .dods~
%patch8 -p1 -b .java~
%patch9 -p1 -b .man~

# Copy in PROVENANCE.TXT-fedora
cp %SOURCE4 .

# Sanitize linebreaks and encoding
#TODO: Don't touch data directory!
# /frmts/grib/degrib18/degrib/metaname.cpp
# and geoconcept.c are potentially dangerous to change
set +x
for f in `find . -type f` ; do
  if file $f | grep -q ISO-8859 ; then
    set -x
    iconv -f ISO-8859-1 -t UTF-8 $f > ${f}.tmp && \
      mv -f ${f}.tmp $f
    set +x
  fi
  if file $f | grep -q CRLF ; then
    set -x
    sed -i -e 's|\r||g' $f
    set +x
  fi
done
set -x

# Solved for 2.0
for f in ogr/ogrsf_frmts/gpsbabel ogr/ogrsf_frmts/pgdump port apps; do
pushd $f
  chmod 644 *.cpp *.h
popd
done

# Workaround about wrong result in configure
# armadillo returns a warning about gcc versions 4.7.0 or 4.7.1
# due to http://gcc.gnu.org/bugzilla/show_bug.cgi?id=53549
# configure interprets the result as an error so ignore it
# this patch can/should be removed after gcc 4.7.2 is released
sed -i 's|if test -z "`${CXX} testarmadillo.cpp -o testarmadillo -larmadillo 2>&1`"|if true|' configure

# Build with fPIC to allow Ruby bindings
# Xcompiler should normally achieve that -- http://trac.osgeo.org/gdal/ticket/3978
# http://trac.osgeo.org/gdal/ticket/1994
sed -i 's|\$(CFLAGS)|$(CFLAGS) -fPIC|g' swig/ruby/RubyMakefile.mk

%if !(0%{?fedora} < 17 || 0%{?rhel})
# Install Ruby bindings to distribution specific directory
sed -i 's|RUBY_EXTENSIONS_DIR :=.*|RUBY_EXTENSIONS_DIR := %{ruby_vendorarchdir}|' swig/ruby/RubyMakefile.mk
%endif

# Install Ruby bindings into the proper place
#TODO: Ticket
sed -i -e 's|^$(INSTALL_DIR):|$(DESTDIR)$(INSTALL_DIR):|' swig/ruby/RubyMakefile.mk
sed -i -e 's|^install: $(INSTALL_DIR)|install: $(DESTDIR)$(INSTALL_DIR)|' swig/ruby/RubyMakefile.mk

# Replace hard-coded library- and include paths
sed -i 's|@LIBTOOL@|%{_bindir}/libtool|g' GDALmake.opt.in
sed -i 's|-L\$with_cfitsio -L\$with_cfitsio/lib -lcfitsio|-lcfitsio|g' configure
sed -i 's|-I\$with_cfitsio -I\$with_cfitsio/include|-I\$with_cfitsio/include/cfitsio|g' configure
sed -i 's|-L\$with_netcdf -L\$with_netcdf/lib -lnetcdf|-lnetcdf|g' configure
sed -i 's|-L\$DODS_LIB -ldap++|-ldap++|g' configure
sed -i 's|-L\$with_ogdi -L\$with_ogdi/lib -logdi|-logdi|g' configure
sed -i 's|-L\$with_jpeg -L\$with_jpeg/lib -ljpeg|-ljpeg|g' configure
sed -i 's|-L\$with_libtiff\/lib -ltiff|-ltiff|g' configure
sed -i 's|-lgeotiff -L$with_geotiff $LIBS|-lgeotiff $LIBS|g' configure
sed -i 's|-L\$with_geotiff\/lib -lgeotiff $LIBS|-lgeotiff $LIBS|g' configure

# libproj is dlopened; upstream sources point to .so, which is usually not present
# http://trac.osgeo.org/gdal/ticket/3602
sed -i 's|libproj.so|libproj.so.0|g' ogr/ogrct.cpp

# Fix Python installation path
sed -i 's|setup.py install|setup.py install --root=%{buildroot}|' swig/python/GNUmakefile

# Must be corrected for 64 bit architectures other than Intel
# http://trac.osgeo.org/gdal/ticket/4544
# Should be gone in 2.0
sed -i 's|test \"$ARCH\" = \"x86_64\"|test \"$libdir\" = \"/usr/lib64\"|g' configure

# Adjust check for LibDAP version
# http://trac.osgeo.org/gdal/ticket/4545
%if %cpuarch == 64
  sed -i 's|with_dods_root/lib|with_dods_root/lib64|' configure
%endif

# Activate support for JPEGLS
sed -i 's|^#HAVE_CHARLS|HAVE_CHARLS|' GDALmake.opt.in
sed -i 's|#CHARLS_INC = -I/path/to/charls_include|CHARLS_INC = -I%{_includedir}/CharLS|' GDALmake.opt.in
sed -i 's|#CHARLS_LIB = -L/path/to/charls_lib -lCharLS|CHARLS_LIB = -lCharLS|' GDALmake.opt.in

# Replace default plug-in dir
# Solved in 2.0
# http://trac.osgeo.org/gdal/ticket/4444
%if %cpuarch == 64
  sed -i 's|GDAL_PREFIX "/lib/gdalplugins"|GDAL_PREFIX "/lib64/gdalplugins"|' \
    gcore/gdaldrivermanager.cpp \
    ogr/ogrsf_frmts/generic/ogrsfdriverregistrar.cpp
%endif

# Remove man dir, as it blocks a build target.
# It obviously slipped into the tarball and is not in Trunk (April 17th, 2011)
#rm -rf man


%build
export PYTHON=%{my_python}
#TODO: Couldn't I have modified that in the prep section?
%ifarch sparcv9 sparc64 s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export CXXFLAGS="$CFLAGS -I%{_includedir}/libgeotiff"
export CPPFLAGS="$CPPFLAGS -I%{_includedir}/libgeotiff"

# For future reference:
# epsilon: Stalled review -- https://bugzilla.redhat.com/show_bug.cgi?id=660024
# openjpeg 2.0 necessary, 1.4 is in Fedora
# Building without pgeo driver, because it drags in Java

%configure \
        LIBS=-lgrib2c \
        --with-autoload=%{_libdir}/%{name}plugins \
        --datadir=%{_datadir}/%{name}/ \
        --includedir=%{_includedir}/%{name}/ \
        --prefix=%{_prefix} \
        --without-bsb \
        --with-armadillo          \
        --with-curl               \
        --with-cfitsio=%{_prefix} \
        --with-dods-root=%{_prefix} \
        --with-expat              \
        --with-freexl             \
        --with-geos               \
        --with-geotiff=external   \
        --with-gif                \
        --with-gta                \
        --with-hdf4               \
        --with-hdf5               \
        --with-jasper             \
        --with-java               \
        --with-jpeg               \
        --without-jpeg12          \
        --with-liblzma            \
        --with-libtiff=external   \
        --with-libz               \
        --without-mdb             \
        --with-mysql              \
        --with-netcdf             \
        --with-odbc               \
        --without-ogdi               \
        --without-msg             \
        --without-openjpeg        \
        --with-pcraster           \
        --with-pg                 \
        --with-png                \
        --with-poppler            \
        %{spatialite}             \
        --with-sqlite3            \
        --with-threads            \
        --with-webp               \
        --with-xerces             \
        --enable-shared           \
        --with-ruby               \
        --with-perl               \
        --with-python

        #--with-rasdaman           # 8.3 rasdaman has no -lcompression; doesn't work

# {?_smp_mflags} doesn't work; Or it does -- who knows!
make %{?_smp_mflags}
make man
make docs

# Make Perl modules
pushd swig/perl
  perl Makefile.PL;  make;
  echo > Makefile.PL;
popd

# Install the Perl modules in the right place
sed -i 's|INSTALLDIRS = site|INSTALLDIRS = vendor|' swig/perl/Makefile_*

# Don't append installation info to pod
#TODO: What about the pod?
sed -i 's|>> $(DESTINSTALLARCHLIB)\/perllocal.pod|> \/dev\/null|g' swig/perl/Makefile_*

# Make Java module and documentation
pushd swig/java
  make
  ./make_doc.sh
popd

# --------- Documentation ----------

# No useful documentation in swig
%global docdirs apps doc doc/br doc/ru ogr ogr/ogrsf_frmts frmts/gxf frmts/iso8211 frmts/pcidsk frmts/sdts frmts/vrt ogr/ogrsf_frmts/dgn/
for docdir in %{docdirs}; do
  # CreateHTML and PDF documentation, if specified
  pushd $docdir
    if [ ! -f Doxyfile ]; then
      doxygen -g
    else
      doxygen -u
    fi
    sed -i -e 's|^GENERATE_LATEX|GENERATE_LATEX = YES\n#GENERATE_LATEX |' Doxyfile
    sed -i -e 's|^USE_PDFLATEX|USE_PDFLATEX = YES\n#USE_PDFLATEX |' Doxyfile

    if [ $docdir == "doc/ru" ]; then
      sed -i -e 's|^OUTPUT_LANGUAGE|OUTPUT_LANGUAGE = Russian\n#OUTPUT_LANGUAGE |' Doxyfile
    fi
    rm -rf latex html
    doxygen

    %if %{build_refman}
      pushd latex
        sed -i -e '/rfoot\[/d' -e '/lfoot\[/d' doxygen.sty
        sed -i -e '/small/d' -e '/large/d' refman.tex
        sed -i -e 's|pdflatex|pdflatex -interaction nonstopmode |g' Makefile
        make refman.pdf || true
      popd
    %endif
  popd
done


%install
rm -rf %{buildroot}

make    DESTDIR=%{buildroot} \
        install \
        install-man

# Directory for auto-loading plugins
mkdir -p %{buildroot}%{_libdir}/%{name}plugins

#TODO: Don't do that?
find %{buildroot}%{perl_vendorarch} -name "*.dox" -exec rm -rf '{}' \;

# Correct permissions
#TODO and potential ticket: Why are the permissions not correct?
find %{buildroot}%{perl_vendorarch} -name "*.so" -exec chmod 755 '{}' \;
find %{buildroot}%{perl_vendorarch} -name "*.pm" -exec chmod 644 '{}' \;

#TODO: JAR files that require JNI shared objects MUST be installed in %{_libdir}/%{name}. The JNI shared objects themselves must also be installed in %{_libdir}/%{name}.
#Java programs that wish to make calls into native libraries do so via the Java Native Interface (JNI). A Java package uses JNI if it contains a .so
#If the JNI-using code calls System.loadLibrary you'll have to patch it to use System.load, passing it the full path to the dynamic shared object. If the package installs a wrapper script you'll need to manually add %{_libdir}/%{name}/<jar filename> to CLASSPATH. If you are depending on a JNI-using JAR file, you'll need to add it manually -- build-classpath will not find it.
touch -r NEWS swig/java/gdal.jar
mkdir -p %{buildroot}%{_javadir}
cp -p swig/java/gdal.jar  \
    %{buildroot}%{_javadir}/%{name}.jar

# Install Maven pom and update version number
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's|<version></version>|<version>%{version}</version>|' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Create depmap fragment
%add_to_maven_depmap org.gdal gdal-java-bindings %{version} JPP %{name}

# 775 on the .so?
# copy JNI libraries and links, non versioned link needed by JNI
# What is linked here?
cp -pl swig/java/.libs/*.so*  \
    %{buildroot}%{_libdir}
chrpath --delete %{buildroot}%{_libdir}/*jni.so*

# Install Java API documentation in the designated place
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr swig/java/java/org %{buildroot}%{_javadocdir}/%{name}

# Install refmans
for docdir in %{docdirs}; do
  pushd $docdir
    path=%{_builddir}/%{name}-%{version}-fedora/refman
    mkdir -p $path/html/$docdir
    cp -r html $path/html/$docdir

    # Install all Refmans
    %if %{build_refman}
        if [ -f latex/refman.pdf ]; then
          mkdir -p $path/pdf/$docdir
          cp latex/refman.pdf $path/pdf/$docdir
        fi
    %endif
  popd
done

# Install formats documentation
for dir in gdal_frmts ogrsf_frmts; do
  mkdir -p $dir
  find frmts -name "*.html" -exec install -p -m 644 '{}' $dir \;
done

#TODO: Header date lost during installation
# Install multilib cpl_config.h bz#430894
install -p -D -m 644 port/cpl_config.h %{buildroot}%{_includedir}/%{name}/cpl_config-%{cpuarch}.h
# Create universal multilib cpl_config.h bz#341231
# The problem is still there in 1.9.
#TODO: Ticket?

#>>>>>>>>>>>>>
cat > %{buildroot}%{_includedir}/%{name}/cpl_config.h <<EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "gdal/cpl_config-32.h"
#else
#if __WORDSIZE == 64
#include "gdal/cpl_config-64.h"
#else
#error "Unknown word size"
#endif
#endif
EOF
#<<<<<<<<<<<<<
touch -r NEWS port/cpl_config.h

# Create and install pkgconfig file
#TODO: Why does that exist? Does Grass really use it? I don't think so.
# http://trac.osgeo.org/gdal/ticket/3470
#>>>>>>>>>>>>>
cat > %{name}.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: GDAL
Description: GIS file format library
Version: %{version}
Libs: -L\${libdir} -lgdal
Cflags: -I\${includedir}/%{name}
EOF
#<<<<<<<<<<<<<
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
install -m 644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/
touch -r NEWS %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# Multilib gdal-config
# Rename the original script to gdal-config-$arch (stores arch-specific information)
# and create a script to call one or the other -- depending on detected architecture
# TODO: The extra script will direct you to 64 bit libs on
# 64 bit systems -- whether you like that or not
mv %{buildroot}%{_bindir}/%{name}-config %{buildroot}%{_bindir}/%{name}-config-%{cpuarch}
#>>>>>>>>>>>>>
cat > %{buildroot}%{_bindir}/%{name}-config <<EOF
#!/bin/bash

ARCH=\$(uname -m)
case \$ARCH in
x86_64 | ppc64 | ia64 | s390x | sparc64 | alpha | alphaev6 )
%{name}-config-64 \${*}
;;
*)
%{name}-config-32 \${*}
;;
esac
EOF
#<<<<<<<<<<<<<
touch -r NEWS %{buildroot}%{_bindir}/%{name}-config
chmod 755 %{buildroot}%{_bindir}/%{name}-config

# Clean up junk
rm -f %{buildroot}%{_bindir}/gdal_sieve.dox
rm -f %{buildroot}%{_bindir}/gdal_fillnodata.dox

#jni-libs and libgdal are also built static (*.a)
#.exists and .packlist stem from Perl
for junk in {*.a,*.la,*.bs,.exists,.packlist} ; do
  find %{buildroot} -name "$junk" -exec rm -rf '{}' \;
done

# Don't duplicate license files
rm -f %{buildroot}%{_datadir}/%{name}/LICENSE.TXT

# Throw away random API man mages plus artefact seemingly caused by Doxygen 1.8.1 or 1.8.1.1
for f in 'GDAL*' BandProperty ColorAssociation CutlineTransformer DatasetProperty EnhanceCBInfo ListFieldDesc NamedColor OGRSplitListFieldLayer VRTBuilder _builddir_build_BUILD_%{name}-%{version}-fedora_apps_; do
  rm -rf %{buildroot}%{_mandir}/man1/$f.1*
done

%check
#for i in -I/usr/lib/jvm/java/include{,/linux}; do
#    java_inc="$java_inc $i"
#done


pushd %{name}autotest-%{testversion}
  # Export test enviroment
  export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python_sitearch}
  #TODO: Nötig?
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
#  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}:$java_inc

  export GDAL_DATA=%{buildroot}%{_datadir}/%{name}/

  # Enable these tests on demand
  #export GDAL_RUN_SLOW_TESTS=1
  #export GDAL_DOWNLOAD_TEST_DATA=1

  # Remove some test cases that would require special preparation
  rm -rf ogr/ogr_pg.py        # No database available
  rm -rf ogr/ogr_mysql.py     # No database available
  rm -rf osr/osr_esri.py      # ESRI datum absent
  rm -rf osr/osr_erm.py       # File from ECW absent

  # Run tests but force normal exit in the end
  ./run_all.py || true
popd


%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post java
/sbin/ldconfig
%update_maven_depmap

%postun java
/sbin/ldconfig
%update_maven_depmap


%files
%{_bindir}/gdallocationinfo
%{_bindir}/gdal_contour
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdaladdo
%{_bindir}/gdalinfo
%{_bindir}/gdaldem
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaltindex
%{_bindir}/gdalwarp
%{_bindir}/gdal_grid
%{_bindir}/gdalenhance
%{_bindir}/gdalmanage
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltransform
%{_bindir}/nearblack
%{_bindir}/ogr*
%{_bindir}/testepsg
%{_mandir}/man1/gdal*.1*
%exclude %{_mandir}/man1/gdal-config.1*
%exclude %{_mandir}/man1/gdal2tiles.1*
%exclude %{_mandir}/man1/gdal_fillnodata.1*
%exclude %{_mandir}/man1/gdal_merge.1*
%exclude %{_mandir}/man1/gdal_retile.1*
%exclude %{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr*.1*

%files libs
%doc LICENSE.TXT NEWS PROVENANCE.TXT COMMITERS PROVENANCE.TXT-fedora
%{_libdir}/libgdal.so.*
%{_datadir}/%{name}
#TODO: Possibly remove files like .dxf, .dgn, ...
%dir %{_libdir}/%{name}plugins

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-config-%{cpuarch}
%{_mandir}/man1/gdal-config.1*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files ruby
%if (0%{?fedora} < 17 || 0%{?rhel})
%{ruby_sitearch}/%{name}
%else
%{ruby_vendorarchdir}/%{name}
%endif

# Can I even have a separate Java package anymore?
%files java
%doc swig/java/apps
%{_javadir}/%{name}.jar
%{_libdir}/*jni.so.*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%files perl
%doc swig/perl/README
%{perl_vendorarch}/*

%files python27
%doc swig/python/README.txt
%doc swig/python/samples
#TODO: Bug with .py files in EPEL 5 bindir, see http://fedoraproject.org/wiki/EPEL/GuidelinesAndPolicies
%{_bindir}/*.py
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%{python_sitearch}/osgeo
%{python_sitearch}/GDAL-%{version}-py*.egg-info
%{python_sitearch}/osr.py*
%{python_sitearch}/ogr.py*
%{python_sitearch}/gdal*.py*

%files doc
%doc gdal_frmts ogrsf_frmts refman

#TODO: jvm
#Should be managed by the Alternatives system and not via ldconfig
#The MDB driver is said to require:
#Download jackcess-1.2.2.jar, commons-lang-2.4.jar and
#commons-logging-1.1.1.jar (other versions might work)
#If you didn't specify --with-jvm-lib-add-rpath at
#Or as before, using ldconfig

%changelog
* Fri Apr 26 2013  Alan Iwi - 1.9.2-1.ceda
- require patched hdf and use python 2.7
- remove maven dependency

* Tue Mar 26 2013 Volker Fröhlich <volker27@gmx.at> - 1.9.2-4
- Rebuild for cfitsio 3.340

* Sun Mar 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.2-3
- rebuild (libcfitsio)

* Wed Mar 13 2013 Vít Ondruch <vondruch@redhat.com> - 1.9.2-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sun Mar 10 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.2-1
- Update to 1.9.2
- Drop poppler and java-swig patches applied upstream

* Fri Jan 25 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.9.1-18
- Rebuild with geos 3.3.7.

* Mon Jan 21 2013 Volker Fröhlich <volker27@gmx.at> - 1.9.1-17
- Rebuild due to libpoppler 0.22

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.9.1-16
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 28 2012 Richard W.M. Jones <rjones@redhat.com> - 1.9.1-15
- Rebuild, see
  http://lists.fedoraproject.org/pipermail/devel/2012-December/175685.html

* Thu Dec 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.1-14
- Tweak -fpic CFLAGS to fix FTBFS on ARM

* Mon Dec  3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.1-13
- Rebuild for hdf5 1.8.10

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> - 1.9.1-12
- Rebuild for libspatialite soname bump

* Thu Aug  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-11
- Correct and extend conditionals for ppc andd ppc64, considering libspatialite
  Related to BZ #846301

* Sun Jul 29 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-10
- Use the correct shell idiom "if true" instead of "if 1"

* Sun Jul 29 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-9
- Ignore for the moment the test for armadillo (to be removed after gcc 4.7.2 release)

* Fri Jul 27 2012 José Matos <jamatos@fedoraproject.org> - 1.9.1-8
- Rebuild for new armadillo

* Fri Jul 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.1-7
- Build with PIC

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.9.1-5
- Perl 5.16 rebuild

* Sat Jul  7 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-4
- Delete unnecessary manpage, that seems to be created with
  new Doxygen (1.8.1 or 1.8.1.1)

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 1.9.1-3
- Rebuild (poppler-0.20.1)

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.9.1-2
- Perl 5.16 rebuild

* Wed May 23 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.1-1
- New upstream release
- Update poppler patch
- Add cleaner script

* Sun May 20 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-5
- Patches for libpoppler 0.20, libdap 3.11.3 and swig 2.0.6

* Thu May 10 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-4
- Correct provides-filtering as of https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Usage
- Support webp
- Remove bogus libjpeg-turbo conditional
- Update Ruby ABI version to 1.9.1
- Install Ruby bindings to vendorarchdir on F17 and later
- Conditionals for Ruby specific elements for versions prior F17 and for EPEL
- Correct quotes for CFLAGS and Ruby
- Disable ogdi, until BZ#816282 is resolved

* Wed Apr 25 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-2
- Rebuild for cfitsio 3.300

* Sun Feb 26 2012 Volker Fröhlich <volker27@gmx.at> - 1.9.0-1
- Completely re-work the original spec-file
  The major changes are:
- Add a libs sub-package
- Move Python scripts to python sub-package
- Install the documentation in a better way and with less slack
- jar's filename is versionless
- Update the version in the Maven pom automatically
- Add a plugins directory
- Add javadoc package and make the man sub-package noarch
- Support many additional formats
- Drop static sub-package as no other package uses it as BR
- Delete included libs before building
- Drop all patches, switch to a patch for the manpages, patch for JAVA path
- Harmonize the use of buildroot and RPM_BUILD_ROOT
- Introduce testversion macro

* Thu Feb 19 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-14
- Require Ruby abi
- Add patch for Ruby 1.9 include dir, back-ported from GDAL 1.9
- Change version string for gdal-config from <version>-fedora to
  <version>
- Revert installation path for Ruby modules, as it proofed wrong
- Use libjpeg-turbo

* Thu Feb  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-13
- Rebuild for Ruby 1.9
  http://lists.fedoraproject.org/pipermail/ruby-sig/2012-January/000805.html

* Tue Jan 10 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.3-12
- Remove FC10 specific patch0
- Versioned MODULE_COMPAT_ Requires for Perl (BZ 768265)
- Add isa macro to base package Requires
- Remove conditional for xerces_c in EL6, as EL6 has xerces_c
  even for ppc64 via EPEL
- Remove EL4 conditionals
- Replace the python_lib macro definition and install Python bindings
  to sitearch directory, where they belong
- Use correct dap library names for linking
- Correct Ruby installation path in the Makefile instead of moving it later
- Use libdir variable in ppc64 Python path
- Delete obsolete chmod for Python libraries
- Move correction for Doxygen footer to prep section
- Delete bundled libraries before building
- Build without bsb and remove it from the tarball
- Use mavenpomdir macro and be a bit more precise on manpages in
  the files section
- Remove elements for grass support --> Will be replaced by plug-in
- Remove unnecessary defattr
- Correct version number in POM
- Allow for libpng 1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.3-11
- Rebuild for new libpng

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-10
- Rebuild for hdf5 1.8.7

* Fri Apr 22 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-9
- Patched spaces problem for Mapinfo files (mif)
  (http://trac.osgeo.org/gdal/ticket/3694)
- Replaced all define macros with global
- Corrected ruby_sitelib to ruby_sitearch
- Use python_lib and ruby_sitearch instead of generating lists
- Added man-pages for binaries
- Replaced mkdir and install macros
- Removed Python files from main package files section, that
  effectively already belonged to the Python sub-package

* Thu Apr 11 2011 Volker Fröhlich <volker27@gmx.at> - 1.7.3-8
- Solved image path problem with Latex
- Removed with-tiff and updated with-sqlite to with-sqlite3
- Add more refman documents
- Adapted refman loop to actual directories
- Harmonized buildroot macro use

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-7
- Rebuild for netcdf 4.1.2

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.7.3-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Sun Mar 20 2011 Volker Fröhlich <volker27@gmx.at> 1.7.3-5
- Dropped unnecessary encoding conversion for Russian refman
- Install Russian refman
- Don't try to install refman for sdts and dgn, as they fail to compile
- Added -p to post and postun
- Remove private-shared-object-provides for Python and Perl
- Remove installdox scripts
- gcc 4.6 doesn't accept -Xcompiler

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.7.3-4
- Rebuilt with xerces-c 3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.7.3-2
- Install all the generated pdf documentation.
- Build documentation as a separate package.
- Spec cleanup

* Fri Nov 19 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.7.3-1
- Update to latest upstream version
- Added jnis
- Patches updated with proper version info
- Added suggestions from Ralph Apel <r.apel@r-apel.de>
        + Versionless symlink for gdal.jar
        + Maven2 pom
        + JPP-style depmap
        + Use -f XX.files for ruby and python

* Sun Oct 31 2010 Mathieu Baudier <mbaudier@argeo.org> - 1.7.2-5_2
- PCRaster support
- cURL support
- Disable building the reference manual (really too long...)

* Sat Oct 09 2010 Mathieu Baudier <mbaudier@argeo.org> - 1.7.2-5_1
- Add Java JNI libraries

* Sat Aug 14 2010 Mathieu Baudier <mbaudier@argeo.org> - 1.7.2-5_0
- Rebuild for EL GIS, based on work contributed by Nikolaos Hatzopoulos and Peter Hopfgartner
- Use vanilla sources

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 20 2010 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-4
- Rebuild with grass support

* Thu Jul 17 2010 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-3
- Add patch to change AISConnect() to Connect() for libdap 3.10
- build without grass for libdap soname bump

* Tue Jul 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.2-2
- reenable grass support

* Fri Jul 09 2010 Robert Scheck <robert@fedoraproject.org> - 1.7.2-1
- upgrade to 1.7.2 (#587707, huge thanks to Sven Lankes)

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 1.7.1-2
- fix bz#572617

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 1.7.1-1
- new stable branch
- re-enable java ColorTable
- gdal custom fedora version banner
- rebuild without grass
- gdal manual are gone (upstream fault)

* Fri Feb  5 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.6.2-5
- reenable grass support

* Fri Feb  5 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.6.2-4
- temporarily disable grass support for bootstrapping
- rebuild for new libxerces-c

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6.2-3
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 1.6.2-2
- re-enable grass support

* Tue Nov 17 2009 Orion Poplawski <orion@cora.nwra.com> - 1.6.2-1
- Update to 1.6.2
- Rebuild for netcdf 4.1.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-2
- rebuilt with new openssl

* Thu Jul 30 2009 Dan Horak <dan[at]danny.cz> - 1.6.1-1
- add patch for incompatibilities caused by libdap 3.9.x (thanks goes to arekm from PLD)
- update to 1.6.1
- don't install some refman.pdf, because they don't build
- don't fail on man pages with suffix other than .gz
- fix filelist for python subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-9
- Rebuild for libdap 3.9.3, bootstrap

* Mon Mar 23 2009 Jesse Keating <jkeating@redhat.com> - 1.6.0-8
- re-enable grass support

* Sun Mar 22 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.6.0-7
- Depend specifically on GCJ for Java (Alex Lancaster)
- Disable grass (Alex Lancaster)
- Create %%_bindir before copying files there

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Balint Cristian <cristian.balint@gmail.com> - 1.6.0-4
- rebuild with grass support
- fix email typo

* Thu Jan 29 2009 Balint Cristian <cristian.balint@gmail.com> - 1.6.0-3
- rebuild against mysql 5.1.30

* Thu Jan 29 2009 Balint Cristian <cristian.balint@gmail.com> - 1.6.0-2
- email change
- rebuild without grass

* Fri Dec 12 2008 Balint Cristian <rezso@rdsor.ro> - 1.6.0-1
- final stable release

* Sat Dec 06 2008 Balint Cristian <rezso@rdsor.ro> - 1.6.0-0.2.rc4
- enable grass

* Sat Dec 06 2008 Balint Cristian <rezso@rdsor.ro> - 1.6.0-0.1.rc4
- new branch
- disable grass
- fix ruby compile

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.3-2
- Rebuild for Python 2.6

* Fri Oct 24 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.3-1
- new stable
- ship static package too
- fix some doc generation
- libdap patch for fc10 only

* Tue Sep 30 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.2-4
- enable gdal_array for python subpackage
- require numpy

* Tue Sep  9 2008 Patrice Dumas <pertusus@free.fr> - 1.5.2-3
- patch for libdap > 0.8.0, from Rob Cermak

* Thu Jun 12 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.2-1
- a new bugfix upstream
- drop gcc43 patch
- more license cleaned

* Wed May 27 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-13
- fix pkgconfig too

* Wed May 27 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-12
- fix once more gdal-config

* Tue May 27 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-11
- fix multilib gdal-config, add wrapper around
- fix typos in cpl_config.h wrapper

* Tue May 27 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-10
- fix for multilib packaging bz#341231
- huge spec cleanup
- enable russian and brazil docs
- enable and triage more docs

* Sun May 25 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-9
- enable ruby and java packages
- fix spurious sed problem
- spec file cosmetics

* Thu May 23 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-8
- fix sincos on all arch

* Thu May 15 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-7
- fix x86_64 problem

* Wed Apr 16 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-6
- disable fortify source, it crash gdal for now.

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-5
- really eanble against grass63

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-4
- disable grass to bootstrap once again

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-3
- rebuild to really pick up grass63 in koji

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-2
- enable build against newer grass
- enable build of reference manuals

* Tue Mar 25 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.1-1
- new bugfix release from upstream
- drop large parts from gcc43 patch, some are upstream now
- fix building with perl-5.10 swig binding issue

* Wed Feb 29 2008 Orion Poplawski <orion@cora.nwra.com> - 1.5.0-4
- Rebuild for hdf5-1.8.0, use compatability API define

* Tue Feb 12 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.0-3
- install cpl_config.h manually for bz#430894
- fix gcc4.3 build

* Mon Jan 14 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.0-2
- fix perl dependency issue.

* Mon Jan 07 2008 Balint Cristian <rezso@rdsor.ro> - 1.5.0-1
- update to new 1.5.0 upstream stable
- dropped build patch since HFA/ILI/DGN mandatories are now present
- dropped swig patch, its upstream now
- enable HFA it holds Intergraph (TM) explicit public license
- enable DGN it holds Avenza Systems (TM) explicit public license
- enable ILI headers since now contain proper public license message
- keep and polish up rest of doubted license
- further fixed hdf not supporting netcdf for for bz#189337
- kill the annoying -Lexternal/lib for -lgeotiff
- fix configure to not export LDFLAGS anyomre, upstream
  should really switch to real GNU automagic stuff
- pymod samples and rfc docs now gone
- hardcode external libtool to be used, LIBTOOL env not propagating anymore
- use DESTDIR instead

* Thu Jan 03 2008 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1.4.2-7
- Re-enable grass support now that gdal has been bootstrapped

* Wed Jan 02 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.2-6
- Bootstrap 1st: disabling grass support
- Workaround for hdf not supporting netcdf (bug 189337 c8)
- Disabling documents creation for now.

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.2-5
- Rebuild for deps
- Disable grass to avoid circular deps

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.4.2-3
- Rebuild for selinux ppc32 issue.

* Wed Jul 24 2007 Balint Cristian <cbalint@redhat.com> 1.4.2-2
- disable one more HFA test, HFA is unaviable due to license

* Wed Jul 24 2007 Balint Cristian <cbalint@redhat.com> 1.4.2-1
- new upstream one
- catch some more docs
- fix ogr python module runtime
- include testcases and run tests
- enable geotiff external library we have new libgeotiff now
- EPSG geodetic database is licensed OK since v6.13 so re-enable
- enable it against grass by default, implement optional switches

* Tue Jun 05 2007 Balint Cristian <cbalint@redhat.com> 1.4.1-4
- re-build.

* Sat May 12 2007 Balint Cristian <cbalint@redhat.com> 1.4.1-3
- re-build against grass.

* Fri May 11 2007 Balint Cristian <cbalint@redhat.com> 1.4.1-2
- fix python lookup paths for ppc64.

* Wed May 09 2007 Balint Cristian <cbalint@redhat.com> 1.4.1-1
- new upstream release.
- disable temporary grass-devel requirement untill find a
  resonable solution for gdal-grass egg-chicken dep problem.

* Fri Apr 20 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-22
- and olso dont attempt pack missing docs.

* Fri Apr 20 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-21
- exclude some docs, doxygen segfault with those now upstream.

* Fri Apr 20 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-20
- rebuild against latest fedora upstream tree.

* Mon Apr 02 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-19
- own gdal includedir
- fix one more spurious lib path

* Wed Mar 21 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-18
- remove system lib path from gdal-config --libs, its implicit

* Tue Mar 20 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-17
- enable build against grass
- fix incorrect use of 32/64 library paths lookups

* Fri Mar 16 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-16
- fix gdal flag from pkgconfig file

* Thu Mar 15 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-15
- require pkgconfig
- generate pkgconfig from spec instead

* Thu Mar 15 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-14
- require perl(ExtUtils::MakeMaker) instead ?dist checking
- add pkgconfig file

* Wed Mar 14 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-13
- fix typo in specfile

* Wed Mar 14 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-12
- add missing dot from dist string in specfile

* Wed Mar 14 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-11
- fix fc6 fc5 builds

* Thu Mar 1 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-10
- fix mock build
- require perl-devel

* Tue Feb 27 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-9
- repack tarball for fedora, explain changes in PROVENANCE-fedora,
  license should be clean now according to PROVENANCE-* files
- require ogdi since is available now
- drop nogeotiff patch, in -fedora tarball geotiff is removed
- man page triage over subpackages
- exclude python byte compiled objects
- fix some source C file exec bits

* Sat Feb 24 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-8
- fix more things in spec
- include more docs

* Wed Feb 21 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-7
- libtool in requirement list for build

* Wed Feb 21 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-6
- use external libtool to avoid rpath usage
- include more docs

* Mon Feb 12 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-5
- use rm -rf for removal of dirs.
- fix require lists

* Mon Feb 12 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-4
- fix doxygen buildreq
- make sure r-path is fine.

* Sat Feb 10 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-3
- disable now ogdi (pending ogdi submission).

* Sat Feb 10 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-2
- more fixups for lib paths

* Fri Feb 09 2007 Balint Cristian <cbalint@redhat.com> 1.4.0-1
- first pack for fedora extras
- disable geotiff (untill license sorted out)
- enable all options aviable from extras
- pack perl and python modules
- kill r-path from libs
- pack all docs posible
