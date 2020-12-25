import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

items[0].find(class_='period-name').get_text()
items[0].find(class_='short-desc').get_text()

short_descriptions = []
period_names = []
temperatures = []#ako nema na prvom onom mora jedan element ovde da se doda
				#i da preskocis prvu iteraciju u for za temp

for item in items:
	period_names.append(item.find(class_='period-name').get_text())
#print(period_names)

for item in items:
	short_descriptions.append(item.find(class_='short-desc').get_text())
#print(short_descriptions)

for item in items:
	temperatures.append(item.find(class_='temp').get_text())
#print(temperatures)

#moze i preko list comprehensiona
#period_names = [item.find(class_='period-name').get_text() for item in items]

weather_stuff = pd.DataFrame(
	{'period': period_names,
	'short_descriptions': short_descriptions,
	'temperatures': temperatures,
	})
print(weather_stuff)

weather_stuff.to_csv('weather.csv')