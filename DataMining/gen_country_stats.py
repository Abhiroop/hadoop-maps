from collections import Counter
f=open("country_stats.txt","r")
f1=open("country1.txt","w");
f2=open("country2.txt","w");
f3=open("country3.txt","w");
finallist=[]
for line in f:
	line=line.strip('\t\n\r')
	list1=line.split("\t")
	finallist.append(list1)
country_count_list=[]
current_word = None
current_count = 0
word = None
curr_casuality=0

for i in finallist:
    word=i[0].strip()
    count="1"
    casuality_count=int(i[-1].strip())
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
        curr_casuality+=casuality_count
    else:
        if current_word:
            country_count_list.append([current_word, current_count,curr_casuality])
        current_count = count
        current_word = word
        curr_casuality=casuality_count


if current_word == word:
    country_count_list.append([current_word, current_count,curr_casuality])
country_count_list.sort(key=lambda x:x[1],reverse=True)

place=[]
location=[]
count=1
for i in country_count_list:
	for l in finallist:
		if i[0].strip()==l[0].strip():
			place.append(l[1].strip())
			location.append(l[2].strip())
	a=Counter(place).most_common(3)
	b=Counter(location).most_common(3)
	print a
	print b
	break
					


