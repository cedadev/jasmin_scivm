Name: grads
Version: 2.1.1.b0
Release: 1.ceda%{dist}
License: GPLv2
Group: Scientific support
URL: http://cola.gmu.edu/grads/
Source0: grads-%{version}-bin-CentOS6-x86_64.tar.gz
Source1: ftp://cola.gmu.edu/grads/2.1/grads-2.1.1.b0-src.tar.gz
Source2: grads_sources.readme
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: COLA
Summary: Grid Analysis and Display System

%description

The Grid Analysis and Display System (GrADS) is an interactive desktop
tool that is used for easy access, manipulation, and visualization of
earth science data. GrADS has two data models for handling gridded and
station data. GrADS supports many data file formats, including binary
(stream or sequential), GRIB (version 1 and 2), NetCDF, HDF (version 4
and 5), and BUFR (for station data). GrADS has been implemented
worldwide on a variety of commonly used operating systems and is
freely distributed over the Internet.

GrADS uses a 5-Dimensional data environment: the four conventional
dimensions (longitude, latitude, vertical level, and time) plus an
optional 5th dimension for grids that is generally implemented but
designed to be used for ensembles. Data sets are placed within the 5-D
space by use of a data descriptor file. GrADS handles grids that are
regular, non-linearly spaced, gaussian, or of variable
resolution. Data from different data sets may be graphically overlaid,
with correct spatial and time registration. Operations are executed
interactively by entering FORTRAN-like expressions at the command
line. A rich set of built-in functions are provided, but users may
also add their own functions as external routines written in any
programming language.

Data may be displayed using a variety of graphical techniques: line
and bar graphs, scatter plots, smoothed contours, shaded contours,
streamlines, wind vectors, grid boxes, shaded grid boxes, and station
model plots. Graphics may be output in PostScript or image
formats. GrADS provides geophysically intuitive defaults, but the user
has the option to control all aspects of graphics output.

GrADS has a programmable interface (scripting language) that allows
for sophisticated analysis and display applications. Use scripts to
display buttons and dropmenus as well as graphics, and then take
action based on user point-and-clicks. GrADS can be run in batch mode,
and the scripting language facilitates using GrADS to do long
overnight batch jobs.

%prep

%setup0 -n %{name}-%{version}

%build
%define debug_package %{nil}

%install

rm -fr $RPM_BUILD_ROOT

%define sharedir %{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{sharedir}

cd bin
cp `find . -type f -perm -100` $RPM_BUILD_ROOT/%{_bindir}
cp COPYRIGHT $RPM_BUILD_ROOT/%{sharedir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

%files

%defattr(0755, root, root)
%{_bindir}/*

%defattr(0644, root, root)
%doc %{sharedir}/COPYRIGHT
