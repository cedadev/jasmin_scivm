%define gpgkey RPM-GPG-KEY-ceda-dist

Name:           ceda-yumrepo
Version:        0.1
Release:        1.ceda%{dist}
Summary:        dist.ceda.ac.uk Repository Configuration
Group:          System Environment/Base
License:        GPL
URL:            http://dist.ceda.ac.uk
Source0:        %{gpgkey}
Source1:        ceda-dist-config.redhat.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description

This package installs the yum repository configuration for dist.ceda.ac.uk.

%global gpg_dir %{_sysconfdir}/pki/rpm-gpg
%global repos_d_dir %{_sysconfdir}/yum.repos.d

%prep
%setup -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# gpg
install -dm 755 $RPM_BUILD_ROOT%{gpg_dir}
install -pm 644 %{SOURCE0}   $RPM_BUILD_ROOT%{gpg_dir}

# yum
install -dm 755 $RPM_BUILD_ROOT%{repos_d_dir}
install -pm 644 %{SOURCE1}   $RPM_BUILD_ROOT%{repos_d_dir}


%post
rpm --import %{gpg_dir}/%{gpgkey}

%postun
key_id=`rpm -q --queryformat="%{NAME}-%{RELEASE} %{SUMMARY}\n" "gpg-pubkey-*" | awk '/JASMIN\/CEMS/{print $1}'`
if [ ! -z "$key_id" ]
then
   cat <<EOF
The yum configuration for the dist.ceda.ac.uk repository has just been
uninstalled.  You may also wish to remove the JASMIN/CEMS signing key
from your database of trusted keys if it is not in other use.  If so,
type:

     rpm -e gpg-pubkey-$key_id

EOF
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{gpg_dir}/*
%config %{repos_d_dir}/*

%changelog
* Mon Jul 15 2013 Alan Iwi <alan.iwi_AT_stfc.ac.uk> - 0.1-1.ceda%{dist}
- initial version

