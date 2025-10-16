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


movie_list = soup.find_all('div',class_='sc-ec40e84d-0 dTHKNo')
print(movie_list)
print(len(movie_list))

name = []
for i in movie_list:
    name.append(i.find('h3').text)

print(name)        


