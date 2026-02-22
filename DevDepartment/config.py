import os
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# Set your API key here (or use a .env file for production)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

# Define the Citadel's global tools
@tool('DuckDuckGoSearch')
def internet_search(search_query: str) -> str:
    """Search the web for real-time information, news, or documentation."""
    return DuckDuckGoSearchRun().run(search_query)
