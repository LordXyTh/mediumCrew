from crewai import Crew, Process
from agents import MediumArticleAgents
from tasks import MediumArticleTasks
from dotenv import load_dotenv


class MediumCrew:

    def __init__(self, topic_area):
        self.topic_area = topic_area


    def  run(self):
        agents = MediumArticleAgents()
        tasks = MediumArticleTasks()


        research_analyst_agent = agents.research_article_agent()
        article_writer_agent = agents.article_writer_agent()


        research_analyst_task = tasks.research(research_analyst_agent, self.topic_area)
        article_writer_task = tasks.write(article_writer_agent)


        crew = Crew(
            agents=[
                research_analyst_agent,
            ],
            tasks=[
                research_analyst_task,
                
            ],
            verbose=True,
            process=Process.sequential
        )
        return crew.kickoff()
    
if __name__ == "__main__":
    load_dotenv()
    print("## Welcome to the MediumCrew ##")
    print("## Let's get started ##")
    topic_area = input("## Please enter the topic area you would like to write about ##")
    medium_crew = MediumCrew(topic_area)
    result = medium_crew.run()
    print("\n\n####################")
    print("## Crew has finished ##")
    print("## Result: ", result)
    print("####################")