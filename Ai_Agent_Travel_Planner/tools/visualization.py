import matplotlib.pyplot as plt
import tempfile
from langchain_core.tools import tool
import os
class VisualizationTool:

    @tool
    def plot_expenses(hotel: float, food: float, transport: float, misc: float) -> str:
        """
        Generate a pie chart to visualize travel expenses across categories.

        Args:
            hotel (float): Expense amount for hotel/accommodation.
            food (float): Expense amount for food and dining.
            transport (float): Expense amount for transportation.
            misc (float): Miscellaneous expenses.

        Returns:
            str: File path to the saved pie chart image showing expense breakdown.
        """
        labels = ['Hotel', 'Food', 'Transport', 'Misc']
        sizes = [hotel, food, transport, misc]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        save_dir = "/teamspace/studios/this_studio/Travel_Planner_AI_Agent/visualization"
        os.makedirs(save_dir, exist_ok=True)  # Ensure directory exists
        save_path = os.path.join(save_dir, "graph.png")

# Save the current plot to the specified path
        plt.savefig(save_path)
        plt.close()
        return f"Expense chart saved at {tmp.name}"
