Summary: A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator.
Name: triangle
Version: 1.6
Release: 1.cdat%{?dost}
License: Noncommercial
Group: Scientific support
URL: http://www.cs.cmu.edu/~quake/triangle.html
Source0: %{name}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

Triangle generates exact Delaunay triangulations, constrained Delaunay
triangulations, conforming Delaunay triangulations, Voronoi diagrams,
and high-quality triangular meshes. The latter can be generated with
no small or large angles, and are thus suitable for finite element
analysis.

%prep
rm -fr triangle
mkdir triangle
cd triangle
unzip %{SOURCE0}

%build
cd triangle
make

%install
cd triangle
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
install -m 755 triangle showme $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/triangle
%{_bindir}/showme
%doc


%changelog
* Mon Feb  3 2014  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.

