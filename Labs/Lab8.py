import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://global.bookwalker.jp/dea38393ef-adca-4375-a5cb-8a49e75d9219/that-time-i-got-reincarnated-as-a-slime-trinity-in-tempest-3/").content

#isolating and cleaning the title value
soup = BeautifulSoup(data, 'html.parser')
d = soup.find("h1", {"itemprop":"name"})
title = d.contents[0]

#isolating and cleaning the price value
p = soup.find("p", {"class":"detail-price"})
price = p.contents[0].strip()[4:]


print("The item %s costs $%s." % (title, price))
