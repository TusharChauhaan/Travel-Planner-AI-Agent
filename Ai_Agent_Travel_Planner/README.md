# 🌍 AI Travel Planner & Expense Manager ✈️💸

An intelligent multi-agent system that helps users plan trips, discover attractions, estimate expenses, and manage currency conversions using real-time APIs and tool-based reasoning.

---

## 🧠 What It Does

- 🗺️ Recommends attractions, restaurants, and activities  
- 🌦️ Provides real-time and forecast weather updates  
- 🚕 Suggests local transportation options  
- 🏨 Searches hotels within budget and estimates costs  
- 💸 Converts currency and calculates trip expenses  
- 📅 Builds personalized day-wise itineraries  
- 📊 Visualizes your expense breakdown  
- 📜 Returns a complete, well-organized travel plan  

---

## 🧱 Agent Architecture

This project uses the **ReAct (Reasoning + Acting)** pattern combined with LangGraph and LangChain tools to structure intelligent planning via multiple reasoning-tool-execution loops.

User ➡️ LLM ➡️ Tool Call ➡️ Result ➡️ Loop ➡️ Final Travel Plan

pgsql
Copy
Edit

---

## 🧰 Tools Used

| Tool Name                     | Description                                      |
|------------------------------|--------------------------------------------------|
| `search_attractions`         | Top places to visit in a city                   |
| `search_restaurants`         | Popular eateries                                |
| `search_activities`          | Fun or cultural activities                      |
| `search_transportation`      | Local transport modes                           |
| `get_current_weather`        | Real-time weather                               |
| `get_weather_forecast`       | Weather forecast                                |
| `search_hotels`              | Hotels under a budget                           |
| `estimate_hotel_cost`        | Hotel cost based on daily rate × days           |
| `add`, `multiply`            | Arithmetic helpers                              |
| `calculate_total_cost`       | Total cost calculation                          |
| `calculate_daily_budget`     | Budget/day estimator                            |
| `get_conversion_factor`      | Currency conversion rate                        |
| `convert`                    | Currency value conversion                       |
| `create_itinerary_prompt`    | Generate day-wise itinerary                     |
| `create_trip_summary`        | Generate a summary                              |
| `return_complete_travel_plan`| Final formatted plan                            |
| `plot_expenses`              | Pie chart visualization                         |

---

## 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Travel-Planner.git
cd AI-Travel-Planner
📦 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Make sure you also install:

bash
Copy
Edit
pip install -U langchain-community tavily-python
🔐 3. Set Up API Keys
Create a .env file and store your keys:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key
GOOGLE_API_KEY=your-google-api-key
SERPER_API_KEY=your-serper-api-key
TAVILY_API_KEY=your-tavily-key
🚀 4. How to Run
bash
Copy
Edit
python main.py
You can also test individual tools via .invoke():

python
Copy
Edit
from tools.activity import ActivityTool
print(ActivityTool.recommend_activities.invoke({"city": "Paris"}))
📂 5. Project Structure
bash
Copy
Edit
Travel_Planner_AI_Agent/
├── main.py
├── tools/
│   ├── activity.py
│   ├── currency.py
│   ├── hotel.py
│   ├── weather.py
│   └── visualization.py
├── prompts/
│   └── system_prompt.txt
├── visualization/
│   └── plan_chart.png
├── README.md
├── requirements.txt
└── .env
📊 6. Example Output
markdown
Copy
Edit
### ✨ Trip Summary: Kyoto for 3 Days

**Top Attractions**:  
- Fushimi Inari Shrine  
- Arashiyama Bamboo Grove  
- Kiyomizu-dera Temple  

**Hotel Cost**: $210  
**Weather Forecast**: Sunny with light showers  
**Currency**: 1 USD = 155.7 JPY  

**Daily Budget**: $60  
**Total Cost**: $390  

**Itinerary**:
- Day 1: Fushimi + local food tour  
- Day 2: Arashiyama + museums  
- Day 3: Temples + souvenir shopping  
📈 7. Visualizations
The app can generate pie charts or bar graphs for:

Hotel vs Misc Expenses

Daily Budget Allocation

Currency Conversion Breakdown

These are saved under /visualization.

✨ 8. Features at a Glance
✅ Attractions, activities & food
✅ Live weather & forecasts
✅ Hotel search with cost estimation
✅ Currency conversion
✅ Multi-step LLM planning
✅ Full markdown travel plan
✅ Visual breakdown of expenses

👨‍💻 Author
Tushar Chauhaan

🧠 Mentored by Krish Naik

📌 Future Enhancements
✈️ Flight booking APIs

📅 Calendar & reminder integrations

🧾 PDF trip exports

🗣️ Multi-language travel plans

