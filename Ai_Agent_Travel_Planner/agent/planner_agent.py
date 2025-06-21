from langchain.chat_models import ChatOpenAI
from tools.weather import WeatherTool
from tools.hotel import HotelTool
from tools.currency import CurrencyTool
from tools.itinerary import ItineraryTool
from tools.activities import ActivityTool
from tools.visualization import VisualizationTool
from tools.summary import SummaryTool
import os
from langchain_openai import ChatOpenAI  
from langchain_groq import ChatGroq
os.environ["OPENAI_API_KEY"] = ""
llm = ChatOpenAI(model="gpt-4") 
# os.environ['GROQ_API_KEY'] = "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"
# model="deepseek-r1-distill-llama-70b"
# llm=ChatGroq(model_name=model)
tools = [
    WeatherTool.get_current_weather,
    WeatherTool.get_weather_forecast,
    HotelTool.estimate_hotel_cost,
    HotelTool.search_hotels,
    CurrencyTool.convert_currency,
    ItineraryTool.get_day_plan,
    ActivityTool.recommend_activities,
    ActivityTool.search_transportation,
    ActivityTool.search_transportation,
    VisualizationTool.plot_expenses,
    SummaryTool.generate_summary
]

llm_with_tools = llm.bind_tools(tools)
def agent_llm(state):
    from prompt import SYSTEM_PROMPT
    messages = [SYSTEM_PROMPT] + state["messages"]  # Preserve all messages

    response = llm_with_tools.invoke(messages)
    return {"messages": state["messages"] + [response]}  # Append only new response


