import sys
import warnings

from final.crew import YoutubeAutomationAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    str = input("enter the topic for search: ")
    inputs = {
        'topic': str
    }
    YoutubeAutomationAgents().crew().kickoff(inputs=inputs)
