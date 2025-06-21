import requests
from datetime import datetime
from langchain_core.tools import tool
from config import OPENWEATHERMAP_API_KEY

class WeatherTool:
    """
    A collection of tools to retrieve weather data using the OpenWeatherMap API.
    Provides both current weather and 3-day forecast for a given city.
    """

    @tool
    def get_current_weather(city: str) -> str:
        """
        Retrieve the current weather for a specified city.

        Args:
            city (str): Name of the city to fetch weather for.

        Returns:
            str: A string describing the current weather and temperature in Celsius.
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        res = requests.get(url).json()
        return f"{city} weather: {res['weather'][0]['description']} at {res['main']['temp']}°C"

    @tool
    def get_weather_forecast(city: str) -> str:
        """
        Retrieve a 3-day weather forecast for a specified city.

        Args:
            city (str): Name of the city to fetch the forecast for.

        Returns:
            str: A multiline string summarizing weather for the next 3 days (one entry per 8-hour interval).
        """
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        res = requests.get(url).json()
        forecast = ""
        for i in range(0, 24, 8):
            item = res["list"][i]
            date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
            forecast += f"{date}: {item['weather'][0]['description']} at {item['main']['temp']}°C\n"
        return forecast
