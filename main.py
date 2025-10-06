from weather_call import weather_checker


def main():
    print("Booting WeatherCLI powered by OpenMeteo")
    city = input("Enter city name: ")

    weather_checker(city)


if __name__ == "__main__":
    main()
