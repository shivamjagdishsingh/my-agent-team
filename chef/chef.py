from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()


chef = Agent(
    role="Senior Chef",
    goal="Create a new recipe using the ingredients provided.",
    backstory="You are an expert chef, skilled in making combinations of ingredients to create delicious dishes.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)

tester = Agent(
    role="Customer",
    goal="You are the customer who wants to order food from the restaurant. You want to try spicy indian food.",
    backstory="You love to taste new food items and want to try something spicy today.",
    verbose=True,
    allow_delegation=False,
)

task1 = Task(
    description="Find required ingredients and create a new recipe using them. Also provide the reciepe for the dish.",
    expected_output="An exotic Indian dish, with ingredients and recipe.",
    agent=chef,
)


task3 = Task(
    description="Order food from the restaurant and provide feedback on the taste",
    expected_output="Check if food is indian, spicy, tasty and upto the mark.",
    agent=tester,
)


crew = Crew(agents=[chef, tester], tasks=[task1, task3], verbose=2)
result = crew.kickoff()

print(result)

with open("chef_output.md", "a") as file:
    # Append content to the file
    file.write(result)