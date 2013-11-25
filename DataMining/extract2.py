#!/usr/bin/env python
import time
from selenium import webdriver

fo = open("data.txt", "a")
browser = webdriver.Firefox()
browser.get('http://terrorist-attacks.findthedata.org/')
next=browser.find_element_by_css_selector("div.next.bg_grad.float")
	
i=0

while i<82594:
        if i!=0:
                time.sleep(60)
                next=browser.find_element_by_css_selector("div.next.bg_grad.float")
                next.click()
        time.sleep(60)
        value1=browser.find_elements_by_css_selector("td.srp-cell")
        value2=browser.find_elements_by_css_selector("td.srp-cell.centered")
        value3=browser.find_elements_by_css_selector("td.srp-cell.last_td")
        print str(len(value1))+" "+str(len(value2))+" "+str(len(value3))+"\n"
         
        for j in xrange(len(value1)):
                print value1[j].text+"\n"
        """
        print "\n\n"
        for j in xrange(len(value2)):
                print value2[j].text+"\t\t"
        print "\n\n"
        for j in xrange(len(value3)):
                print value3[j].text+"\t\t"
         
        """
        """for j in xrange(len(value1)):
                print value1[j].text+"\t"+value2[j].text+"\t"+value3[j].text+"\n"
                break
        
        break
        """
        break
browser.quit()


