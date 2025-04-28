import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def display_weather(weather):
    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['description'].title()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    api_key = "bb2f790ba0e26fcad93c50af47bc6ab1"
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)
