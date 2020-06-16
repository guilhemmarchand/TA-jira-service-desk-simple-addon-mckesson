#!/usr/bin/env bash
# set -x

PWD=`pwd`
app="TA-jira-service-desk-simple-addon-mck"
version=`grep 'version =' TA-jira-service-desk-simple-addon-mck/default/app.conf | head -1 | awk '{print $3}' | sed 's/\.//g'`

find . -name "*.pyc" -type f -exec rm -f {} \;
rm -f *.tgz
tar -czf ${app}_${version}.tgz --exclude=TA-jira-service-desk-simple-addon-mck/local --exclude=TA-jira-service-desk-simple-addon-mck/metadata/local.meta --exclude=TA-jira-service-desk-simple-addon-mck/lookups/lookup_file_backups TA-jira-service-desk-simple-addon-mck
echo "Wrote: ${app}_${version}.tgz"

exit 0

