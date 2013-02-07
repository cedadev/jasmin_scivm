%define java_package java-1.6.0-openjdk
%define jardir /usr/lib/ncBrowse
%define script %{_bindir}/ncBrowse
%define tmp_install /tmp/ncBrowse

Name: ncBrowse
Version: 1.6.5
Release: 2.ceda%{?dist}
Source: install_rel1_6_5.bin
License: http://www.epic.noaa.gov/java/license.html
Group: Scientific support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: Donald Denbo <Donald.W.Denbo@noaa.gov>
Url: http://www.epic.noaa.gov/java/ncBrowse/
Summary: a graphical netCDF file browser
Requires: %{java_package}
BuildRequires: %{java_package}
BuildArch: noarch

%description

ncBrowse is a Java application that provides flexible, interactive graphical 
displays of data and attributes from a wide range of netCDF data file conventions.

This installation is for use with java package %{java_package}

%prep

%build
# find the directory called "bin" containing "java" in our java package
# (insist that there is exactly one)
java_exe=`rpm -ql %{java_package} | egrep '/bin/java$'`
[ `echo $java_exe | wc -w` -eq 1 ] || (echo "cannot determine java executable" ; exit 1)
java_bin_dir=`dirname $java_exe`

if [ -d %{tmp_install} ]
then
     cat <<EOF
====================================================================
Making an RPM based on files installed into %{tmp_install} by the
graphical installer, which hopefully you have just run?
====================================================================
EOF
else
     cat <<EOF
====================================================================
Outside the rpmbuild environment, please run the graphical installer
with:

   sh %{SOURCE0}

telling it,

   * to use java executable $java_exe
   * to install to target directory %{tmp_install}
   * not to create links

Then please rerun this rpmbuild to package up the resultant 
installation into an RPM.

===================================================================
EOF
    exit 1
fi

rm -fr %{tmp_install}/UninstallerData
pushd %{tmp_install}
perl -p -i -e 's,^(lax\.dir|lax\.root\.install\.dir)=.*,\1=%{jardir},' ncBrowse.lax
jars=`for f in *.jar ; do echo %{jardir}/$f; done`
popd

classpath=`echo $jars | tr ' ' :`
cat > ncBrowse <<EOF
#!/bin/sh
export PATH=$java_bin_dir:\$PATH
classpath="$classpath"
java -cp \$classpath ncBrowse.Browser \$1
EOF



%install
rm -fr $RPM_BUILD_ROOT
tmp_jardir=$RPM_BUILD_ROOT/%{jardir}
mkdir -p `dirname $tmp_jardir`
mv %{tmp_install} $tmp_jardir

tmp_script=$RPM_BUILD_ROOT/%{script}
mkdir -p `dirname $tmp_script`
mv ncBrowse $tmp_script


%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Thu Jan 24 2013  <builderdev@builder.jc.rl.ac.uk> - 1.6.5-1.ceda
- hack based on first running the graphical installer outside of rpmbuild (as the installer doesn't want to run in non-GUI mode at all, or in GUI mode inside rpmbuild)

%files
%defattr(755,root,root)
%{script}
%defattr(-,root,root)
%{jardir}
