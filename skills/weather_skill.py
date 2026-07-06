import requests


def get_weather_data(latitude: float = 18.4088, longitude: float = 76.5604):
    """
    Direct Open-Meteo skill (used by ADK agents)
    """

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
        "humidity": current.get("relative_humidity_2m"),
    }