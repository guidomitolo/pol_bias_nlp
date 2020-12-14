from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

from time import time, sleep, strftime

import re

import pandas as pd

url = "https://www.clarin.com/economia/"

driver = "./drivers/geckodriver"
delay = 3
script = "window.scrollTo(0, document.body.scrollHeight);"

options = Options()
options.headless = True

with webdriver.Firefox(options=options, executable_path = driver ) as browser:

    browser.implicitly_wait(4)

    browser.get(url)
    print(browser.current_url)

    start = time()
    print('Start time:', strftime("%H:%M:%S"))

    n_scrolls = 0
    n_hangs = 0
    back_scroll = 0

    last_scroll_height = browser.execute_script("return document.body.scrollHeight;")

    date = []
    flyer = []
    headline = []
    body = []
    url = []

    while True:
        # count iterations
        n_scrolls += 1

        # scroll down and check full html load
        try:
            browser.execute_script(script)
            sleep(delay)
            print(n_scrolls, ' scroll(s)', ', Scroll height: ', last_scroll_height, ', Page length: ',len(browser.page_source), sep='')
            print('Last piece of news got:', browser.find_elements_by_class_name('fecha')[-1].text)
            print('------------')      
        except:
            n_hangs += 1
            if n_hangs > 3:
                print('Loading hanged up')
                break
            print('Trying to load...')
            sleep(delay * 10)

        # parse html with bs4 and avoid null elements crash
        # each time the browser is called
        try:
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            classes = ["content-nota onexone_foto list", "content-nota twoxone_foto_vertical"]
            news = soup.find_all('article', {'class': classes})

            current_scroll_height = browser.execute_script("return document.body.scrollHeight;")

            for p_news in news:
                if p_news.find(re.compile('^h[1-6]$')).text in headline:
                    pass
                else:
                    headline.append(p_news.find(re.compile('^h[1-6]$')).text)
                    date.append(p_news.findAll('p')[0].text)
                    if p_news.find('p', {'class': 'volanta'}) is not None:
                        flyer.append(p_news.find('p', {'class': 'volanta'}).text)
                    else:
                        flyer.append('')
                    body.append('')
                    url.append('https://www.clarin.com' + p_news.find('a')['href'])
            print('News collected:',len(date))
        except:
            print('Incomplete html')
            break

        # avoid scroll going backwards more than 3 times
        if current_scroll_height < last_scroll_height:
            back_scroll =+ 1
            print(f'Scroll went backward {back_scroll} time(s)') # ojo q se imprime siempre q este debajo del ultimo scroll
            if back_scroll > 3:
                print('Scroll cannot advance')
                break
        else:
            last_scroll_height = browser.execute_script("return document.body.scrollHeight;")

    end = time()
    print('End of scrolling', strftime("%H:%M:%S"))
    print('Total time:', (end - start)/60)

    browser.quit()  

    data = {
        'date': date,
        'flyer': flyer,
        'headline': headline,
        'body': body,
        'url': url
    }

    df = pd.DataFrame(data)
    df.to_csv('clarin_econ_news.csv')