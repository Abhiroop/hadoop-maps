from geopy import geocoders
import time
import re
g=geocoders.GoogleV3()
count=0
f1=open('city.txt', 'r')
f=open('new_data.txt','a')
for line in f1:
        if count>=106 & count<=9000:
                line=re.sub(" in ",",",line)
                line=line.strip(' \t\n\r,')
                words=line.split(',')
                m=len(words)
                country=words[-1].strip(' \t\n\r')
              
                if m==2:
                        state=""
                if(m>2):
                        state=words[-2].strip(' \t\n\r')
                        if len(state.split(" "))>4:
                                state=""
                state=state.replace("'","")
                time.sleep(10)
                cord=g.geocode("%s, %s"%(state,country),exactly_one=False)
                print cord
                coord=cord[0][1]
                lat=coord[0]
                lng=coord[1]
                f.write(state+","+country+","+str(lat)+","+str(lng)+"\n")
                
        count=count+1               
f.close()	
