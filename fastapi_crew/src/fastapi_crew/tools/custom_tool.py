from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

import os

load_dotenv()

app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    site: str = Field(..., description="The site we want to map out.")

class MyCustomTool(BaseTool):
    name: str = "Firecrawl site mapper"
    description: str = (
        "Maps a website with Firecrawl and returns the URLs it finds, one per line. "
        "Use it first to discover which pages of a site to scrape."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, site: str) -> str:
        # map() is the firecrawl-py v2 call; map_url() is a deprecated v1 alias.
        # It returns MapData whose links are LinkResult objects, so hand the agent plain URLs.
        map_result = app.map(url=site)

        return "\n".join(link.url for link in map_result.links)
