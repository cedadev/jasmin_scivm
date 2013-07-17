%global repo_config ceda-Globus-repo-config

%global package_list_no_devel_no_gram globus-authz globus-authz-callout-error globus-authz-callout-error-doc globus-authz-doc globus-callout globus-callout-doc globus-common globus-common-doc globus-common-progs globus-core globus-data-management-client globus-data-management-sdk globus-data-management-server globus-ftp-client globus-ftp-client-doc globus-ftp-control globus-ftp-control-doc globus-gass-cache globus-gass-cache-program globus-gass-copy globus-gass-copy-doc globus-gass-copy-progs globus-gass-server-ez globus-gass-server-ez-progs globus-gass-transfer globus-gass-transfer-doc globus-gatekeeper globus-gfork globus-gfork-progs globus-gridftp globus-gridftp-server globus-gridftp-server-control globus-gridftp-server-progs globus-gridmap-callout-error globus-gridmap-callout-error-doc globus-gsi globus-gsi-callback globus-gsi-callback-doc globus-gsi-cert-utils globus-gsi-cert-utils-doc globus-gsi-cert-utils-progs globus-gsi-credential globus-gsi-credential-doc globus-gsi-openssl-error globus-gsi-openssl-error-doc globus-gsi-proxy-core globus-gsi-proxy-core-doc globus-gsi-proxy-ssl globus-gsi-proxy-ssl-doc globus-gsi-sysconfig globus-gsi-sysconfig-doc globus-gssapi-error globus-gssapi-error-doc globus-gssapi-gsi globus-gssapi-gsi-doc globus-gss-assist globus-gss-assist-doc globus-gss-assist-progs globus-io globus-openssl-module globus-openssl-module-doc globus-proxy-utils globus-resource-management-client globus-resource-management-sdk globus-resource-management-server globus-rsl globus-rsl-doc globus-scheduler-event-generator globus-scheduler-event-generator-doc globus-scheduler-event-generator-progs globus-simple-ca globus-usage globus-xio globus-xio-doc globus-xio-gsi-driver globus-xio-gsi-driver-doc globus-xioperf globus-xio-pipe-driver globus-xio-popen-driver grid-packaging-tools gsi-openssh gsi-openssh-clients myproxy myproxy-admin myproxy-doc myproxy-libs myproxy-server
# gsi-openssh-server removed

%global gram_list globus-gram5 globus-gram-audit globus-gram-client globus-gram-client-doc globus-gram-client-tools globus-gram-job-manager globus-gram-job-manager-callout-error globus-gram-job-manager-callout-error-doc globus-gram-job-manager-condor globus-gram-job-manager-doc globus-gram-job-manager-fork globus-gram-job-manager-fork-doc globus-gram-job-manager-fork-setup-poll globus-gram-job-manager-fork-setup-seg globus-gram-job-manager-pbs globus-gram-job-manager-pbs-doc globus-gram-job-manager-pbs-setup-poll globus-gram-job-manager-pbs-setup-seg globus-gram-job-manager-scripts globus-gram-job-manager-scripts-doc globus-gram-job-manager-sge globus-gram-job-manager-sge-doc globus-gram-job-manager-sge-setup-poll globus-gram-job-manager-sge-setup-seg globus-gram-protocol globus-gram-protocol-doc

%global devel_list globus-authz-callout-error-devel globus-authz-devel globus-callout-devel globus-common-devel globus-ftp-client-devel globus-ftp-control-devel globus-gass-cache-devel globus-gass-copy-devel globus-gass-server-ez-devel globus-gass-transfer-devel globus-gfork-devel globus-gram-client-devel globus-gram-job-manager-callout-error-devel globus-gram-protocol-devel globus-gridftp-server-control-devel globus-gridftp-server-devel globus-gridmap-callout-error-devel globus-gsi-callback-devel globus-gsi-cert-utils-devel globus-gsi-credential-devel globus-gsi-openssl-error-devel globus-gsi-proxy-core-devel globus-gsi-proxy-ssl-devel globus-gsi-sysconfig-devel globus-gssapi-error-devel globus-gssapi-gsi-devel globus-gss-assist-devel globus-io-devel globus-openssl-module-devel globus-rsl-devel globus-scheduler-event-generator-devel globus-usage-devel globus-xio-devel globus-xio-gsi-driver-devel globus-xio-pipe-driver-devel globus-xio-popen-driver-devel myproxy-devel

# uncomment as appropriate (and adjust Summary below to reflect)
#%global package_list %{package_list_no_devel_no_gram} %{gram_list} %{devel_list}
%global package_list %{package_list_no_devel_no_gram}


Summary: Adds all the globus packages (except devel). First install %{repo_config}.
Name: all-globus-packages
Version: 1.0
Release: 2.ceda
Group: Utilities/Configuration
License: Copyright STFC
BuildRoot: %{_builddir}/%{name}-root
Packager: Alan Iwi <alan.iwi@stfc.ac.uk>
BuildArch: noarch
Requires: %{repo_config}
Requires: %{package_list}

%description
Installs all the globus packages. Checks that they really come from the Globus build not the fedora ones.

%prep
%build
%clean
%install
%files

%pre
fedora_rpm_list=/root/globus-meta-rpm-tmp.$$
rpm -q --queryformat="%{NAME} %{BUILDHOST}\n" %{package_list} | fgrep fedoraproject.org > $fedora_rpm_list
grep_status=$?
if [ $grep_status -eq 0 ]
then
   # we found some fedora RPMs
   echo "The following packages are built by fedora, not the ones you want. Uninstall them, and install %{repo_config} before installing %{name}"
   cat $fedora_rpm_list
   rm -f $fedora_rpm_list
   exit 1
fi
rm -f $fedora_rpm_list



%changelog
* Thu Jun 27 2013  <builderdev@builder.jc.rl.ac.uk> - 1.0-2.ceda
- remove gsi-openssh-server; also fix the %pre script to actually show the fedora packages

* Fri May 03 2013 Alan Iwi <alan.iwi@stfc.ac.uk> 1.0
Initial version
