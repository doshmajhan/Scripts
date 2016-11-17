#!/usr/bin/python
# Required - pip install bs4

from bs4 import BeautifulSoup
import requests
import re
import sqlite3

class proxy:
    def __init__(self, ip, port, https, country):
        self.ip = ip
        self.port = port
        self.https = https
        self.country = country

    def toString():
        return self.ip + ':' + self.port + " " + self.https + " " + self.country

def scrape():

    proxylst = []
    count = 0
    r = requests.get("http://free-proxy-list.net/")
    page = r.text
    soup = BeautifulSoup(page, "html.parser")
    
    for line in soup.find_all('td'):

        if count == 8:
            proxylst += [p]
            p = proxy(0, 0, "", "")
            count = 0
        if count == 0:
            p = proxy(0, 0, "", "")
            p.ip = line.contents[0].output_ready(formatter='html')
        if count == 1:
            p.port = line.contents[0].output_ready(formatter='html')
        if count == 3:
            p.country = line.contents[0].output_ready(formatter='html')
        if count == 6:
            p.https = line.contents[0].output_ready(formatter='html')

        count += 1

    return proxylst

