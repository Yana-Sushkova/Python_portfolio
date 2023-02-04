import requests
from bs4 import BeautifulSoup

# Парсинг курса доллара
def dollar():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[3].text
    return price

# Парсинг курса евро
def euro():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[8].text
    return price