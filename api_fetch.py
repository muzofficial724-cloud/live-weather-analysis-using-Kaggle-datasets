import requests

def fetch_weather():
    API_KEY = '1c0f34bdeb4036bd5a3c0553c3e09ebf'
    CITY = 'Gujranwala'
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    
    response = requests.get(URL)
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"Live Temp: {temp}°C | Humidity: {humidity}%")
    return temp, humidity
