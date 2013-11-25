import sys
for line in sys.stdin:
    entries=line.split(',')
    print entries[1]+" "+entries[0]
