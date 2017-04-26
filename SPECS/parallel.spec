Name:		parallel
Version:	20160822
Source0:	parallel-%{version}.tar.bz2
Patch0:         parallel-cite.patch
Release:	1.ceda%{?dist}
Summary:        A shell tool for executing jobs in parallel using one or more computers
Group:		Development/Other
License:	GPLv3+
URL:		http://www.gnu.org/software/parallel
Packager:       alan.iwi@stfc.ac.uk

#BuildRequires:	
#Requires:	

%description

GNU parallel is a shell tool for executing jobs in parallel using one or more computers. A job can be a single command or a small script that has to be run for each of the lines in the input. The typical input is a list of files, a list of hosts, a list of users, a list of URLs, or a list of tables. A job can also be a command that reads from a pipe. GNU parallel can then split the input and pipe it into commands in parallel.
If you use xargs and tee today you will find GNU parallel very easy to use as GNU parallel is written to have the same options as xargs. If you write loops in shell, you will find GNU parallel may be able to replace most of the loops and make them run faster by running several jobs in parallel.

GNU parallel makes sure output from the commands is the same output as you would get had you run the commands sequentially. This makes it possible to use output from GNU parallel as input for other programs.

For each line of input GNU parallel will execute command with the line as arguments. If no command is given, the line of input is executed. Several lines will be run in parallel. GNU parallel can often be used as a substitute for xargs or cat | bash.

%prep
%setup -q
%patch0 -p1


%build
%configure
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# to avoid auto RPM dependency on shells not used on JASMIN, 
# remove the setup scripts for them
rm $RPM_BUILD_ROOT%{_bindir}/env_parallel.{pdksh,ksh,fish,zsh}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc
%{_docdir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* Sun Sep 18 2016  <builderdev@builder.jc.rl.ac.uk> - 2016.08.22-1.ceda
- initial version


