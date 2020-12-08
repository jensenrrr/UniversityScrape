# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:59:48 2020

@author: Jensen
"""
import requests
import json
from bs4 import BeautifulSoup

baseURL = 'https://m.fsu.edu'
fullURL = 'https://m.fsu.edu/default/course_catalog/index'


sourcePage = BeautifulSoup(requests.get(fullURL).content, 'html.parser')
coursePageLinks = sourcePage.find_all('a', class_='kgoui_list_item_action kgo_highlight')
coursePages = []
data= {'courses': []}

for aLink in coursePageLinks:
    if str(aLink.get('href')).find('/default/course_catalog/catalog?') != -1:
        link = baseURL + aLink.get('href')
        coursePage = BeautifulSoup(requests.get(link).content, 'html.parser')
        coursePages.append(coursePage)
    else:
        print("bad link")
    
for coursePage in coursePages:
    ids = coursePage.find_all('div', class_='kgoui_list_item_label')
    names = coursePage.find_all('span', class_='kgoui_list_item_title')
    if len(ids) == len(names):
        for i in range(len(ids)):
            data['courses'].append({
                'id': ids[i].getText().replace(" ", ""),
                'name': names[i].getText()
            })
            
            
with open('fsu.txt', 'w') as outfile:
    json.dump(data, outfile)
