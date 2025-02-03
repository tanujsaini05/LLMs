from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
import os
from dotenv import load_dotenv
import google.generativeai as genai
from Bot.key import google_api_key

genai.configure(api_key="AIzaSyDrEux_4FBib-avY7xxna-_6lu7sfYkVZY")
load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.5,
    verbose=True,
    google_api_key = google_api_key,
)

os.environ["SERPER_API_KEY"] = os.getenv("serper_api_key")
serper = SerperDevTool()
scrape = ScrapeWebsiteTool("https://www.makemytrip.com/")


