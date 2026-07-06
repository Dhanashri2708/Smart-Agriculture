import os
from functools import wraps

# Store this in an environment variable in production
API_KEY = os.getenv("API_KEY", "SMART_AGRI_2026")

def verify_api_key(api_key):
    """
    Returns True if API key is valid.
    """
    return api_key == API_KEY


def require_api_key(func):
    """
    Decorator to protect functions.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        api_key = kwargs.get("api_key")

        if not verify_api_key(api_key):
            return {
                "status": "error",
                "message": "Unauthorized request"
            }

        return func(*args, **kwargs)

    return wrapper


@require_api_key
def weather_agent(query, api_key=None):
    return {
        "status": "success",
        "response": f"Weather information for: {query}"
    }


if __name__ == "__main__":

    print(weather_agent(
        query="Rain in Pune",
        api_key="SMART_AGRI_2026"
    ))

    print(weather_agent(
        query="Rain in Pune",
        api_key="WRONG_KEY"
    ))
