#!/usr/bin/env python
import sys

for line in sys.stdin:
    line=line.strip()
    entries=line.split('\t')
    country=entries[2].strip()
    if country==sys.argv[1].strip():
    	print entries[3].strip()+";"+entries[6].strip()+"\t"+"1"
       
