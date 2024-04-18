from dotenv import load_dotenv
load_dotenv()

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()


researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting edge research in the field of AI and Machine Learning.",
    backstory="You are an expert at a technology research group, skilled in identifying trends and analysing complex data",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="You are a content strategist known for making complex tech topics interesting and easy to understand.",
    verbose=True,
    allow_delegation=False,
)


task1 = Task(
    description="Alanyze 2024's AI advancements. Find major trends, new technologies, and their effects. Provide a detailed report.",
    expected_output="A detailed report on the major AI advancements in 2024.",
    agent=researcher,
    # output="output1.txt",
)


task2 = Task(
    description="Create a blog post about major AI advancements using your insights. Make it interesting, clear, and suited for tech enthusiasts. It should be atleast 4 parapraps long.",
    expected_output="A blog post about major AI advancements in 2024.",
    agent=writer,
    # output="output2.txt",
)


crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=2)
result = crew.kickoff()

print(result)
with open("blog.md", "a") as file:
    # Append content to the file
    file.write(result)