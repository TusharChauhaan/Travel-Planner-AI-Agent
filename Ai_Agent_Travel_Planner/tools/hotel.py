from langchain_core.tools import tool
import requests
SERP_API_KEY = ""
class HotelTool:

    @tool
    def estimate_hotel_cost(per_night: float, nights: int) -> float:
        """
        Estimate the total cost of a hotel stay based on nightly rate and number of nights.

        Args:
            per_night (float): The cost of one night's stay in the hotel.
            nights (int): The total number of nights the user plans to stay.

        Returns:
            float: The total estimated hotel cost.
        """
        return per_night * nights


    @tool
    def search_hotels(city: str, budget: int) -> str:
        """
        Search for hotels in a city under a user-defined budget using SerpAPI.

        Args:
            city (str): Destination city.
            budget (int): Maximum hotel budget in USD.

        Returns:
            str: Formatted list of hotel names with prices and sources.
        """
        query = f"best hotel in {city} under ${budget}"

        url = "https://serpapi.com/search.json"
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERP_API_KEY
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            results = response.json()

            # Extract hotels from shopping results
            hotel_results = results.get("shopping_results", [])

            if not hotel_results:
                return f"No hotels found in {city} under ${budget}."

            output_lines = []
            for hotel in hotel_results:
                title = hotel.get("title", "Unnamed Hotel")
                price = hotel.get("price", "Price not available")
                source = hotel.get("source", "Unknown source")
                rating = hotel.get("rating", "Unknown rating")
                output_lines.append(f"- **{title}** ({price}) via {source}\n  having Rating({rating})")

            return f"Top hotel options in {city} under ${budget}:\n" + "\n".join(output_lines)
        except Exception as e:
            return f"Error fetching hotel info: {str(e)}"