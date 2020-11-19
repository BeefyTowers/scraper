# Thirteen Software Solutions Ltd 2020

import urllib.request
from bs4 import BeautifulSoup
import csv

src = "https://winefolly.com/grapes/"


def get_pages(url):
    grape_urls = []
    response = urllib.request.urlopen(url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if "https://winefolly.com/grapes/" in href:
            grape_urls.append(href)
    return grape_urls


def get_flavours(page_urls):
    grapes = []
    for url in page_urls:
        response = urllib.request.urlopen(url)
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        section = soup.find("section", {"id": "flavours"})
        flavours = []
        for span in section.find_all("span"):
            flavours.append(span.text)
        title = (str(soup.title).split('|', 1)[0].strip("<title>"))
        grapes.append((title, flavours))
    return grapes


def export(data):
    with open('grape_flavour.csv', mode='w') as grape_flavour:
        writer = csv.writer(
            grape_flavour,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        for title, flavour in data:
            writer.writerow([title] + flavour)


if __name__ == "__main__":
    page_urls = get_pages(src)
    grapes = get_flavours(page_urls)
    export(grapes)
