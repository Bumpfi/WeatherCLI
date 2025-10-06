import requests


def weather_checker(city):
    print(f"Getting Weather for {city}...")
    weather = None
    # location['lat'], location ['lon']
    location = geocode_open_meteo(city)
    if location:
        weather = get_weather_open_meteo(location["lat"], location["lon"])
        print(f"Current Temperature: {weather['current']['temperature_2m']}°C")
        print(f"Current Humidity: {weather['current']['relative_humidity_2m']}")


def get_weather_open_meteo(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "hourly": "temperature_2m,precipitation_probability",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
    }

    response = requests.get(url, params=params)
    return response.json()


def geocode_open_meteo(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and data["results"]:
            result = data["results"][0]
            return {
                "city": result["name"],
                "country": result.get("country", ""),
                "lat": result["latitude"],
                "lon": result["longitude"],
                "admin": result.get("admin1", ""),  # State/region
            }
    return None
