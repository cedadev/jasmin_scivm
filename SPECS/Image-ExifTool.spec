# Spec file based on cpan2rpm output with local tweaks.

%define pkgname Image-ExifTool
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

name:      perl-Image-ExifTool
summary:   Image-ExifTool - Read and write meta information
version:   9.98
release:   1.ceda%{dist}
vendor:    Phil Harvey (phil@owl.phy.queensu.ca)
packager:  Alan Iwi <alan.iwi@stfc.ac.uk>
license:   Artistic
group:     Applications/CPAN
url:       http://www.cpan.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: noarch
prefix:    /usr
source:    Image-ExifTool-9.98.tar.gz

%description
Reads and writes meta information in a wide variety of files, including the
maker notes of many digital cameras by various manufacturers such as Canon,
Casio, FLIR, FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Nintendo, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and
Sony.

Below is a list of file types and meta information formats currently
supported by ExifTool (r = read, w = write, c = create):

  File Types
  ------------+-------------+-------------+-------------+------------
  3FR   r     | DVB   r/w   | KEY   r     | ORF   r/w   | RWL   r/w
  3G2   r/w   | DYLIB r     | LA    r     | OTF   r     | RWZ   r
  3GP   r/w   | EIP   r     | LFP   r     | PAC   r     | RM    r
  AA    r     | EPS   r/w   | LNK   r     | PAGES r     | SEQ   r
  AAX   r/w   | EPUB  r     | M2TS  r     | PBM   r/w   | SO    r
  ACR   r     | ERF   r/w   | M4A/V r/w   | PCD   r     | SR2   r/w
  AFM   r     | EXE   r     | MEF   r/w   | PDB   r     | SRF   r
  AI    r/w   | EXIF  r/w/c | MIE   r/w/c | PDF   r/w   | SRW   r/w
  AIFF  r     | EXR   r     | MIFF  r     | PEF   r/w   | SVG   r
  APE   r     | EXV   r/w/c | MKA   r     | PFA   r     | SWF   r
  ARW   r/w   | F4A/V r/w   | MKS   r     | PFB   r     | THM   r/w
  ASF   r     | FFF   r/w   | MKV   r     | PFM   r     | TIFF  r/w
  AVI   r     | FLA   r     | MNG   r/w   | PGF   r     | TORRENT r
  AZW   r     | FLAC  r     | MOBI  r     | PGM   r/w   | TTC   r
  BMP   r     | FLV   r     | MODD  r     | PLIST r     | TTF   r
  BTF   r     | FPF   r     | MOI   r     | PICT  r     | VCF   r
  CHM   r     | FPX   r     | MOS   r/w   | PMP   r     | VRD   r/w/c
  COS   r     | GIF   r/w   | MOV   r/w   | PNG   r/w   | VSD   r
  CR2   r/w   | GZ    r     | MP3   r     | PPM   r/w   | WAV   r
  CRW   r/w   | HDP   r/w   | MP4   r/w   | PPT   r     | WDP   r/w
  CS1   r/w   | HDR   r     | MPC   r     | PPTX  r     | WEBP  r
  DCM   r     | HTML  r     | MPG   r     | PS    r/w   | WEBM  r
  DCP   r/w   | ICC   r/w/c | MPO   r/w   | PSB   r/w   | WMA   r
  DCR   r     | ICS   r     | MQV   r/w   | PSD   r/w   | WMV   r
  DFONT r     | IDML  r     | MRW   r/w   | PSP   r     | WV    r
  DIVX  r     | IIQ   r/w   | MXF   r     | QTIF  r/w   | X3F   r/w
  DJVU  r     | IND   r/w   | NEF   r/w   | RA    r     | XCF   r
  DLL   r     | INX   r     | NRW   r/w   | RAF   r/w   | XLS   r
  DNG   r/w   | ITC   r     | NUMBERS r   | RAM   r     | XLSX  r
  DOC   r     | J2C   r     | ODP   r     | RAR   r     | XMP   r/w/c
  DOCX  r     | JNG   r/w   | ODS   r     | RAW   r/w   | ZIP   r
  DPX   r     | JP2   r/w   | ODT   r     | RIFF  r     |
  DR4   r/w/c | JPEG  r/w   | OFR   r     | RSRC  r     |
  DSS   r     | K25   r     | OGG   r     | RTF   r     |
  DV    r     | KDC   r     | OGV   r     | RW2   r/w   |

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  DPX            r
  ICC Profile    r/w/c  |  DICOM          r    |  APE            r
  MIE            r/w/c  |  Flash          r    |  Vorbis         r
  JFIF           r/w/c  |  FlashPix       r    |  SPIFF          r
  Ducky APP12    r/w/c  |  QuickTime      r    |  DjVu           r
  PDF            r/w/c  |  Matroska       r    |  M2TS           r
  PNG            r/w/c  |  MXF            r    |  PE/COFF        r
  Canon VRD      r/w/c  |  PrintIM        r    |  AVCHD          r
  Nikon Capture  r/w/c  |  FLAC           r    |  ZIP            r
  GeoTIFF        r/w/c  |  ID3            r    |  (and more)

#
# This package was generated automatically with the cpan2rpm
# utility.  To get this software or for more information
# please visit: http://perl.arix.com/
#

%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '` PREFIX=%{_prefix}
%{__make} 
%if %maketest
%{__make} test
%endif

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux
if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
then
    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
    %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
        | %{__sed} -e s+%{buildroot}++g                 \
        > %{buildroot}/var/adm/perl-modules/%{name}
fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  html config_files arg_files fmt_files Changes README";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Mon Jul 13 2015  <builderdev@builder.jc.rl.ac.uk> - 9.98-1.ceda%{dist}
- initial version from cpan2rpm and change prefix from /usr/local to /usr (in particular see 'prefix: /usr' and 'PREFIX=%{_prefix}' above)

* Mon Jul 13 2015 builderdev@builder.jc.rl.ac.uk
- Initial build.
