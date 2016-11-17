import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_related(track):
    results = []
    browser = webdriver.Chrome()
    browser.get('https://soundcloud.com/rlgrime/halloween-v/recommended')
    source = browser.page_source
    browser.quit()
    text = source.encode('utf-8').decode('ascii', "ignore")
    soup = BeautifulSoup(text, "html.parser")
    hrefs = soup.find_all("a", {"class": "soundTitle__title sc-link-dark"})
    for link in hrefs:
        results += [(link.text, link['href'])]
    return results

if __name__ == '__main__':
    track = 'halloween-v'
    results = get_related(track)
    for x, y in results:
        print(x, y)
