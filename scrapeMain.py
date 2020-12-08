# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:47:11 2020

@author: Jensen
        
class SuperScrape:
    def __init__(self, URL, elementTargets):
        self.URL = URL
        self.htmlTargets = htmlTargets
        self.sourcePage = BeautifulSoup(page.content, 'html.parser')
        
    def scrapeSite(self):
        pass
    
"""
import requests
import json
from bs4 import BeautifulSoup

class University:
    def __init__(self, name, baseURL, undergradURL, gradURL, primaryColor, secondaryColor):
        self.name = name
        self.baseURL = baseURL
        self.undergradURL = undergradURL
        self.gradURL = gradURL
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        self.sourcePage = BeautifulSoup(requests.get(undergradURL).content, 'html.parser')
        self.coursePages = []
        
    def scrape(self):
        return "meme"
    
    def getCourseListPages(self, getLinks):
        if self.sourcePage is not None:
            if self.name == "University of Florida":
                courses = page.find_all('p', class_='courseblocktitle noindent')
            elif self.name == "Florida State University": 
                sections = sourcePage.find_all('a', class_='kgoui_list_item_action kgo_highlight')
                for section in sections:
                    if str(section.get('href')).find('/default/course_catalog/catalog?') != -1:
                        link = self.baseURL + section.get('href')
                        coursePage = BeautifulSoup(requests.get(link).content, 'html.parser')
                        self.coursePages.append(coursePage)
            elif self.name == "University of Miami":
                courses = page.find_all('p', class_='courseblocktitle noindent')
        else:
            print(self.name + " no source page")
    
    def getCourses(self):
        courses = []
        for page in self.coursePages:
            if self.name == "University of Florida":
                courses = page.find_all('p', class_='courseblocktitle noindent')
            elif self.name == "Florida State University": 
                courses = page.find_all('p', class_='courseblocktitle noindent')
            elif self.name == "University of Miami":
                courses = page.find_all('p', class_='courseblocktitle noindent')
        return courses
    
    def parseCourse(self):
        pass
        

        
universityData = {}

universityDict = { 
    'uf': University("University of Florida", 'https://catalog.ufl.edu','https://catalog.ufl.edu/UGRD/courses/', 'https://catalog.ufl.edu/graduate/courses-az/', '#FA4616', '#0021A5'),
    'fsu': University("Florida State University", 'https://m.fsu.edu', 'https://m.fsu.edu/default/course_catalog/index', None, '#782F40', '#CEB888'),
    'um': University("University of Miami", 'http://bulletin.miami.edu','http://bulletin.miami.edu/courses-az/', None, '#f47321', '#005030'),
}

for uni in universityDict.keys():
    universityData[uni.name] = {
     'meta': {
         'name': uni.name, 'theme': {'primary': uni.primaryColor, 'secondary': uni.secondaryColor}
    }, 'courses': [] }

        




