from langchain.tools import tool
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserTools():
    WEBDRIVER_PATH = '/Users/rizwanqaiser/Play/mediumCrew/tools/chromedriver'
    # Write a headless browser that logs into medium and scrapes the data of a paid article.
    options = Options()
    options.add_argument('--headless=new')
    self.driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)

    @tool("Scrape Medium Content")
    def scrape_and_summarize_medium(self, url):
        # login to medium
        
        self.driver.get(url)
