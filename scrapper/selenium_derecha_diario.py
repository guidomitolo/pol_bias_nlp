
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from time import time, strftime, sleep

import pandas as pd

url = "https://derechadiario.com.ar/economia"
driver = "./drivers/geckodriver"
delay = 3

options = Options()
options.headless = True
options.page_load_strategy = 'normal'

with webdriver.Firefox(executable_path = driver, options=options) as browser:

    browser.get(url)
    print('url',browser.current_url)
    
    start = time()
    print('Start time:', strftime("%H:%M:%S"))

    count=0

    while True:
        count += 1
        button = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/button')
        if button.text != 'Ver más de Economía':
            print('No more to load')
            break        
        browser.execute_script('arguments[0].scrollIntoView(true);', button)
        sleep(3)

        elements = browser.find_elements(By.TAG_NAME,'article')
        print(f'{count} page(s) loaded with {len(elements)} articles')

        button.click()
        sleep(3)
    
    # save page to parse with bs4
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    news = soup.findAll('a', {'class': 'jsx-1028219248'})
    print(f'{len(news)} articles founded')

    end = time()
    print('End of loading:', strftime("%H:%M:%S"))
    print('Total time:', (end - start)/60)

    browser.quit()

    date = []
    flyer = []
    headline = []
    lead = []
    body = []
    link = []

    # parse and classify
    for p_news in news:

        url = 'https://derechadiario.com.ar' + p_news['href']
        link.append(url)
        date.append(p_news.findAll('p')[2].text)
        headline.append(p_news.find('h1').text)
        lead.append(p_news.findAll('p')[1].text)
        flyer.append(p_news.findAll('p')[0].text)

        web = requests.get(url)
        article = BeautifulSoup(web.content, 'html.parser')
        content = article.find('div', {'class':"jsx-2701897770 editor body"})
        texto = str()
        for paragraph in content.children:
            out = ['h3', 'img', 'div']
            if paragraph.name not in out:
                try:
                    texto = texto + paragraph.text
                except:
                    pass
        body.append(texto)

    data = {
        'date': date,
        'flyer': flyer,
        'title': headline,
        'lead': lead,
        'body': body,
        'url': link
    }

    # save to a csv file
    df = pd.DataFrame(data)
    df.to_csv('derecha_econ_news.csv')
