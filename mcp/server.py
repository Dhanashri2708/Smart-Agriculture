from fastapi import FastAPI
import requests

app = FastAPI(title="Smart Agriculture MCP Server")


# -----------------------------
# WEATHER TOOL (Open-Meteo)
# -----------------------------
@app.get("/weather")
def weather(latitude: float = 18.4088, longitude: float = 76.5604):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    )

    response = requests.get(url)
    data = response.json()

    current = data.get("current", {})

    return {
        "temperature": current.get("temperature_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "humidity": current.get("relative_humidity_2m")
    }


# -----------------------------
# MARKET TOOL (STATIC DATA)
# -----------------------------
@app.get("/market")
def market(crop: str = "wheat"):

    prices = {
        "wheat": {"min": 2200, "max": 2600},
        "rice": {"min": 1800, "max": 2400},
        "maize": {"min": 1500, "max": 2100},
        "soybean": {"min": 4000, "max": 5200},
    }

    return prices.get(crop.lower(), {"message": "No data available"})


# -----------------------------
# CROP TOOL
# -----------------------------
@app.get("/crop")
def crop(season: str = "monsoon"):
    if season == "monsoon":
        return ["Rice", "Sugarcane", "Maize"]
    elif season == "winter":
        return ["Wheat", "Mustard", "Gram"]
    else:
        return ["Millets", "Groundnut"]


# -----------------------------
# IRRIGATION TOOL
# -----------------------------
@app.get("/irrigation")
def irrigation(temperature: float = 30, humidity: float = 50):

    if temperature > 32 and humidity < 40:
        return {"irrigate": True, "level": "high"}

    if temperature < 25:
        return {"irrigate": False, "level": "low"}

    return {"irrigate": True, "level": "medium"}