url = "https://derechadiario.com.ar/economia/regreso-el-rulo-y-el-pure-para-proteger-el-sueldo-de-la-inflacion"

# url = "https://derechadiario.com.ar/economia/en-el-primer-ano-de-alberto-fernandez-se-perdieron-mas-de-223-000-empleos-en-el-sector-privado"

# jsx-2701897770 editor body


import requests
from bs4 import BeautifulSoup

web = requests.get(url)


print(web)

soup = BeautifulSoup(web.content, 'html.parser')
article = soup.find('div', {'class':"jsx-2701897770 editor body"})
print(article.text)