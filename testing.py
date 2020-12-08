# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:54:43 2020

@author: Jensen



    '''
        """
import requests
import json
from bs4 import BeautifulSoup
'''
page = BeautifulSoup(requests.get('http://bulletin.miami.edu/courses-az/tax/').content, 'html.parser')
courses = []

courseHeaders = page.find_all('p', class_='courseblocktitle')
for header in courseHeaders:
    info = str(header.getText()).split()
    if(len(info)>5):
        courses.append({'id': (info[0]+info[1]).replace(" ", "").replace(".", ""), 'name': " ".join(info[2:len(info)-3]).replace(".", "")})
            

print(courses)

'''
def scrapeCourseInformation(courseListing, courses):
    info = str(courseListing.getText()).split()
    if(len(info)>4):
        courses.append({'id': info[0]+info[1], 'name': " ".join(info[2:len(info)-3])})
    
         
page = BeautifulSoup(requests.get('https://catalog.ufl.edu/graduate/courses-az/computer_and_information_science_and_engineering/').content, 'html.parser')
courses = []

courseListings = page.find_all('p', class_='courseblocktitle noindent')
theCourse = courseListings[3]
# print(theCourse)
# print(f'\n text: {theCourse.getText()}')
print(f'as array: {str(theCourse.getText()).split()}')
asArray = str(theCourse.getText()).split()
name = " ".join(asArray[2:len(asArray)-2])
print(f'name: {name}')


# for courseListing in courseListings:
#         scrapeCourseInformation(courseListing, courses)
        
with open('test.txt', 'w') as outfile:
    json.dump(courses, outfile)