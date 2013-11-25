#!/usr/bin/env python
import time
from selenium import webdriver

fo=open("C:\Users\Abhinav\Desktop\data.txt","w")
browser = webdriver.Firefox()
browser.get('http://terrorist-attacks.findthedata.org/')
next=browser.find_element_by_css_selector("div.next.bg_grad.float")
	
i=0

while i<82594:
        if i!=0:
                time.sleep(60)
                next=browser.find_element_by_css_selector("div.next.bg_grad.float")
                next.click()
       # time.sleep(60)
        value1=browser.find_elements_by_xpath("//td[@class='srp-cell']")
        value2=browser.find_elements_by_xpath("//table[@id='srp-results']/tbody/tr[@class='srp-row']/td[@class='srp-cell centered']")
        value3=browser.find_elements_by_xpath("//table[@id='srp-results']/tbody/tr[@class='srp-row']/td[@class='srp-cell last_td']")
        j=0
        while j <(len(value3)):
                list1=value1[j:j+6]
                #print list1
                
                fo.write("Country-"+list1[0].text+"\n"+"Event Type-"+list1[1].text+"\n"+"Facility Type-"+list1[2].text+"\n"+"Facility Damage-"+list1[3].text+"\n"+"Weapon Type-"+list1[4].text+"\n"+"Victim Type-"+list1[5].text+"\n")
                
                list1=value2[j:j+2]
                print list1
                fo.write("Dead Count-"+list1[0].text+"\n"+"Wounded Count-"+list1[1].text+"\n")  
                fo.write("Date-"+value3[j].text+"\n")  
                
                #print value1[j].text+"\t"+value2[j].text+"\t"+value3[j].text+"\n"
                
                break
        
        break
        
        
browser.quit()

