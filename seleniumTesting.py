# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:37:47 2020

@author: Jensen
"""
from bs4 import BeautifulSoup


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

def scrapeClubInfo(club):
    title = club.find("h2", class_="box-title").getText()
    info = club.find("p", class_="ng-binding").getText()
    return {
        'title': title,
        'info': info
    }

driver = webdriver.Chrome("C:/Users/Jensen/chromedriver.exe", options=options)

URL = "https://orgs.studentinvolvement.ufl.edu/Organizations#!#searchresults"

driver.get(URL)

driver.implicitly_wait(10)

clubsDict = {}
okay = driver.find_elements_by_css_selector("div[ng-if='organizations.length > 0']")
for meme in okay:
    club = BeautifulSoup(meme.get_attribute('innerHTML'), 'html.parser')
    temp = scrapeClubInfo(club)
    clubsDict[temp['title']] = temp
    
#driver.find_element_by_xpath('//a[contains(text(), "2")]').click()

buttons = driver.find_elements_by_css_selector("a[ng-click='selectPage(page.number, $event)']")
print(buttons)
for button in buttons:
    if(button.text=="2"):
        button.click()
        print("this button!")
#okay = driver.find_elements_by_css_selector("div[ng-if='organizations.length > 0']")

#for x in okay:
#    print(x.find_element_by_class_name("box_title"))
    

# buttons = driver.find_elements_by_css_selector("a[ng-click='selectPage(page.number, $event)']")


#meme = driver.find_elements_by_css_selector('ng-click="selectPage(page.number, $event)"')    

#'a[ng-click='selectPage(page.number, $event)']'


