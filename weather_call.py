import requests


def weather_checker(city):
    """Main function to get weather data for a city"""
    print(f"🔍 Searching for {city}...")

    # Get location coordinates
    location = geocode_open_meteo(city)
    if not location:
        print(f"❌ Could not find location for '{city}'. Please check the spelling.")
        return None

    print(f"📍 Found: {location['city']}, {location['country']} {location['admin']}")

    # Get weather data
    weather = get_weather_open_meteo(location["lat"], location["lon"])
    if not weather:
        print("❌ Could not fetch weather data.")
        return None

    # Display current weather
    if "current" in weather:
        current = weather["current"]
        print(f"\n🌡️  Current Temperature: {current.get('temperature_2m', 'N/A')}°C")
        print(f"💧 Current Humidity: {current.get('relative_humidity_2m', 'N/A')}%")

        if "wind_speed_10m" in current:
            print(f"💨 Wind Speed: {current['wind_speed_10m']} km/h")

    return weather


def get_weather_open_meteo(latitude, longitude):
    """Fetch weather data from OpenMeteo API"""
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,is_day",
        "hourly": "temperature_2m,precipitation_probability",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "past_days": 0,
        "forecast_days": 3,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("⏰ Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("🌐 Connection error. Please check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"🚫 HTTP error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error fetching weather data: {e}")
        return None


def geocode_open_meteo(city_name):
    """Convert city name to coordinates using OpenMeteo geocoding API"""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

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
        else:
            return None

    except requests.exceptions.Timeout:
        print("⏰ Geocoding request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print(
            "🌐 Connection error during geocoding. Please check your internet connection."
        )
        return None
    except requests.exceptions.HTTPError as e:
        print(f"🚫 HTTP error during geocoding: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Geocoding request failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error during geocoding: {e}")
        return None
