#!/bin/bash

# Determine R versions
R_SUPER_VERSION=`R --version | grep "R version" | cut -d " " -f 3 | cut -d "." -f 1`
R_MAJOR_VERSION=`R --version | grep "R version" | cut -d " " -f 3 | cut -d "." -f 2`

# If R 3.0.* ever comes out, we'll need to revisit this logic.
# Or, just nuke this script and the macros entirely.
if [ "$R_SUPER_VERSION" -ge "2" -a "$R_MAJOR_VERSION" -ge "10" ]; then
  # echo "R is new enough to not need this anymore."
  exit 0
else

# Figure out what RHOME is set to
TMP_R_HOME=`R RHOME`

# Figure out what R_DOC_DIR is set to
# Ideally, we could ask R just like we do for RHOME, but we can't yet.
TMP_R_DOC_DIR=`grep "R_DOC_DIR=" /usr/bin/R | cut -d "=" -f 2`

# Write out all the contents in arch library locations
cat $TMP_R_HOME/library/*/CONTENTS > $TMP_R_DOC_DIR/html/search/index.txt 2>/dev/null
# Don't use .. based paths, substitute TMP_R_HOME
sed -i "s!../../..!$TMP_R_HOME!g" $TMP_R_DOC_DIR/html/search/index.txt

# Write out all the contents in noarch library locations
cat /usr/share/R/library/*/CONTENTS >> $TMP_R_DOC_DIR/html/search/index.txt 2>/dev/null
# Don't use .. based paths, substitute /usr/share/R
sed -i "s!../../..!/usr/share/R!g" $TMP_R_DOC_DIR/html/search/index.txt

fi

exit 0

