from urllib.request import urlopen 
from bs4 import BeautifulSoup
from urllib.request import HTTPError
import csv
from datetime import datetime

html = urlopen('https://www.batteryjunction.com/')
soup = BeautifulSoup(html, 'html.parser')

def get_all_links():
    all_links = []
    categories = soup.find_all('ul', {"class": "categories"})
    for links in categories:
        a_tag = links.find_all('a')
        for href in a_tag:
            all_links.append(href.get('href'))
    return all_links;

def collect_data():
    links = get_all_links()
    for link in links:
        html = urlopen('https://www.batteryjunction.com/'+link)
        soup = BeautifulSoup(html, 'html.parser')
        name_and_price = soup.find_all('div', {"class" : "details"})

        for item in name_and_price:
            name = item.find('h2').text
            link = item.find('a')
            link = link.get('href')
            price = item.find('div', {"class": "price"})
            price = price.text
            print(name, price, link)
            with open('products.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([name, price, link, datetime.now()])
        
collect_data()