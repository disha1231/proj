
import requests
#import os
from datetime import datetime

api_key = '83d9cbd65407efb03a458100a2d7b5e1'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
fhand=open("weather.txt",'w')
for line in fhand:
      fhand.write("-------------------------------------------------------------")
      fhand.write ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
      fhand.write ("-------------------------------------------------------------")
      fhand.write ("Current temperature is: {:.2f} deg C".format(temp_city))
      fhand.write ("Current weather desc  :",weather_desc)
      fhand.write("Current Humidity      :",hmdt, '%')
      fhand.write ("Current wind speed    :",wind_spd ,'kmph')
fhand.close()
               
