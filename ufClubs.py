import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver

def scrapeClubInfo(club):

    title = club.find("h2", class_="box_title").getText()
    info = club.find("p", class_="ng-binding").getText()
    return {
        'title': title,
        'info': info
    }

def scrapePage(page, clubsDict):
    clubDivs = soup.find_all("div", class_="box_body")
    for clubDiv in clubDivs:
        temp = scrapeClubInfo(clubDiv)
        clubsDict[temp['title']] = temp
    return

URL = "https://orgs.studentinvolvement.ufl.edu/Organizations#!#searchresults"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
clubsDict = {}

i = 0
while True: 
    scrapePage(page, clubsDict)
    