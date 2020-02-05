import json
import os
import time
from urllib import request

def locationinput():
	with open('history.city.list.json') as f:
		data = json.load(f)
	city_list = []
	id_list = []
	for i in data:
		city_list.append(i["city"]["name"])
		id_list.append(i["id"])
	while True:
		location = input("please enter a valid city name: ")
		if location in city_list:
			return id_list[city_list.index(location)]
			break
		else:
			print("location invalid, check spelling, Upper case")
			print("eg: type 'Boston' rather than 'boston'")


def getweather(location):
	openweather = "http://api.openweathermap.org/data/2.5/weather?id="
	accountID = "&APPID=399fb5d0a7974b62bcc7a33a2de4d82f&units=imperial"
	Loc = str(location)
	#print(Loc)
	url = openweather + Loc + accountID
	while True:
		try:
			print("Collecting Data from openweathermap.org...")
			uh = request.urlopen(url)
			#print(uh)
			data = json.loads(uh.read().decode("utf-8"))
			print("-------- Successfully Collected --------")

			current_F = data["main"]["temp"]
			current_C = (current_F - 32)*(5/9)
			feel_F = data["main"]["feels_like"]
			feel_C = (feel_F - 32)*(5/9)
			wind_speed = data["wind"]["speed"]
			humidity = data["main"]["humidity"]
			description = data["weather"][0]["description"]
			pressure = data["main"]["pressure"]
			name = data["name"]

			current_F = round(current_F)
			current_C = round(current_C)
			feel_F = round(feel_F)
			feel_C = round(feel_C)
			wind_speed = round(wind_speed)

			print("The weather of", name, "is:\n")
			print("Current Atmosphere:", description)
			print("Current Temperature:", current_F, "deg F, ", current_C, "deg C")
			print("Feels Like:", feel_F, "deg F", feel_C, "deg C")
			print("Atmospheric Pressure:", pressure, "hPa")
			print("Humidity:", humidity, "%")
			print("Wind Speed:", wind_speed, "mph\n")

			update = input("To refresh the weather for "+name+" press ENTER;\n"+
			"For other cities, press o and ENTER; To exit, press any key and ENTER\n")
			if update == "o":
				location = locationinput()
				getweather(location)
			if len(update) == 0:
				os.system("clear")
				continue
			else:
				os.system("clear")
				break
			return 1
		except:
			print("---- Failure to Collect, openweather.org do not have information about this city:", location)
			return 0
			exit()

def weather_test(city_name):
	openweather = "http://api.openweathermap.org/data/2.5/weather?q="
	accountID = "&APPID=399fb5d0a7974b62bcc7a33a2de4d82f&units=imperial"
	url = openweather + city_name + accountID

	try:
		a = request.urlopen(url)
		return 1
	except:
		return 0

def main():
	location = locationinput()
	getweather(location)

if __name__ == '__main__':
	main()

