from crewai import Task
from textwrap import dedent

class MediumArticleTasks():
    def research(self, agent, topic_area):
        return Task(description=dedent(f"""
                                        
            Collect and summarize trending articles, blog posts, and reddit comment threads related to the topic area: {topic_area}.                           

            Pay special attention to any things thats got people excited, or they want to learn more about,
            their sentiments and opinion opinions. Also include new release and actions being done by companies 
            or technologists.

            Your final answer MUST be a report that includes a
            comprehensive summary of the latest trends online and on social media,
            any areas that are special interest, and any notable areas which are not being covered by the media or blog articles.

            {self.__tip_section()}

            Make sure to use the most recent data as possible.

            Selected topic area: {topic_area}
            """),
            agent=agent
        )

    def outline(self, agent): 
        return Task(description=dedent(f"""
            Given the summaries from the Researcher, Identify a perspective or topic you can write about and 
            create a detailed outline for a blog post or article that a writer
            can use to write an article of over 3000 words. You may ignore summaries that dont make sense to you for the central point of your article.
            The outline should include a clear structure, main points, and
            include real world example and case studies.       

                    

            Your final outlines must be cohesive. {self.__tip_section()}

            Make sure to use the most recent data possible.
            """),
            agent=agent
        )

    def write(self, agent):
        return Task(description=dedent(f"""
            Take the outlines, and for each section, expand on the section to create a compelling article.
            The article should be at least 3000 words long and be engaging and informative.
                                       
            Your audience is on Medium where readers are technical but also enjoy a good story.
            Be funny, be witty, and be engaging.
            Use the most recent data possible.
            
            {self.__tip_section()}        
            """),
            agent=agent
        )


    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"