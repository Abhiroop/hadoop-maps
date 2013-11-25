#!/usr/bin/env python
import sys

for line in sys.stdin:
    line=line.strip()
    entries=line.split('\t')
    year=entries[1].split(',')[1].strip()
    if entries[4].strip()=="-":
    	entries[4]="0"
    if entries[5].strip()=="-":
    	entries[5]="0"
    
    dead_wounded=int(entries[4])+int(entries[5])
    
    if year==sys.argv[1].strip():
			print '%s\t%s' % (entries[0].strip(), 1)
       
