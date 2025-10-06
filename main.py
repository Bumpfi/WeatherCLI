import sys

from weather_call import weather_checker


def print_opening_ascii():
    """Display the WeatherCLI opening screen with ASCII art"""
    ascii_art = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗  ║
║  ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗ ║
║  ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝ ║
║  ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗ ║
║  ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║ ║
║   ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ║
║                                                              ║
║                          ████████╗██╗     ██╗                ║
║                          ██╔════╝██║     ██║                ║
║                          ██║     ██║     ██║                ║
║                          ██║     ██║     ██║                ║
║                          ╚═╝     ╚═╝     ╚═╝                ║
║                                                              ║
║                    🌤️  Powered by OpenMeteo 🌤️              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(ascii_art)
    print()


def get_weather_ascii(weather_code, is_day=True):
    """Return ASCII art for weather conditions based on weather code"""
    # Weather code mappings for OpenMeteo
    weather_art = {
        0: {  # Clear sky
            "day": """
    ☀️
 \\  |  /
  \\ | /
   \\|/
────────
   /|\\
  / | \\
 /  |  \\
""",
            "night": """
    🌙
   ✨  ✨
 ✨      ✨
   ✨  ✨
     ✨
""",
        },
        1: {  # Mainly clear
            "day": """
  ☀️  ☁️
 \\  |
  \\ |
   \\|
────────
   /|
  / |
 /  |
""",
            "night": """
   🌙  ☁️
  ✨
 ✨
   ✨
""",
        },
        2: {  # Partly cloudy
            "day": """
   ☁️ ☀️
  ☁️   ☁️
 ☁️     ☁️
   ☁️ ☁️
""",
            "night": """
   ☁️ 🌙
  ☁️   ☁️
 ☁️     ☁️
   ☁️ ☁️
""",
        },
        3: {  # Overcast
            "day": """
 ☁️☁️☁️☁️
☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️
 ☁️☁️☁️☁️
""",
            "night": """
 ☁️☁️☁️☁️
☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️
 ☁️☁️☁️☁️
""",
        },
        45: {  # Fog
            "day": """
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
""",
            "night": """
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
""",
        },
        51: {  # Light drizzle
            "day": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ・ ・ ・
・ ・ ・ ・
""",
            "night": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ・ ・ ・
・ ・ ・ ・
""",
        },
        61: {  # Light rain
            "day": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ⸚ ⸚ ⸚
⸚ ⸚ ⸚ ⸚
""",
            "night": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ⸚ ⸚ ⸚
⸚ ⸚ ⸚ ⸚
""",
        },
        71: {  # Light snow
            "day": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ❄ ❅ ❄
❅ ❄ ❅ ❄
""",
            "night": """
  ☁️☁️☁️
 ☁️☁️☁️☁️
 ❄ ❅ ❄
❅ ❄ ❅ ❄
""",
        },
        95: {  # Thunderstorm
            "day": """
  ☁️⛈️☁️
 ☁️☁️☁️☁️
  ⚡ ⚡
 ⸚ ⸚ ⸚
""",
            "night": """
  ☁️⛈️☁️
 ☁️☁️☁️☁️
  ⚡ ⚡
 ⸚ ⸚ ⸚
""",
        },
    }

    # Default to clear sky if weather code not found
    if weather_code not in weather_art:
        weather_code = 0

    period = "day" if is_day else "night"
    return weather_art[weather_code][period]


def get_weather_description(weather_code):
    """Get text description for weather code"""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Slight thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return descriptions.get(weather_code, "Unknown weather condition")


def get_yes_no_input(prompt):
    """Get yes/no input from user with validation"""
    while True:
        answer = input(f"{prompt} (yes/no): ").lower().strip()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'")


def main():
    print_opening_ascii()
    print("Welcome to WeatherCLI! 🌤️")
    print("Get current weather and forecasts for any city worldwide.")
    print()

    while True:
        try:
            # Get city name
            city = input("Enter city name (or 'quit' to exit): ").strip()

            if city.lower() in ["quit", "exit", "q"]:
                print("\nThank you for using WeatherCLI! 🌈")
                print("Stay dry and have a great day! ☀️")
                sys.exit(0)

            if not city:
                print("Please enter a valid city name.")
                continue

            print(f"\n{'=' * 50}")
            print(f"🌍 Getting weather for {city}...")
            print(f"{'=' * 50}")

            # Get current weather
            current_weather = weather_checker(city)

            if current_weather is None:
                print("❌ Could not fetch weather data. Please try again.")
                continue

            # Display ASCII art for current weather
            if (
                "current" in current_weather
                and "weather_code" in current_weather["current"]
            ):
                weather_code = current_weather["current"]["weather_code"]
                is_day = current_weather["current"].get("is_day", 1) == 1

                print("\nCurrent Weather:")
                print(get_weather_ascii(weather_code, is_day))
                print(f"Condition: {get_weather_description(weather_code)}")

                # Display additional current weather info if available
                current = current_weather["current"]
                if "wind_speed_10m" in current:
                    print(f"💨 Wind Speed: {current['wind_speed_10m']} km/h")

            print()

            # Ask if user wants to see daily forecast
            if get_yes_no_input("Would you like to see the daily forecast?"):
                print(f"\n📅 3-Day Forecast for {city}:")
                print("-" * 40)

                if "daily" in current_weather:
                    daily = current_weather["daily"]
                    dates = daily.get("time", [])
                    max_temps = daily.get("temperature_2m_max", [])
                    min_temps = daily.get("temperature_2m_min", [])
                    precipitation = daily.get("precipitation_sum", [])

                    for i in range(min(3, len(dates))):
                        date = dates[i]
                        max_temp = max_temps[i] if i < len(max_temps) else "N/A"
                        min_temp = min_temps[i] if i < len(min_temps) else "N/A"
                        precip = precipitation[i] if i < len(precipitation) else 0

                        print(f"\n📆 {date}")
                        print(f"🌡️  High: {max_temp}°C | Low: {min_temp}°C")
                        if precip > 0:
                            print(f"🌧️  Precipitation: {precip}mm")
                        else:
                            print("☀️  No precipitation expected")

            # Ask if user wants to see hourly forecast
            if get_yes_no_input("Would you like to see the hourly forecast for today?"):
                print(f"\n⏰ Today's Hourly Forecast for {city}:")
                print("-" * 45)

                if "hourly" in current_weather:
                    hourly = current_weather["hourly"]
                    times = hourly.get("time", [])
                    temps = hourly.get("temperature_2m", [])
                    precip_prob = hourly.get("precipitation_probability", [])

                    # Show next 8 hours
                    for i in range(min(8, len(times))):
                        time = times[i].split("T")[1] if "T" in times[i] else times[i]
                        temp = temps[i] if i < len(temps) else "N/A"
                        prob = precip_prob[i] if i < len(precip_prob) else 0

                        rain_icon = "🌧️" if prob > 50 else "☁️" if prob > 20 else "☀️"
                        print(f"{time}: {temp}°C {rain_icon} ({prob}% rain)")

            print("\n" + "=" * 50)

            # Ask if user wants to check another city
            if not get_yes_no_input(
                "Would you like to check weather for another city?"
            ):
                print("\nThank you for using WeatherCLI! 🌈")
                print("Stay weather-aware and have a wonderful day! ☀️")
                break

        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
