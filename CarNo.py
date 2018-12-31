# coding : utf-8
import requests
from bs4 import BeautifulSoup
import json



data = {}
list = []
for i in range(1,11):
    html = requests.get('http://www.chepaishe.com/xiyouchepai/page/{}'.format(i)).text
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    for article in articles:
        figure = article.find_all('figure', {'class': 'thumbnail'})
        for f in figure:
            a = f.find('a')
            img = a.find('img')
            link = img['src']
            carNo = img['alt']
            data = {
                'carNo': carNo,
                'link':  link
            }
            list.append(data)
j = json.dumps(list)
print(j)





