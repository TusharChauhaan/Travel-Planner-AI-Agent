from langchain_core.tools import tool

class SummaryTool:

    @tool
    def generate_summary(city: str, days: int, total_cost: float, currency: str) -> str:
        """
        Generate a summary for a trip, including destination, duration, and total estimated cost.

        Args:
            city (str): The travel destination city.
            days (int): The number of days the user will spend on the trip.
            total_cost (float): The total estimated cost of the trip.
            currency (str): The currency in which the cost is calculated (e.g., "USD", "INR").

        Returns:
            str: A formatted summary string of the trip.
        """
        return f"Trip Summary:\nDestination: {city}\nDuration: {days} days\nTotal Cost: {total_cost} {currency}\nBon voyage!"
