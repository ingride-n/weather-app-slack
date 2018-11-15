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
entries = []
final_msg = location+'\n'
for i in range(4):
	entries.append(str(forecast_items[i].find('img').get('title')))
	final_msg += entries[i]+'\n'

# Create a simple webpage

file = open("CPweather.html","w")
file.write(str(panel_titles[1]))
for i in range(4):
	file.write(str(entries[i]))
file.close()

# Post forecast through a Slack app

weather_msg_CP = {'text' : final_msg}
requests.post(web_hook_url, data=json.dumps(weather_msg_CP))


