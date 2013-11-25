f=open('/var/www/DataMining/AnalysisByYear/abcd.txt','r')
f1=open('/var/www/geojson','w')
count=0
f1.write('eqfeed_callback({  "type": "FeatureCollection","features": [')
i=0
for line in f:
  if i>3:
    line=line.replace('[','')
    line=line.replace(']','')
    arr=line.split('), ')
    for j in xrange(len(arr)):
      f1.write('{"type": "Feature","geometry": {"type": "Point","coordinates": [')
      axe=arr[j].split(',')
      axe[0]=axe[0].replace("('","")
      axe[1]=axe[1].replace("'","")
      f1.write(axe[1])
      f1.write(',')
      f1.write(axe[0])
      f1.write(']}}')
      if count<8:
        f1.write(',')
      count=count+1
  i=i+1
f1.write(']});')