import sys
for line in sys.stdin:
    line=line.strip()
    entries=line.split('\t')
    print entries[1]+","+entries[0]       
