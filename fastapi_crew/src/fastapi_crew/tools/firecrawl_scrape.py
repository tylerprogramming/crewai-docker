from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from typing import List
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

import os

load_dotenv()

app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

class FireScrapeToolInput(BaseModel):
    """Input schema for FireScrapeToolInput."""
    site: str = Field(..., description="The site we want to scrape.")

class FireScrapeTool(BaseTool):
    name: str = "Firescrape tool for scraping a URL"
    description: str = (
        "This will scrape the url."
    )
    args_schema: Type[BaseModel] = FireScrapeToolInput

    def _run(self, site: str):
        import requests

        api_key = os.getenv("FIRECRAWL_API_KEY")

        import requests

        url = "https://api.firecrawl.dev/v1/scrape"

        payload = {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "waitFor": 1000,
            "mobile": False,
            "skipTlsVerification": False,
            "timeout": 30000,
            "location": {"country": "US"},
            "blockAds": True,
            "url": site
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

        return response.text
