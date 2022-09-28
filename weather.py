import requests,json
from decouple import config

WEATHER_API_KEY = config('WEATHER')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER}"

# 3 "https://api.open-meteo.com/v1/forecast?latitude=25.37&longitude=49.55&hourly=temperature_2m"

# 2 "https://api.openweathermap.org/data/3.0/onecall?lat="

# 1 "https://api.openweathermap.org/data/2.5/weather?"

class City:
    def __init__(self,name,lon,lat):
        self.name = name #name of the city
        self.lon = lon #longitude 
        self.lat = lat #latitude

#تكدر تعرف اي مدينة من هذا الكلاس

Hasa = City("Hasa ,IQ", "25.40768", "49.59028")

Riyadh = City("Riyadh, IQ","24.68773", "46.72185")



limit = 5
URL = BASE_URL + "lat=" + Hasa.lat + "&lon=" + Hasa.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY

# HTTP request
def getCurrentWeather():

    response = requests.get(BASE_URL)
    # checking the status code of the request
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()

        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        # print(f"{CITY:-^30}")
        # print(f"temp : {temperature} °C")
        # print(f"humind : {humidity} %")
        # print(f"prusser : {pressure} hPa")
        # print(f"report : {report[0]['description']} ")
        
        return f""" \n
        {Hasa.name:-^30} \n
        درجة الحرارة : {temperature} °C\n
        الرطوبة : {humidity} %\n
        الضغط : {pressure} hPa\n
        {report[0]['description']}
        
        """
    else:
        # showing the error message
        print("Error in the HTTP request")


# from datetime import datetime


# def sample_response(input_text):
#     user_message = str(input_text).lower()
    
#     if user_message in ('hello' , 'hi' , 'sup',):
#         return "Hey! How's it going?"
    
#     if user_message in ('who are you', 'who are you?', 'hi' , 'sup',):
#         return "I am FaisliDev_bot!"
    
    
#     if user_message in ('time', 'time?'):
#         now = datetime.datetime.now()
#         date_time = now.strftime("%d/%m/%y , %H:%M:%S")
        
        
#         return str(date_time)
    
    
#     return "I don't understands you."