#import json
from bs4 import BeautifulSoup
import json
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:/Users/Jensen/chromedriver.exe", options=options)
wait = 3

def scrapeClubInfo(club):
    title = club.find("h2", class_="box-title").getText()
    info = club.find("p", class_="ng-binding").getText()
    return {
        'title': title,
        'info': info
    }

def scrapePage(page, clubsDict):
    clubDivs = page.find_all("div", class_="box_body")
    print(clubDivs)
    for clubDiv in clubDivs:
        temp = scrapeClubInfo(clubDiv)
        clubsDict[temp['title']] = temp
    return

URL = "https://orgs.studentinvolvement.ufl.edu/Organizations#!#searchresults"
driver.get(URL)
driver.implicitly_wait(3)
clubsDict = {}

i = 1
while True: 
    i = i+1
    clubs = driver.find_elements_by_css_selector("div[ng-if='organizations.length > 0']")
    for club in clubs:
        temp = scrapeClubInfo(BeautifulSoup(club.get_attribute('innerHTML'), 'html.parser'))
        clubsDict[temp['title']] = temp
    buttons = driver.find_elements_by_css_selector("a[ng-click='selectPage(page.number, $event)']")
    found = False
    for button in buttons:
        print(button.text)
        if(button.text==str(i)):
            button.click()
            found = True
            break
    if(found == False):
        print(f"Couldn't find button {str(i)}")
        break

with open('ufClubs.txt', 'w') as outfile:
    json.dump(clubsDict, outfile)

    