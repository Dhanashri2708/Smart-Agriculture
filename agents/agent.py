from google.adk.agents import Agent

from agents.weather_agent.agent import weather_agent
from agents.crop_agent.agent import crop_agent
from agents.irrigation_agent.agent import irrigation_agent
from agents.market_agent.agent import market_agent


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Smart agriculture coordinator",
    instruction="""
    always return only final user friendly answers.never show tool traces or logs.
You route user queries to correct agent:

Weather → weather_agent
Crop → crop_agent
Irrigation → irrigation_agent
Market → market_agent
""",
    sub_agents=[
        weather_agent,
        crop_agent,
        irrigation_agent,
        market_agent
    ],
)
