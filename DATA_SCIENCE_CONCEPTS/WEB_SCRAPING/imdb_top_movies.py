import requests as r
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

website = r.get('https://www.imdb.com/chart/top/',headers=headers).text

# print(website)


soup = bs(website,'lxml')
print(soup.find_all('h1')[0].text)
print(len(soup.find_all('p')))


