#!/bin/sh

#
# wrapper script as root to 'su' to user jap to generate the HTML table 
# and then put it up in an editor for copying and pasting into help scout
#

dir=/home/jap/auto-doc

su jap -c "cd $dir ; python create_html_table.py"

cat <<EOF 
launching editor - copy and paste content into
https://secure.helpscout.net/docs/56d57ee09033601bde8bae50/article/57f264379033602e61d4ad75
EOF
 
leafpad $dir/packages.html

