from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools



class MediumArticleAgents():

    def research_article_agent(self):
        return Agent(
            role="The best internet researcher",
            goal="Impress everyone by finding trending articles that rank high on Google",
            backstory="""An amazing marketer with a knack for finding the latest happenings on the internet.
            Always on the lookout for the next big thing and knows exactly whats going to go viral.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
            ],
            max_iter=2
        )
    
    def article_outline_agent(self):
        return Agent(
            role="The most succinct and to the point creator of article summaries",
            goal="Impress everyone by creating an outline that will make the article a hit",
            backstory="""An amazing writer with a knack for creating the most compelling outlines.
            Writes in a way that makes it really easy and enjoyable for the writer to write a compelling, and interesting article.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
            ],
            max_iter=3

        )
    
    def article_writer_agent(self):
        return Agent(
            role="A personable, engaging writer who weaves humor and wit into their writing.",
            goal="Impress everyone by creating the most engaging article",
            backstory="""An amazing writer with a knack for creating the most compelling articles.
            Writes in a way that makes it really easy and enjoyable for the reader to read and understand the article.""",
            verbose=True,
        )