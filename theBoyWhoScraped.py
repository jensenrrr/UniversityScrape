# -*- coding: utf-8 -*-
"""
Generic Scrape
"""

import requests
import json
from bs4 import BeautifulSoup

class University:
    def __init__(self, name, undergradURL, gradURL, primaryColor, secondaryColor):
        self.name = name
        self.undergradURL = undergradURL
        self.gradURL = gradURL
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        
    
class ElementTarget:
    def __init__(self, elementType, elementName):
        self.elementType = elementType
        self.elementName = elementName
    
    def findAll(self):
        return "s"  
    
    def findOne(self):
        return "s"
    

class SuperScrape:
    def __init__(self, URL, elementTargets):
        self.URL = URL
        self.htmlTargets = htmlTargets
        self.sourcePage = BeautifulSoup(page.content, 'html.parser')
        
    def scrapeSite(self):
        pass
    
class SingleNestScrape(SuperScrape):
    def scrapeSite(self):
        for target in htmlTargets:
            
    

