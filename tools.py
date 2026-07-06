from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

# Lazy init for Tavily client to avoid import-time failures when env is missing
def _get_tavily_client():
    try:
        from tavily import TavilyClient
    except Exception as e:
        raise ImportError("tavily package not installed. Install tavily-python. Original error: " + str(e))
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise EnvironmentError("TAVILY_API_KEY not set in environment (.env).")
    return TavilyClient(api_key=api_key)

@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information on a topic. 
    Returns Titles, URLs and snippets.
    """
    try:
        tavily = _get_tavily_client()
        results = tavily.search(
            query=query,
            max_results=5
        )
    except Exception as e:
        return f"Web search failed: {e}"

    out = []
    for r in results.get('results', []):
        out.append(
            f"Title: {r.get('title')}\n"
            f"URL: {r.get('url')}\n"
            f"Snippet: {r.get('content','')[:300]}\n"
        )
    return "\n---\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """
    Scrape and return clean text content from a given URL for deeper reading.
    """
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
