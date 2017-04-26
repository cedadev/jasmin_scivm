Name: xconv
Version: 1.93
Release: 1.ceda%{?dist}
Source0: xconv1.93
License: NCAS
Group: Scientific support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix} 
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Vendor: NCAS
Url: http://cms.ncas.ac.uk/documents/xconv/index.html
Summary: a tool for viewing and converting climate data in various formats

%description

Xconv is a program designed to convert model output into a format
suitable for use in various plotting packages. Xconv is designed to be
simple to use with a point and click, windows based interface. Xconv
can read data in the following formats:

    Data output from the Met. Office Unified Model

    Met. Office PP format

    GRIB format (Edition 1 and 2)

    NetCDF format (classic, 64-bit offset and netCDF-4 classic model)

    Grads format

The following output formats are supported by xconv:

    NetCDF format (classic, 64-bit offset and netCDF-4 classic model)

    Grads format

Xconv can be used to see what fields are contained within a data file
and to look at the data values, either directly at the numerical
values or at a grid box fill plot of the data. xconv can also be used
to manipulate the input data before it is converted into the output
format. Data manipulations available are:

    Spectral data can be transformed to grid point data

    The inverse Laplacian operator can be applied to spectral data

    Grid point data can interpolated onto a different grid using
    either bilinear interpolation or area weighted interpolation

    Data which is on a rotated grid can be unrotated, plus normal
    gridded data can be put on a rotated grid.

    Data values can be extrapolated over missing data values

    Zonal and meridonal means can be computed

    The missing data value can be changed

Also available is convsh, which allows scripts to be written to
automate various xconv tasks. Convsh uses the tcl scripting language,
plus various extensions for reading, writing and manipulating data
files.

%prep

%build

%install
[ $RPM_BUILD_ROOT != / ] && rm -fr $RPM_BUILD_ROOT

dir=$RPM_BUILD_ROOT/%{_bindir}
mkdir -p $dir
#gzip -dc < %{SOURCE0} > $dir/xconv
cp %{SOURCE0} $dir/xconv
ln -s xconv $dir/convsh

# don't strip the binaries during RPM build
%define __os_install_post %{nil}

# also prevent prelink tampering with the executable, which breaks it
%define prelink_conf /etc/prelink.conf.d/xconv.conf
tmp_prelink_conf=$RPM_BUILD_ROOT/%{prelink_conf}
mkdir -p `dirname $tmp_prelink_conf`
echo "-b /usr/bin/xconv" > $tmp_prelink_conf

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Nov  9 2015  <builderdev@builder.jc.rl.ac.uk> - 1.93-1.ceda
- upgrade to 1.93; change URL; update description based on NCAS website

* Wed Feb  5 2014  <builderdev@builder.jc.rl.ac.uk> - 1.92dev-1.ceda
- upgrade to 1.92dev

* Wed Jan 23 2013  <builderdev@builder.jc.rl.ac.uk> - 1.91-3.ceda
- add prelink stuff

%files
%defattr(755,root,root)
%{_bindir}/xconv
%{_bindir}/convsh
%defattr(-,root,root)
%{prelink_conf}
