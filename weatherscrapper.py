import pandas as pd
import requests
from bs4 import BeautifulSoup

#URL of the webpage i want to collect data from
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')
soup = BeautifulSoup(page.content, 'html.parser')
#Finding the data
week = soup.find(id='seven-day-forecast-body')
#Selecting and separating the daily data into a list
items = week.find_all(class_='tombstone-container')

items[0].find(class_='period-name').get_text()
items[0].find(class_='short-desc').get_text()

short_descriptions = []
period_names = []
temperatures = []

#Filling in my data into dedicated lists
for item in items:
	period_names.append(item.find(class_='period-name').get_text())

for item in items:
	short_descriptions.append(item.find(class_='short-desc').get_text())

for item in items:
	temperatures.append(item.find(class_='temp').get_text())
'''
could've done it with list comprehension
period_names = [item.find(class_='period-name').get_text() for item in items]
'''
weather_stuff = pd.DataFrame(
	{'period': period_names,
	'short_descriptions': short_descriptions,
	'temperatures': temperatures,
	})
print(weather_stuff)

weather_stuff.to_csv('weather.csv')
