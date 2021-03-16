import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://global.bookwalker.jp/dea38393ef-adca-4375-a5cb-8a49e75d9219/that-time-i-got-reincarnated-as-a-slime-trinity-in-tempest-3/").content
#print(data)
soup = BeautifulSoup(data, 'html.parser')
d = soup.find("h1", {"itemprop":"name"})
title = d.contents[0]

#title = d.string.strip()
p = soup.find("p", {"class":"detail-price"})
price = p.contents[0].strip()[4:]

#price = soup.find("p", {"class":"detail-price"})
#print(type(p))

print("The item %s costs $%s." % (title, price))
