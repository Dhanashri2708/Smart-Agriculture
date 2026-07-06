from google.adk.agents import Agent
from datetime import datetime


# -----------------------------
# Market Price Tool (Mock Data)
# -----------------------------
def get_market_price(crop: str = "wheat"):
    """
    Simple market price system (static data for now)
    Later we can connect real APIs (Agmarknet etc.)
    """

    crop = crop.lower()

    prices = {
        "wheat": {"min": 2200, "max": 2600, "trend": "stable"},
        "rice": {"min": 1800, "max": 2400, "trend": "rising"},
        "maize": {"min": 1500, "max": 2100, "trend": "stable"},
        "sugarcane": {"min": 300, "max": 350, "trend": "stable"},
        "soybean": {"min": 4000, "max": 5200, "trend": "rising"},
        "cotton": {"min": 6000, "max": 7500, "trend": "falling"},
    }

    data = prices.get(crop, None)

    if not data:
        return {
            "crop": crop,
            "message": "No market data available for this crop"
        }

    return {
        "crop": crop,
        "min_price": data["min"],
        "max_price": data["max"],
        "trend": data["trend"],
        "date": str(datetime.now().date())
    }


# -----------------------------
# Market Agent (ADK)
# -----------------------------
market_agent = Agent(
    name="market_agent",
    model="gemini-2.5-flash",
    description="Provides crop market prices and selling advice for farmers.",
    instruction="""
You are a smart agricultural market advisor.

Your job:
- Give crop price ranges
- Explain market trends (rising, stable, falling)
- Help farmers decide when to sell crops
- Suggest profit-maximizing advice

Always explain in simple farming language.
""",
    tools=[get_market_price],
)