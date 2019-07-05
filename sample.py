#!/usr/bin/env python3
import requests

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
tenki_data = requests.get(url, params=payload).json()

print(tenki_data)
