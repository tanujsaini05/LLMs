import google.generativeai as genai
from Bot.key import google_api_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import SequentialChain
import os

os.environ[google_api_key]=google_api_key
genai.configure(api_key=google_api_key)

llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.1,google_api_key = google_api_key)

first_prompt_template = PromptTemplate(
    template=" suggent me the cuisine name for {cuisine} country. just one name.",
    input_variables=["cuisine"],
)
second_prompt_template = PromptTemplate(
    template= "suggest me a menu for the {resturent_name}.",
    input_variables=["resturent_name"]
)
chain_1 = LLMChain(
    llm = llm, prompt = first_prompt_template,output_key = ["resturent_name"]
)
chain_2 = LLMChain(
    llm = llm, prompt = second_prompt_template,output_key = ["menu"]
)

chain = SequentialChain(
    chains=[chain_1, chain_2],
    input_variables = ["cuisine"],
    output_variables = ["resturent_name","menu"],
    verbose = 1
)

result = chain.invoke({"cuisine":"Indian"})
print(result)

import streamlit as st

st.title("Resturent Ji")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

