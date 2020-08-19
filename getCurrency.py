import requests
import json
#load json conf
req = requests.get('https://www.cbr-xml-daily.ru/latest.js')
data = req.json()
#TEST PARSE
#print (data)
print("Актуальность курса: " + data['date'])
rub=input("Введите количество рублей ")
setvalute=input("Введите обозначение валюты (USD,UAH,ZAR) ")
jumbola=float(data['rates'][setvalute])*float(rub)
print(str(rub) +  " руб. стоит " + str(jumbola))

