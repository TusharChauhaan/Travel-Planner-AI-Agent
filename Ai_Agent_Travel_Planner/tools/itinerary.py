from langchain_core.tools import tool

class ItineraryTool:

    @tool
    def get_day_plan(city: str, days: int) -> str:
        """Suggest transportation options in the city."""
        base_activities = ["Visit museum", "Explore old town", "Try local food", "Relax at a park", "Enjoy nightlife"]
        plan = ""
        for i in range(1, days + 1):
            activity = base_activities[i % len(base_activities)]
            plan += f"Day {i}: {activity} in {city}\n"
        return plan
