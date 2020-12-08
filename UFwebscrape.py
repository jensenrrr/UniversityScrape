import requests
import json
from bs4 import BeautifulSoup

URL = "https://catalog.ufl.edu/UGRD/courses/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
linkContainer = soup.find(id='aztextcontainer')
courseSections = []
data = {'courses': []}

    
for link in linkContainer.find_all('a'):
    if str(link.get('href')).find('courses') != -1:
        courseSections.append('https://catalog.ufl.edu' + str(link.get('href')))
        
for section in courseSections:
    sectionPage = requests.get(section)
    sectionSoup = BeautifulSoup(sectionPage.content, 'html.parser')
    courseListings = sectionSoup.find_all('p', class_='courseblocktitle noindent')
    for courseListing in courseListings:
            info = str(courseListing.getText()).split()
            if(len(info)>4):
                uf['courses'].append({'id': info[0]+info[1], 'name': " ".join(info[2:len(info)-3])})
            
with open('uf_undergrad.txt', 'w') as outfile:
    json.dump(uf, outfile)
    

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
