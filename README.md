# WeatherApp CLI

A simple command-line weather application that provides current weather information for any city using the OpenMeteo API.

## Features

- 🌡️ Current temperature display
- 💧 Humidity levels
- 🌍 Global city support with geocoding
- 🚀 Fast and lightweight
- 🔓 No API key required (uses free OpenMeteo API)

## Requirements

- Python 3.13+
- Internet connection

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd weatherapp
```

2. Install dependencies using uv (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application will prompt you to enter a city name:

```
Booting WeatherCLI powered by OpenMeteo
Enter city name: London
Getting Weather for London...
Current Temperature: 15.2°C
Current Humidity: 78
```

## How it Works

1. **Geocoding**: The app first converts the city name to geographic coordinates using OpenMeteo's geocoding API
2. **Weather Data**: Using the coordinates, it fetches current weather data from OpenMeteo's forecast API
3. **Display**: Shows the current temperature and humidity in a user-friendly format

## API Endpoints Used

- **Geocoding API**: `https://geocoding-api.open-meteo.com/v1/search`
- **Weather API**: `https://api.open-meteo.com/v1/forecast`

## Project Structure

```
weatherapp/
├── main.py           # Entry point and user interface
├── weather_call.py   # Weather API logic and data fetching
├── pyproject.toml    # Project configuration and dependencies
└── README.md         # This file
```

## Dependencies

- `requests`: HTTP library for API calls

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Weather data provided by [Open-Meteo](https://open-meteo.com/)
- Built with Python and the requests library
