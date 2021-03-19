import requests
import json
import re
from bs4 import BeautifulSoup
import re
import pandas as pd

# titulo = [ 'A pesar del súper cepo, en octubre las reservas del Banco Central cayeron en más de U$S 1.500 millones', 'Hidrovía: el ministerio de Transporte definirá la nueva licitación', 'Estalló la guerra entre el Banco Central y Rodríguez Larreta por el impuesto sobre las Leliq que quiere cobrar el gobierno porteño', 'Dólar ahorro: en 2020 los argentinos compraron US$ 3.500 millones, el monto más bajo desde 2014', 'Cuánto deberían pagar los herederos de Diego Maradona de impuesto a la Riqueza', 'Diego Maradona tendrá una estatua en el aeropuerto de Ezeiza', 'El dólar blue bajó por sexto día consecutivo y se vendió a $ 156', 'Preocupación de las estaciones de GNC por el Plan Gas', 'Dólar hoy: a cuánto cotizan el oficial y sus diferentes tipos de cambio este viernes 27 de noviembre', 'Jubilados: declaran inconstitucional los aumentos por decreto', 'Dólar blue hoy: a cuánto cotiza este viernes 27 de noviembre', 'Cambios de hábito: la holandesa Makro invirtió $ 850 millones en Benavidez', 'El Banco Central avisó: los precios subirán por las paritarias y los descongelamientos', 'Tibia respuesta del mercado a una colocación de Guzmán en pesos', 'Economistas esperan que el plan con el FMI ayude a mejorar las expectativas', 'Supermercados: se desacelera la caída de ventas y crece la modalidad on line', 'El dólar blue bajó a $ 157 y el dólar ahorro ya cotiza a $ 142', 'Estadías más largas, alquiler de autos y compras anticipadas: los nuevos hábitos en turismo', 'Dólar: el Gobierno afloja el supercepo para intentar bajar la brecha cambiaria', 'Dólar hoy: a cuánto cotizan el oficial y sus diferentes tipos de cambio este jueves 26 de noviembre', 'Histórico: el consumo de carne aviar llega a los 50 kilos e iguala por primera vez al de carne vacuna', 'Dólar blue hoy: a cuánto cotiza este jueves 26 de noviembre', 'Maquinaria agrícola: hay un fuerte aumento en las ventas de pulverizadoras, tolvas y mixers', 'Veranito financiero: ¿Se frena la salida de los depósitos en dólares?', 'Empresarias impulsan una agenda por la igualdad', 'Ley de Fuego: el campo se siente atacado y critica el proyecto como “mamarracho”', 'La salida de Falabella del país: cuatro candidatos para comprar Sodimac', 'Sorpresa en las empresas por la postergación del aumento de la luz']
# ejemplo = 'Tras 15 años, el Indec arranca este lunes un censo a firmas, autónomos y monotributistas'

soup = BeautifulSoup(open('prueba.html', 'r').read(), 'html.parser')
classes = ["content-nota onexone_foto list", "content-nota twoxone_foto_vertical"]
news = soup.find_all('article', {'class': classes})

date = []
flyer = []
title = []
body = []
url = []

count = 0
for p_news in news:
    print(p_news.find(re.compile('^h[1-6]$')).text, type(p_news.find(re.compile('^h[1-6]$')).text))
    if p_news.find(re.compile('^h[1-6]$')).text in title:
        count =+1
    title.append(p_news.find(re.compile('^h[1-6]$')).text)
    # date.append(p_news.findAll('p')[0].text)
    # if p_news.find('p', {'class': 'volanta'}) is not None:
    #     flyer.append(p_news.find('p', {'class': 'volanta'}).text)
    # else:
    #     flyer.append('')
    # body.append('')
    # url.append('https://www.clarin.com' + p_news.find('a')['href'])

print(count)
# print(title)
# data = {
#     'date': date,
#     'flyer': flyer,
#     'title': title,
#     'body': body,
#     'url': url
# }

# print(pd.DataFrame(data))
