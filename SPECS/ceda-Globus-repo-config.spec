Name:           ceda-Globus-repo-config
Version:        5.2stable
Release:        2.ceda%{dist}
Summary:        Globus Repository Configuration
Group:          System Environment/Base
License:        ASL 2.0
URL:            http://globus.org
Source0:        RPM-GPG-KEY-Globus
Source1:        Globus-5.2.stable-config.redhat.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%global conf_file_tag line-added-by-globus-repo-rpm
%global repos_d_dir %{_sysconfdir}/yum.repos.d

%description

This package installs the Globus yum repository configuration with (NB
1=highest, 99=lowest), and the GPG key, and also (in a post-install
script) sets the priorities of Globus repos to 80 and all other repos
to 10 (though at the start of the relevant section to allow any
existing lines to override it).  The pre-install script also puts
"exclude=" for the Globus packages into the epel-tier1 repo config.
The result will be that the Globus repository will be used for the
Globus packages (ignoring any with the same name in epel-tier1), but
anything else in the Globus repo will not override packages in other
repos.

%prep
%setup -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# gpg
install -Dpm 644 %{SOURCE0}   $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-Globus

# yum
install -dm 755 $RPM_BUILD_ROOT%{repos_d_dir}
install -pm 644 %{SOURCE1}   $RPM_BUILD_ROOT%{repos_d_dir}


#--------------------------------------------------------------
# post-install script modifies the repos config files. 
# This includes the Globus repos config file itself, meaning that 
# a "pristine source" from Globus without the priority lines is used
# in this source RPM.  (Alternative to achieve that would be to patch
# it at RPM build time.) 
# Note that only stuff printed in the 'while' loop in the perl appears
# in the in-place edited files, hence the $done_hdr stuff instead of 
# just a print before the loop.
#--------------------------------------------------------------

%post
tmp_perl=%{repos_d_dir}/modify_conf_$$.pl
cat > $tmp_perl <<'EOF'
$tag="%{conf_file_tag}";
$excludes="globus-* gsi-openssh* grid-packaging-tools myproxy*";
while(<>) {
    unless ($done_hdr) {
        print "# lines containing '$tag' will be auto-removed on uninstall of %{name}\n";
        $done_hdr = 1;
    }
    print;
    if (/^\s*\[(.*)\]/) {
       $section = $1;
       if ($section =~ /^Globus/) {
           print "priority = 80  # $tag\n";
           print "proxy = http://wwwcache.rl.ac.uk:8080/  # $tag\n";
       } else {
           print "priority = 10  # $tag\n";
       }       
       if ($section eq 'epel-tier1') {
          print "exclude = $excludes  # $tag\n";
       }
    }
}
EOF
for i in %{repos_d_dir}/*.repo
do
    perl -i $tmp_perl $i
done
rm -f $tmp_perl

%postun
for i in %{repos_d_dir}/*.repo
do
    if fgrep -q "%{conf_file_tag}" $i > /dev/null
    then
        tmp=$i.tmp$$
        fgrep -v "%{conf_file_tag}" $i > $tmp && mv -f $tmp $i
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config %{repos_d_dir}/*

%changelog
* Tue May  7 2013  <builderdev@builder.jc.rl.ac.uk> - 5.2stable-2.ceda%{dist}
- proxy only for globus

* Fri May 03 2013 Alan Iwi - 1.ceda
- CEDA customisation, including all the %post and %postun stuff
