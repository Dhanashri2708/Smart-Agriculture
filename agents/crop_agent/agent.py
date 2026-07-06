from google.adk.agents import Agent


# -----------------------------
# Crop Recommendation Logic
# -----------------------------
def recommend_crop(season: str = "monsoon", temperature: float = 30):
    """
    Simple rule-based crop recommendation system
    (we will upgrade to AI + data later)
    """

    season = season.lower()

    if season == "monsoon":
        if temperature > 25:
            return {
                "recommended_crops": ["Rice", "Sugarcane", "Maize"],
                "reason": "Warm + monsoon climate is good for water-intensive crops"
            }
        else:
            return {
                "recommended_crops": ["Pulses", "Soybean"],
                "reason": "Cool monsoon conditions favor pulses"
            }

    elif season == "winter":
        return {
            "recommended_crops": ["Wheat", "Gram", "Mustard"],
            "reason": "Cool winter climate suitable for rabi crops"
        }

    elif season == "summer":
        return {
            "recommended_crops": ["Millets", "Groundnut", "Sunflower"],
            "reason": "Dry summer conditions need drought-resistant crops"
        }

    else:
        return {
            "recommended_crops": ["General vegetables", "Pulses"],
            "reason": "Default crop suggestion"
        }


# -----------------------------
# Crop Agent (ADK)
# -----------------------------
crop_agent = Agent(
    name="crop_agent",
    model="gemini-2.5-flash",
    description="Recommends suitable crops based on season and weather conditions for farmers.",
    instruction="""
You are an agricultural crop expert.

Your job:
- Suggest best crops for farmers
- Use season and temperature logic
- Explain in simple farming language
- Always include reason for recommendation

Be practical and farmer-friendly.
""",
    tools=[recommend_crop],
)