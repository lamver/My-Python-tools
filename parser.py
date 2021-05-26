# ############
# parser.py
# By Lamver
##############
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

print(quotes)


for quote in quotes:
    print(quote.text)


# Наконец, добавим код получения всех тегов для каждой цитаты.
# Здесь уже немного сложнее, потому что сперва нужно получить каждый внешний
# блок каждой коллекции тегов. Если этот первый шаг не выполнить,
# то теги можно будет получить, но ассоциировать их с конкретной цитатой — нет.
#
# Когда блок получен, можно опускаться ниже с помощью функции find_all для полученного подмножества.
# А уже дальше потребуется добавить внутренний цикл для завершения процесса.


for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')



# Нужно просто извлечь название элемента и его цену,
# отобразив данные в виде списка.

import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}:  {itemPrice} за {itemName}')