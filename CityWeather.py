import requests
import datetime

while True:
    city = input("Enter a city: ")

    if city == "q" or city == "quit":
        print("Program ending.")
        break

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    location = data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
        "daily": "sunrise,sunset",
        "timezone": "auto",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph"
    }

    weather_response = requests.get(weather_url, params=weather_params)

    weather_data = weather_response.json()

    current = weather_data["current"]
    daily = weather_data["daily"]

    temperature = current["temperature_2m"]
    feels_like = current["apparent_temperature"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]
    sunrise = daily["sunrise"][0]
    sunset = daily["sunset"][0]

    # Convert sunrise and sunset times to a more readable format if needed
    converted_sunrise = datetime.datetime.fromisoformat(sunrise).strftime("%I:%M %p")
    converted_sunset = datetime.datetime.fromisoformat(sunset).strftime("%I:%M %p")
    

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    weather_code = current["weather_code"]
    conditions = weather_codes.get(weather_code, "Unknown")

    print()
    print(f"Weather for {location['name']}, {location['admin1']}")
    print(f"Conditions: {conditions}")
    print(f"Temperature: {temperature}F")
    print(f"Feels like: {feels_like}F")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} mph")
    print(f"Sunrise time: {converted_sunrise}")
    print(f"Sunset time: {converted_sunset}")
    print()