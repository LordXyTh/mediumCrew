import os
from urllib.parse import quote_plus

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

from urllib.parse import quote_plus

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    
    url = "https://scraping.narf.ai/api/v1/"

    response = requests.get(
        f"{url}?api_key={os.environ['FISH_API_KEY']}&url={quote_plus(website)}")
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Article Researcher',
          goal=
          'Do amazing research and summaries based on the content you are working with',
          backstory=
          "You're a researcher who goes in deep and provides amazing summaries for blog and medium articles.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)