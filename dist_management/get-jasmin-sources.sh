#!/bin/sh
#
# grab the source RPMs corresponding to the binary RPMs for the JASMIN-repo mirror
# Alan Iwi 16 July 2013
#
# (run with "-v" option for more output)

base=/datacentre/opshome/dist/htdocs/yumrepo
rpm_dir=$base/RPMS
srpm_dir=$base/SRPMS
url_base=http://yumit.jc.rl.ac.uk/yum/rhel6/RPMS

echo_if_verbose()
{
    if [ $verbose -eq 1 ]
    then
	echo $1
    fi
}

verbose=0
if [ "X$1" = "X-v" ]
then
    verbose=1
fi

if [ ! -d $srpm_dir ]
then
    echo_if_verbose "creating $srpm_dir"
    mkdir -p $srpm_dir || exit 1
fi

retval=0

srpm_names=$(rpm -q --queryformat="%{SOURCERPM}\n" -p $rpm_dir/*.rpm | fgrep 'src.rpm' | sort -u)
for srpm_name in $srpm_names
do
   echo_if_verbose "$srpm_name"
   srpm_path=$srpm_dir/$srpm_name
   if [ -e $srpm_path ]
   then
       echo_if_verbose "already have $srpm_path"
   else
       srpm_url=$url_base/$srpm_name
       echo_if_verbose "Fetching $srpm_url to $srpm_path"
       if wget -q -O $srpm_path $srpm_url
       then
	   echo_if_verbose "Mirrored $srpm_name"
       else
           echo "*** Failed to mirror $srpm_name ***"
	   rm $srpm_path
           retval=1
       fi
   fi
done

exit $retval
