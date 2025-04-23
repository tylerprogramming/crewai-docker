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
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, site: str) -> str:
        map_result = app.map_url(url=site)

        return map_result
