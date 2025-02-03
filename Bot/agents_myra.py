from crewai import Agent
from tools_myra import serper,scrape
from tools_myra import model


booking_agent = Agent(
    role = "Booking Specialist",
    goal = "Streamline a flights or trains (which ever will be the best)from {start_trip} to {destination} and hotels in {destination} for  with minimal hassle in {Budget} for {people} people with {day} stay. ",
    backstory = ("""You are skilled in finding the best deals and securing bookings quickly at cheapest."""),
    memory = True,
    allow_deligation = True,
    verbose = True,
    tools = [serper,scrape],
    llm = model)