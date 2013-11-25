import sys

for line in sys.stdin:
    line=line.strip()
    entries=line.split('\t');
    if entries[0].strip()=="Bombing":
        print entries[0]+","+entries[2]+","+"1"
       
