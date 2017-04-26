Summary: nccmp compares two NetCDF files bitwise. 
Name: nccmp
Version: 1.7.5.1
Release: 2.ceda%{?dist}
License: GPL v2
Group: Scientific support
URL: http://nccmp.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: netcdf
BuildRequires: netcdf

%description

nccmp compares two NetCDF files bitwise, semantically or with a user
defined tolerance (absolute or relative percentage). Parallel
comparisons are done in local memory without requiring temporary
files. Highly recommended for regression testing scientific models or
datasets in a test-driven development environment.

 Features

    Multi-threaded if posix threads are supported on your system.
    Prints differences and their locations (C or Fortran indexing). Format precision is customizable and allows hex.
    Specific variable inclusion or exclusion.
    Specific groups by short or full (absolute) names, or all (including recursive groups).
    Metadata and/or data comparisons.
    Global attributes compared with or without the history attribute.
    Exits when first difference is found or optionally continues to process all variables and/or attributes by force, or up to a global or per-variable count.
    Attribute exclusion when comparing metadata.
    Bitwise compare or with tolerances (absolute or relative).
    Header padding contents and attribute comparisons for NetCDF3 classic/64bit file formats.
    NaN values can be treated as equal (in case you use NaN's as grid masks).
    Compare or dump encodings for one or both files: checksumming, chunking, compression, endianness, format, shuffling, and header-pad sizes.
    Support all Netcdf4/HDF atomic types (char/text, schar, uchar, short, ushort, int, uint, int64, uint64, float, double, string) and user-defined types (enumeration, compound, opaque blob, variable-length array) and nesting.
    Compare asymmetric atomic data type values, within variable-length arrays too. For example, a variable can be uint in the first file, and int64 in the second.
    Compare similarly named compound fields and ignore differently named or missing fields, so compound schemas may have variation in field type, field order and field existence.
    Asymmetric enum value and datatype semantics. Enum identifiers are compared instead of their encoded values, so your dataset schema can evolve flexibly without worrying about enum order, size, type, or numeric values, although any metadata differences will be reported.
    Lightweight. Comparing multi-gigabyte files will only consume several megabytes of memory.
    Written in the most portable language, C.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT	

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/nccmp
%doc %{_mandir}/man1/nccmp.1.gz

%changelog
* Fri Apr  8 2016  <builderdev@builder.jc.rl.ac.uk> - 1.7.5.1-2.ceda
- rebuild against netcdf 4.4.0

* Sat Nov  7 2015  <builderdev@builder.jc.rl.ac.uk> - 
- Initial build.

