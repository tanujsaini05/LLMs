from crewai import Task
from tools_myra import serper,scrape,model
from agents_myra import booking_agent


booking_task = Task(
    description = ("""streamline the flights or trains(which ever will be the best) from {start_trip} to {destination} and hotel in {destination}.
                   you will focus on finding the cheapest flights and hotels for residence.
                   They should be properly arranged.
                   and provide links also."""),
    tools = [serper,scrape],
    agent = booking_agent,
    async_execution = True,
    expected_output = "blocks with in headings either trains,flights or hotels.",
    output_file = "availables.md" 
)