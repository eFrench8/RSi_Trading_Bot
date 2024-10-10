#use alpha vantage to get the rsi data and work out if i should buy or sell the stock

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey='
r = requests.get(url)
data = r.json()

print(data)