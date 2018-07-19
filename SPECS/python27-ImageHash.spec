%define pname ImageHash
Summary: Image Hashing library
Name: python27-%{pname}
Version: 4.0
Release: 1.ceda%{?dist}
Source0: %{pname}-%{version}.tar.gz
License: BSD 2-clause (see LICENSE file)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Johannes Buchner <buchner.johannes@gmx.at>
Url: https://github.com/JohannesBuchner/imagehash
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
Requires: python27 
BuildRequires: python27
BuildArch: noarch

%description

ImageHash
===========

A image hashing library written in Python. ImageHash supports:

* average hashing (`aHash`_)
* perception hashing (`pHash`_)
* difference hashing (`dHash`_)
* wavelet hashing (`wHash`_)

Rationale
---------
Why can we not use md5, sha-1, etc.?

Unfortunately, we cannot use cryptographic hashing algorithms in our
implementation. Due to the nature of cryptographic hashing algorithms,
very tiny changes in the input file will result in a substantially
different hash. In the case of image fingerprinting, we actually want
our similar inputs to have similar output hashes as well.

Requirements
-------------
Based on PIL/Pillow Image, numpy and scipy.fftpack (for pHash)
Easy installation through `pypi`_.

Basic usage
------------
::

	>>> from PIL import Image
	>>> import imagehash
	>>> hash = imagehash.average_hash(Image.open('test.png'))
	>>> print(hash)
	d879f8f89b1bbf
	>>> otherhash = imagehash.average_hash(Image.open('other.bmp'))
	>>> print(otherhash)
	ffff3720200ffff
	>>> print(hash == otherhash)
	False
	>>> print(hash - otherhash)
	36

The demo script **find_similar_images** illustrates how to find
similar images in a directory.

Source hosted at github: https://github.com/JohannesBuchner/imagehash




%prep
%setup -n %{pname}-%{version}

%build
python2.7 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2.7 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
