Summary: A lightweight visulisation GUI for use with Iris and Cartopy
Name: thea
Version: 0.1
Release: 1.ceda
License: (c) Met Office, see URL for details
Group: Scientific support
URL: https://github.com/SciTools/thea
Source0: %{name}-%{version}.tar.gz
Patch0: thea-main.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python27-pyside
BuildRequires: python27-pyside texlive-latex

%description

Thea is a lightweight visulisation tool designed for use with Iris and Cartopy.
It allows you to quickly and easily load a le, and then view plots of the
cubes within it.

You are able to select which cube from the le you would like to plot,
and, for cubes with more than 2 dimensions, you are able to choose to plot
any 2D slice of the cube.

Further, you have numerous options regarding how the cube will be plot-
ted, from the type of graph, to drawing coastlines.

%prep
%setup -n %{name}-%{version}
%patch0 -p0

%build
make
chmod a+x lib/thea/main.py
(cd docs; for repeat in 1 2 ; do pdflatex user_manual.tex; done)

%install
%define lib_target %{_datadir}/%{name}
%define doc_target %{_docdir}/%{name}
%define tmp_lib_target $RPM_BUILD_ROOT/%{lib_target}
%define tmp_doc_target $RPM_BUILD_ROOT/%{doc_target}
%define tmp__bindir $RPM_BUILD_ROOT/%{_bindir}

rm -rf $RPM_BUILD_ROOT
mkdir -p %{tmp_lib_target} %{tmp_doc_target} %{tmp__bindir}
(cd lib/thea && tar cf - .) | (cd %{tmp_lib_target} && tar xf -)
rm %{tmp_lib_target}/Makefile
cp docs/user_manual.pdf %{tmp_doc_target}/
ln -s %{lib_target}/main.py %{tmp__bindir}/thea

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{lib_target}/*
%{_bindir}/thea
%doc %{doc_target}/user_manual.pdf

%changelog
* Tue Oct 22 2013  Alan Iwi <alan.iwi@stfc.ac.uk> - v0.1
- Initial build.

