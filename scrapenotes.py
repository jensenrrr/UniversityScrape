# -*- coding: utf-8 -*-
"""
Undergrad scrape:
UF: https://catalog.ufl.edu/UGRD/courses/
    1 - Visit each category/link (A-Z list) (all on single page)
        2 - In each category -> scrape the details of each course 
        
USF: https://catalog.usf.edu/content.php?catoid=13&navoid=1570
    All courses are listed on the above link, BUT has 40 pages of these links
    if we only want ID and Title
    1 - go through page, gather each courseID and courseTitle
    2 - navigate to next page, 
    
UCF: ???
    They have like archives in pdfs.
    idk -> email them.
UT (u of tampa): http://ut.smartcatalogiq.com/Current/catalog/Course-Descriptions
    Actually perfect. All the courses in one page for easy pickings.
    
UM (University of Maimi): http://bulletin.miami.edu/courses-az/
    same as UF

FSU: https://m.fsu.edu/default/course_catalog/index
    Functionally the same as UF and UM. List of course categories with courses on each page.
"""

