from crewai import Agent
from tools import *
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
import os

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose = True,
    temperature=0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY")
)
news_research_agent = Agent(
    role = "Senior Researcher",
    goal = 'uncover ground technologies in {topic}',
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curosity, you're at the forefont of "
        "innovation eager to explore and share knowledge that could change"
        "the world"
    ),
    tools = [],
    llm = model,
    allow_delegation = True


)

news_writer = Agent(
    role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[],
  llm=model,
  allow_delegation=False
)