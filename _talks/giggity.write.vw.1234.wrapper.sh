#!/bin/sh
for i in $(ls -1 *.md | grep -v gottschall); do ./giggity.write.vw.1234.py $i; done
