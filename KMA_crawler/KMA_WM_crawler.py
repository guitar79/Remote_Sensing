# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:32:11 2017

@author: User
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.kma.go.kr/weather/images/satellite_basic03.jsp?prevSat=le1b&sat=le1b&dtm=&area=a&x=20&y=9&data=ir1&tm=2017.08.21&tmHour=22%3A30")

page.content
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
list(soup.children)

[type(item) for item in list(soup.children)] 

html = list(soup.children)[3]

list(html.children)


def crawler(max_pages):
  page = 1
  while page < max_pages:
    url    = TARGET + str(page) + "/"
    source = requests.get(url).text
    soup   = BeautifulSoup(source, "html.parser")
    
    for link in soup.findAll(TAGNAME, {ATTR: VALUE}):
      href = link.get(TG_ATTR)
      print(href)
      
    page += 1

crawler(5)