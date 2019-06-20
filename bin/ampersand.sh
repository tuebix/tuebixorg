#!/usr/bin/env bash

set -o errexit
set -o xtrace

# ampersand
perl -p -i -e 's/ & / &#x26; /g' giggity.xml
perl -p -i -e 's/next&id/next&#x26;id/g' giggity.xml

xmllint giggity.xml --noout
