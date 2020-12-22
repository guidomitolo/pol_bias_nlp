import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.laizquierdadiario.com/Economia/"

def parse_url(url):
    response = requests.get(url)
    content = response.content
    parsed_response = BeautifulSoup(content, "html.parser")
    return parsed_response

soup = parse_url(base_url)
here = soup.find('strong', {'class':"on"})

flyer = []
headline = []
url = []

date = []
lead = []
body = []

i = 0
n_news = 0

# arbitrary stop at 300 iterations
while int(here.text) < 600:
    here = soup.find('strong', {'class':"on"})
    print(f"{i + 1}º page, articles from {int(here.text)} to {soup.find_all('a', {'class':'lien_pagination'})[i].text}")

    # strict selection
    news = soup.select("div[class=noticia]")
    n_news += len(news)
    print('News collected:', n_news)

    # parse while reading page source
    for p_news in news:
        link = base_url + p_news.find('a')['href']

        url.append(link)
        if p_news.find('h4') is not None:
            flyer.append(p_news.find('h4').text)
        else:
            flyer.append('')
        headline.append(p_news.find('a').text)

        web = requests.get(link)
        article = BeautifulSoup(web.content, 'html.parser')
        
        if article.find('div', {'class': 'header-articulo'}) is not None:
            if article.find('div', {'class': 'header-articulo'}).find('p') is not None:        
                lead.append(article.find('div', {'class': 'header-articulo'}).find('p').text)
            else:
                lead.append('')
            date.append(article.find('span', {'style': 'color: #364b67;'}).text)

            texto = str()
            for paragraph in article.find('div', {'class': 'articulo'}).findAll('p')[:-5]:
                texto = texto + paragraph.text
            body.append(texto)
        else:
            body.append('')
            date.append('')
            lead.append('')

    # go to next page
    next_pag_url = base_url + soup.find_all('a', {'class':"lien_pagination"})[i]['href']
    soup = parse_url(next_pag_url)
    if i < 5:
        i += 1
    print('------------------------------------------')

# make dict with lists
data = {
    'date': date,
    'flyer': flyer,
    'lead': lead,
    'headline': headline,
    'body': body,
    'url': url
}

# save everything to a csv file
pd.DataFrame(data).to_csv('data/izq_econ_news_2.csv')