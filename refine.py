f=open('sortedleadCountry_city.txt','r')
for line in f:
	arr=line.split()
	print arr[0].split(';')[0],arr[1]