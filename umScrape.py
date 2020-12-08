# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:59:48 2020

@author: Jensen
"""
import requests
import json
from bs4 import BeautifulSoup

baseURL = 'http://bulletin.miami.edu'
fullURL = 'http://bulletin.miami.edu/courses-az/'

sourcePage = BeautifulSoup(requests.get(fullURL).content, 'html.parser')

coursePageLinks = sourcePage.find(id='atozindex').find_all('a')
coursePages = []
data= {'courses': []}

for aLink in coursePageLinks:
    if str(aLink.get('href')).find('/courses-az/') != -1:
        link = baseURL + aLink.get('href')
        coursePage = BeautifulSoup(requests.get(link).content, 'html.parser')
        coursePages.append(coursePage)
    else:
        print("bad link")
    
for coursePage in coursePages:
    courseHeaders = coursePage.find_all('p', class_='courseblocktitle')
    for header in courseHeaders:
        info = str(header.getText()).split()
        if(len(info)>5):
            data['courses'].append({'id': (info[0]+info[1]).replace(" ", "").replace(".", ""), 'name': " ".join(info[2:len(info)-3]).replace(".", "")})
            
            
with open('um.txt', 'w') as outfile:
    json.dump(data, outfile)
            
