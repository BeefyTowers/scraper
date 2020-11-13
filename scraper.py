# Thirteen Software Solutions Ltd 2020

import urllib.request
from bs4 import BeautifulSoup

src = "https://winefolly.com/grapes/"

def get_pages(url):
	response = urllib.request.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source, 'html.parser')
	for link in soup.find_all('a'):
		print(link.get('href'))


if __name__ == "__main__":
	get_pages(src)