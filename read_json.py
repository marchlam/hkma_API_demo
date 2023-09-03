import json
filename = 'exchange_rate.json'
currency_name = 'jpy'

f = open('data.json')

exchange_rate = json.load(f)


for i in exchange_rate['result']['records']:
    print(i['end_of_day'] + ' '+  str(i[currency_name]) )