from crewai import Agent, Task, Process, Crew
import os
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper

from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = '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'
topics = ['Data science', 'Programming', 'Python', 'Data Engineering', 'Programming tutorials', 'Philosophy of Technology']
search_tool = DuckDuckGoSearchRun()
research_tool = ArxivAPIWrapper()
llm = ChatOpenAI(model_name='gpt-4')


data_science_researcher = Agent(
    role='Data Science Researcher',
    goal='do a deep dive in the latest research and trends on AI and machine learning',
    backstory="""You're a data science expert. You have been hired to conduct research for an article on data science.
    You're passionate about technology and keep up to date with the latest trends in data science and machine learning.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[search_tool],
    max_iter=10
    )

data_science_research_task = Task(
    name='Data Science Research',
    description='do a deep dive into a specific piece of latest research and trends on AI and machine learning, especially focusing on the business applications of LLMs in 2024.',
    agent=data_science_researcher,
    expected_output='a 5000 word report on your area of research',
    
)



medium_writer = Agent(
    role='Medium Writer',
    goal='Write an article on the latest trends in data science',
    backstory="""You're a writer for Medium. You have been hired to write an article on the latest trends in data science.
    You're passionate about technology and keep up to date with the latest trends in data science and machine learning.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[search_tool]
)

planning_task = Task(
    name='Plan medium article',
    description='Take the research given to you by the data science researcher and plan a medium article that will be fun to read and also quite educational.',
    agent=medium_writer,
    expected_output='A detailed outline of the article',
)

crew = Crew(
    agents=[data_science_researcher,  medium_writer],
    tasks=[data_science_research_task, planning_task],
    tools=[search_tool, search_tool,search_tool],
    verbose=1,
    process=Process.sequential
)

result = crew.kickoff()
print(result)

