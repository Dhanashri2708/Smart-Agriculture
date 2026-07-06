from google.adk.agents import Agent
from skills.weather_skill import get_weather_data


weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Weather agent for agriculture using Open-Meteo",
    instruction="""
You are a farming weather assistant.

Always:
- Use weather skill to get real data
- Explain simply for farmers
- Suggest irrigation decisions
""",
    tools=[get_weather_data],
)