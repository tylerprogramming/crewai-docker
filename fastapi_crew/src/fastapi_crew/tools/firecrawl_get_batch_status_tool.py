from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from typing import List
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

import os

load_dotenv()

app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

class FireScrapeRetrieveDataToolInput(BaseModel):
    """Input schema for FireScrapeRetrieveDataToolInput."""
    id: str = Field(..., description="The id from the firecrawl batch scrape.")

class FireScrapeRetrieveDataTool(BaseTool):
    name: str = "Firescrape tool for retrieving data from a batch status id."
    description: str = (
        "This will return the data from batch scrape."
    )
    args_schema: Type[BaseModel] = FireScrapeRetrieveDataToolInput

    def _run(self, id: str) -> str:
        import requests

        api_key = os.getenv("FIRECRAWL_API_KEY")

        url = "https://api.firecrawl.dev/v1/batch/scrape/{id}"

        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

        return response.text
