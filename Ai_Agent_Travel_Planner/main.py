# main.py
from langchain_core.messages import HumanMessage
from workflow.build_workflow import create_workflow
from langchain_openai import ChatOpenAI 
from IPython.display import Image, display
# from tools.activities import ActivityTool
from tools.currency import CurrencyTool
# Create workflow
app = create_workflow()

# Call with required thread_id
input = "Hi, I want to take a 5-day trip to Kyoto next month. My hotel budget is around $70 per night. I’d like to know what the weather will be like, what places I can visit, and how much the whole trip might cost. I’ll be paying in Japanese Yen, but my native currency is USD. Also, I prefer local food and public transportation. Can you plan it all for me, also use the summary tool and create visualisation using the visualization tool?"

config={"configurable": {"thread_id": "1"}}
events=app.stream(
    {"messages": [HumanMessage(content=input)]},config=config,stream_mode="values"
    )

for event in events:
    event["messages"][-1].pretty_print()



# Generate the PNG image bytes from the graph
png_data = app.get_graph().draw_mermaid_png()

# Save to file
with open("Travel_Planner_AI_Agent/workflow_graph.png", "wb") as f:
    f.write(png_data)
