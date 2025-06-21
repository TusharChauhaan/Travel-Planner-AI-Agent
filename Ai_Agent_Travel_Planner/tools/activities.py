from langchain_core.tools import tool
import requests
import os 
from langchain_community.tools.tavily_search import TavilySearchResults
API_KEY = ""
os.environ["TAVILY_API_KEY"] = ""
class ActivityTool:

    @staticmethod
    def get_lat_lon_google(address: str):
        """Geocode address → (lat, lon) using Google Geocoding API."""
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        resp = requests.get(url, params={"address": address, "key": API_KEY}, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("results")
        if not results:
            return None
        loc = results[0]["geometry"]["location"]
        return loc["lat"], loc["lng"]

    @staticmethod
    def get_top_places(lat: float, lon: float, radius: int = 5000,
                       types: list = ["tourist_attraction", "museum", "park"],
                       max_results: int = 20):
        """Nearby Search (New) for top places using Google Places API."""
        url = "https://places.googleapis.com/v1/places:searchNearby"
        body = {
            "includedTypes": types,
            "maxResultCount": max_results,
            "locationRestriction": {
                "circle": {"center": {"latitude": lat, "longitude": lon}, "radius": radius}
            }
        }
        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.types"
        }
        resp = requests.post(url, json=body, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json().get("places", [])

    @staticmethod
    def find_top_attractions(place_name: str):
        """
        1. Geocode place_name → coords
        2. Run Nearby Search to get top attractions
        Returns list of {name}
        """
        coords = ActivityTool.get_lat_lon_google(place_name)
        if not coords:
            raise ValueError(f"Could not geocode '{place_name}'")
        lat, lon = coords
        places = ActivityTool.get_top_places(lat, lon)
        return [{"name": p["displayName"]["text"]} for p in places]

    @tool
    @staticmethod
    def recommend_activities(city: str) -> str:
        """
        Recommend popular tourist activities in a given city.

        Args:
            city (str): Name of the city to search for activities.

        Returns:
            str: A human-readable sentence listing the top activities in the city.

        Raises:
            ValueError: If the city name is invalid or no activities are found.

        Examples:
            >>> ActivityTool.recommend_activities("Paris")
            'Top activities in Paris: Eiffel Tower, Louvre Museum, Seine River Cruise'

            >>> ActivityTool.recommend_activities("UnknownCity")
            'Top activities in UnknownCity: Explore local attractions'
        """
        top_places_dict = ActivityTool.find_top_attractions(city)
        places_names = [p["name"] for p in top_places_dict]
        if not places_names:
            return f"Top activities in {city}: Explore local attractions"
        return f"Top activities in {city}: {', '.join(places_names)}"
    @tool
    def search_transportation(city: str) -> str:
        """
        Search transportation options in a city.

        Args:
            city (str): Name of the city to search for transport details.

        Returns:
            str: Transportation options like bus, metro, taxi, and car rental.
        """
        
        tavily = TavilySearchResults()
        return tavily.invoke(f"list of transportation options in {city} for tourists")
