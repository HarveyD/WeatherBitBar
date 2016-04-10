#!/usr/local/bin/python

import requests
import json
from num2words import num2words

url = "api.openweathermap.org/data/2.5/weather?q=Canberra"

response = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22canberra%22)%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys");

data= json.loads(response.text)

temp=  data["query"]["results"]["channel"]["item"]["condition"]["temp"]

condition = data["query"]["results"]["channel"]["item"]["condition"]["text"]

temp = int(temp)

condition = str(condition).lower()

conditionEmoji = ""

if ("rain" in condition or "showers" in condition or "drizzle" in condition):
	conditionEmoji=":rain:"
elif ("sun" in condition or "fair" in condition or "clear" in condition):
	conditionEmoji=":sunny:"
elif ("cloud" in condition):
	conditionEmoji=":cloud:"
elif "snow" in condition:
	conditionEmoji = ":snowflake"
elif ("thunder" in condition or "tornado" in condition):
	conditionEmoji = ":zap:"

# Determine colour of the temperature
if(temp<20 ):
	colorStatus="blue"
elif (temp>20 and temp < 30):
	colorStatus = "orange"
else:
	colorStatus="red" 

# Determine emoji for condition

	conditionEmoji = ":umbrella:"
print num2words(temp)+  " degrees and " + condition + " " +  conditionEmoji + " | color = " + colorStatus