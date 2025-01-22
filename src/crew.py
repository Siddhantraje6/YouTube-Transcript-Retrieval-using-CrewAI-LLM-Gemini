import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tools.youtube_video_search_tool import YoutubeVideoSearchTool


@CrewBase
class YoutubeAutomationAgents():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    YoutubeVideoSearchTool = YoutubeVideoSearchTool()

    @agent
    def research_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['research_manager'],
            verbose=True,
            tools=[self.YoutubeVideoSearchTool]
        )

    @task
    def research_task(self) -> Task:
	    return Task(
			config=self.tasks_config['research_task']
		)

    @crew
    def crew(self) -> Crew:
        return Crew(
		    agents=self.agents, 
		    tasks=self.tasks, 
		    verbose=True
	    )


