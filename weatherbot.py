import os, json
import requests
from bs4 import BeautifulSoup

# Get the web hook url for you app

web_hook_url = '[enter url here]'

# Retrieve information from online source by webscraping

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=38.9872&lon=-76.9404#.W-sk4pNKg2w")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")

# Retrieve location information

panel_titles = soup.find_all(class_="panel-title")
location = str(panel_titles[1].get_text().strip())
print(location)

# Get forecast information

forecast_items = seven_day.find_all(class_="tombstone-container")
entry0 = forecast_items[0]
entry1 = forecast_items[1]

# Retrieve text descriptions of forecast

day_cast = str(entry0.find('img').get('title'))
night_cast = str(entry1.find('img').get('title'))

# Save information as a simple webpage

file = open("CPweather.html","w")
file.write(str(panel_titles[1]))
file.write(str(entry0))
file.write(str(entry1))
file.close()

# Post text descriptions to a Slack channel

weather_msg_CP = {'text' : location+'\n'+day_cast+'\n'+night_cast}
requests.post(web_hook_url, data=json.dumps(weather_msg_CP))
