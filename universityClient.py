# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:57:07 2020

@author: Jensen
"""


import requests
import json

class University:
    def __init__(self, name, primaryColor, secondaryColor):
        self.name = name
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        
universityDict = { 
    'uf': University("University of Florida",  '#FA4616', '#0021A5'),
    'fsu': University("Florida State University", '#782F40', '#CEB888'),
    'um': University("University of Miami", '#f47321', '#005030'),
}

universityData = {}

for uni in universityDict.keys():
    universityData[universityDict[uni].name] = {
     'meta': {
         'name': universityDict[uni].name, 'theme': {'primary': universityDict[uni].primaryColor, 'secondary': universityDict[uni].secondaryColor}
    }, 'courses': [] }
    

with open('uf.txt') as json_file:
   universityData['University of Florida']['courses'] = json.load(json_file)['courses']
    
with open('fsu.txt') as json_file:
    universityData['Florida State University']['courses'] = json.load(json_file)['courses']
    
with open('um.txt') as json_file:
    universityData['University of Miami']['courses'] = json.load(json_file)['courses']

# x = requests.post('http://localhost:3000/api/university/set', json = universityData)

# print(x.text)



