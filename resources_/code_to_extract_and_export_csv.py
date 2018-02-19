from urllib.request import urlopen 
from bs4 import BeautifulSoup
from urllib.request import HTTPError

html = urlopen('https://www.batteryjunction.com/')
soup = BeautifulSoup(html, 'html.parser')

name_and_price = soup.find_all('div', {"class" : "details"})

import csv
from datetime import datetime

for item in name_and_price:
    name = item.find('h2').text
    link = item.find('a')
    link = link.get('href')
    price = item.find('div', {"class": "price"})
    price = price.text
    print(name, price, link)
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, link, datetime.now()])