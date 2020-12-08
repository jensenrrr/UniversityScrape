
# University Scrape

Scrapes the list of courses from university websites. Different universities  have different layouts and require different functionality so it is difficult to abstract this process, but the ideal for this project is to abstract it as much as possible. 

## How
### Approach
While different universities have different layouts for their course list, there are common patterns. For example: FSU, UF, and UM all have a "single nested layout". Their course homepage contains a list of subjects/areas of study and each of these areas of study links to a page where courses and course information are listed.

It appears possible to abstract single nested layouts to the point where all that would be needed are the html elements ids/class(whatever unique identifier) that contain the links and information, and a function that parses the html of a course for it's information.

It's hard to say if this is a worthwhile abstraction, however, so for now the approach is to code up each university.
### Tools
Python 3, BeautifulSoup, and requests.
