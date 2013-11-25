#!/usr/bin/env python
import sys

for line in sys.stdin:
    line=line.strip()
    entries=line.split('\t')
    event=entries[0].strip()
    if event==sys.argv[1].strip():
    	print entries[2].strip()+"\t"+"1"
       
