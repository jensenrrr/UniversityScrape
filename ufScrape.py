# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:12:48 2020

@author: Jensen
"""


import requests
import json
from bs4 import BeautifulSoup

class UniversityOfFlorida:
    def __init__(self, name, URLs, primaryColor, secondaryColor):
        self.university = {
            "meta": {
                "name": name,
                "theme": {
                    "primary": primaryColor,
                    "secondary": secondaryColor
                    }
                },
            "courses": []
            }
        self.URLs = URLs

    def scrape(self):
        for URL in URLs:
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            linkContainer = soup.find("div", class_="az_sitemap")
            self.scrapeCoursePages(linkContainer)
            
    def scrapeCoursePages(self, linkContainer):
            for link in linkContainer.find_all('a'):
                if str(link.get('href')).find('courses') != -1:
                    sectionPage = requests.get('https://catalog.ufl.edu' + str(link.get('href')))
                    sectionSoup = BeautifulSoup(sectionPage.content, 'html.parser')
                    courseListings = sectionSoup.find_all('p', class_='courseblocktitle noindent')
                    for courseListing in courseListings:
                            self.scrapeCourseInformation(courseListing)
    
    def scrapeCourseInformation(self, courseListing):
         info = str(courseListing.getText()).split()
         if(len(info)>4):
             self.university['courses'].append({'id': info[0]+info[1], 'name': " ".join(info[2:len(info)-2])})
    
    def getUniversity(self):
        return self.university
#END CLASS                            
    
    
URLs = ["https://catalog.ufl.edu/UGRD/courses/", 'https://catalog.ufl.edu/graduate/courses-az/']
uf = UniversityOfFlorida("University of Florida", URLs, '#FA4616', '#0021A5')
uf.scrape()
university = uf.getUniversity()
with open('uf.txt', 'w') as outfile:
    json.dump(university, outfile)