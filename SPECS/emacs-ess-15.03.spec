%define pkg ess
%define pkgname Emacs Speaks Statistics

# If the emacs-el package has installed a pkgconfig file, use that to determine
# install locations and Emacs version at build time, otherwise set defaults.
%if %($(pkg-config emacs) ; echo $?)
%define emacs_version 23.1
%define emacs_lispdir %{_datadir}/emacs/site-lisp
%define emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%define emacs_version %(pkg-config emacs --modversion)
%define emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%define emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

# If the xemacs-devel package has installed a pkgconfig file, use that
# to determine install locations and Emacs version at build time,
# otherwise set defaults.

Name:           emacs-common-%{pkg}
Version:        15.03.1
Release:        1.ceda%{?dist}
Summary:        %{pkgname} add-on package for Emacs

Group:          Applications/Editors
License:        GPLv2+
URL:            http://ESS.R-project.org/
Source0:        http://ESS.R-project.org/downloads/ess/ess-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  emacs 
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description

%{pkgname} (ESS) is an add-on package for GNU Emacs and XEmacs.  
It provides Emacs-based front ends for popular statistics packages.

ESS provides an intelligent, consistent interface between the user and
the software.  ESS interfaces with S-PLUS, R, SAS, BUGS and other
statistical analysis packages under the Unix, Microsoft Windows, and
Apple Mac OS operating systems.  ESS is a package for the GNU Emacs
and XEmacs text editors whose features ESS uses to streamline the
creation and use of statistical software.  ESS knows the syntax and
grammar of statistical analysis packages and provides consistent
display and editing features based on that knowledge.  ESS assists in
interactive and batch execution of statements written in these
statistical analysis languages.

This package contains the files common to both the GNU Emacs and
XEmacs %{pkgname} packages.

%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run %{pkgname} under GNU Emacs
Group:          Applications/Editors
Requires:       emacs(bin) >= %{emacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg} 
This package contains the byte compiled elisp packages to run
%{pkgname} with GNU Emacs.


%package -n emacs-%{pkg}-el
Summary:        Elisp source files for %{pkgname} under GNU Emacs
Group:          Applications/Editors
Requires:       emacs-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}-el
This package contains the elisp source files for %{pkgname} 
under GNU Emacs. You do not need to install this package to run
%{pkgname}. Install the emacs-%{pkg} package to use 
%{pkgname} with GNU Emacs.


%prep
%setup -q -n %{pkg}-%{version}
( cd doc && chmod u+w html info ) # fix perms to ensure builddir can be deleted

%build
## first build GNU Emacs
for D in lisp etc
do
    cd $D
    make
    cd -
done

## don't build PDF or PS 
cd doc
make docs
cd -


# create an init file that is loaded when a user starts up emacs to
# tell emacs to autoload our package's Emacs code when needed
cat > %{name}-init.el <<"EOF"
;;; Set up %{name} for Emacs.
;;;
;;; This file is automatically loaded by emacs's site-start.el
;;; when you start a new emacs session.

(require 'ess-site)

EOF


%install
rm -rf $RPM_BUILD_ROOT

## now install GNU Emacs elisp

INITDIR=${RPM_BUILD_ROOT}%{emacs_startdir}
PKGLISP=${RPM_BUILD_ROOT}%{emacs_lispdir}/%{pkg}
ETCDIR=${PKGLISP}/etc
INFODIR=${RPM_BUILD_ROOT}%{_infodir}

%{__install} -m 755 -d $INITDIR
%{__install} -m 644 %{name}-init.el $INITDIR/%{pkg}-init.el
%{__install} -m 755 -d $PKGLISP
%{__install} -m 755 -d $INFODIR
%{__make} install \
          PREFIX=${RPM_BUILD_ROOT}%{_prefix} \
          LISPDIR=$PKGLISP \
          INFODIR=$INFODIR \
          ETCDIR=$ETCDIR \
          ETCFILES="backbug? *.S *.R sas* ess-sas-sh-command config.guess"
%{__rm} -f $INFODIR/dir # don't package but instead update in pre and post
%{__mv} $PKGLISP/ChangeLog ChangeLog.lisp

## now build and XEmacs elisp

make clean

## now fix permissions on doc files that aren't UTF-8
for i in ChangeLog ChangeLog.lisp doc/TODO
do
    /usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i
done


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/install-info %{_infodir}/ess.info.gz %{_infodir}/dir || :


%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/ess.info.gz \
	%{_infodir}/dir || :
fi


%files
%defattr(-,root,root,-)
%doc COPYING VERSION ChangeLog doc ChangeLog.lisp  
%doc fontlock-test
%doc LDA
%doc etc/sas-keys.*
%doc etc/function-outline.S
%doc etc/R-ESS-bugs.R
%doc etc/other
%doc %{_infodir}/*.gz
/usr/share/doc/ess/*

%files -n emacs-%{pkg}
%defattr(-,root,root,-)
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/etc
%{emacs_startdir}/*.el
%dir %{emacs_lispdir}/%{pkg}


%files -n emacs-%{pkg}-el
%defattr(-,root,root,-)
%{emacs_lispdir}/%{pkg}/*.el



%changelog
* Sun Mar  6 2016  <builderdev@builder.jc.rl.ac.uk> - 15.03.1-1.ceda
- downgrade emacs version in order to use standard Redhat emacs package

* Sun Oct 5 2014 Paul Johnson <pauljohn[AT]ku.edu>
- fixups for ESS 14.09 on Centos 7

* Tue Sep 24 2013 Paul Johnson <pauljohn[AT]ku.edu>
- fixups for ESS 13.05 and additional etc files that were not packaged

* Thu Sep 27 2012 Paul Johnson <pauljohn[AT]ku.edu
- for centos 6.3

* Sat Jan 28 2012 Paul Johnson <pauljohn[AT]ku.edu
- for centos 6.2

* Tue May 5 2009 Paul Johnson <pauljohn[AT]ku.edu>
- get rid of xemacs stuff

* Mon Aug  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.3.8-1
- Update to latest upstream (5.3.8)

* Tue Apr 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.3.7-1
- Update to new upstream release (5.3.7)

* Sun Nov 18 2007 <alexlan@fedoraproject.org> - 5.3.6-2
- Moved all non-code related files in etc/ to documentation directory
- Make sure all doc files are UTF-8
- Fix post, preun scriptlets and add Requires for installing info
  files

* Tue Nov 13 2007 <alexlan@fedoraproject.org> - 5.3.6-1
- Initial packaging, borrowed some elements of package by Tom Moertel
  <tom-rpms@moertel.com>
