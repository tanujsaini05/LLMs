from crewai import Crew
from crewai.process import Process
from agents_myra import booking_agent
from tasks_myra import booking_task
import streamlit as st

st.title('Myra Bot')
main_crew = Crew(
    agents = [booking_agent],
    tasks = [booking_task],
    process = Process.sequential,
)
results = main_crew.kickoff(inputs={"start_trip":"Delhi","destination":"Bhopal","Budget" : 20000,"people":2,"day":2})


from IPython.display import Markdown, display

# Path to your Markdown file


# Open and read the Markdown file
with open("availables.md", "r", encoding="utf-8") as md_file:
    content = md_file.read()

# Render and display the Markdown content in the notebook
st.text(display(Markdown(content)))

