from agents.agent import root_agent
from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("GOOGLE_API_KEY"))


def main():
    print("\n==============================")
    print(" SMART AGRICULTURE SYSTEM")
    print("==============================\n")

    print("Root Agent Loaded:", root_agent.name)
    print("System is ready to use!\n")

    print("Example queries:")
    print("- What is the weather in Latur?")
    print("- Which crop should I grow?")
    print("- Should I irrigate today?")
    print("- What is market price of wheat?\n")


if __name__ == "__main__":
    main()