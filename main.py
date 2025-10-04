from weather_call import weather_checker


def main():
    print("Booting WeatherCLI powered by OpenMeteo")
    city = input("Enter city name: ")
    if isinstance(city, str):
        weather_checker(city)
    else:
        print("Argument must be a string!")


if __name__ == "__main__":
    main()
