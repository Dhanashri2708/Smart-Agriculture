from google.adk.agents import Agent


# -----------------------------
# Irrigation Decision Tool
# -----------------------------
def irrigation_advice(
    temperature: float = 30,
    humidity: float = 50,
    rain_expected: bool = False
):
    """
    Simple irrigation decision system for farmers
    """

    # If rain is expected → no irrigation
    if rain_expected:
        return {
            "irrigation_needed": False,
            "reason": "Rain is expected, so irrigation is not required",
            "advice": "Skip watering today"
        }

    # High temperature + low humidity → high water need
    if temperature > 32 and humidity < 40:
        return {
            "irrigation_needed": True,
            "reason": "High temperature and low humidity",
            "advice": "Irrigate heavily in morning or evening"
        }

    # Moderate conditions
    if 25 <= temperature <= 32:
        return {
            "irrigation_needed": True,
            "reason": "Normal temperature conditions",
            "advice": "Light irrigation recommended"
        }

    # Cool weather
    if temperature < 25:
        return {
            "irrigation_needed": False,
            "reason": "Cool weather reduces water needs",
            "advice": "Minimal or no irrigation required"
        }

    # Default fallback
    return {
        "irrigation_needed": True,
        "reason": "Default irrigation rule",
        "advice": "Check soil moisture before watering"
    }


# -----------------------------
# Irrigation Agent (ADK)
# -----------------------------
irrigation_agent = Agent(
    name="irrigation_agent",
    model="gemini-2.5-flash",
    description="Decides irrigation schedule based on weather and farming conditions.",
    instruction="""
You are an irrigation expert for farmers.

Your job:
- Decide whether irrigation is needed or not
- Save water intelligently
- Avoid irrigation if rain is expected
- Give simple farming advice

Always explain clearly in farmer-friendly language.
""",
    tools=[irrigation_advice],
)