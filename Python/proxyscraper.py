#!/usr/bin/python
# Required - pip install bs4

from bs4 import BeautifulSoup
import requests
import re
import sqlite3

class proxy:
    def __init__(self, ip, port, protocol, country):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.country = country

    def __str__(self):
        return "{}://{}:{}".format(self.protocol, self.ip, self.port)

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
            https = line.contents[0].output_ready(formatter='html')
            p.protocol = "https" if https == "yes" else "http"

        count += 1

    return proxylst


if __name__ == "__main__":
    lst = scrape()
    for x in lst:
        print(x)
