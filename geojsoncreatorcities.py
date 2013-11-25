f=open('sortedleadCountry.txt','r')
f1=open('geojson','w')
i=0
f1.write('eqfeed_callback({"type": "FeatureCollection","features": [')
for line in f:
	if i<7:
		arr=line.split();
		f1.write('{"type": "Feature","geometry": {"type": "Point","coordinates": [')
		arr1=arr[0].split(';')
		f1.write(arr1[1].split(',')[1])
		f1.write(',')
		f1.write(arr1[1].split(',')[0])
		f1.write(']}}')
		if(i<6):
			f1.write(',')
		i=i+1
f1.write(']});')