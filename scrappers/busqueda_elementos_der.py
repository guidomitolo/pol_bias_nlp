import requests
import json
import re
from bs4 import BeautifulSoup
import re
import pandas as pd

soup = BeautifulSoup(open('derecha_econ_news.html', 'r'), 'html.parser')

news = soup.findAll('article')

for p_news in news:
    # print(p_news.find('h1').text)
    print(p_news.findAll('p')[1].text)

# date = []
# flyer = []
# title = []
# body = []
# url = []

# for p_news in news:
#     date.append(p_news.findAll('p')[0].text)
#     flyer.append(p_news.findAll('p')[1].text)
#     title.append(p_news.find(re.compile('^h[1-6]$')).text)
#     body.append('')
#     url.append(p_news.find('a')['href'])

# data = {
#     'date': date,
#     'flyer': flyer,
#     'title': title,
#     'body': body,
#     'url': url
# }

# print(pd.DataFrame(data))
