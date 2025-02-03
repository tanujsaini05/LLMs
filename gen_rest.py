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
def generate_chain_rest(god):
    first_prompt_template = PromptTemplate(
        template=" create the aarti of hindu for {God}.",
        input_variables=["God"],
    )
    # second_prompt_template = PromptTemplate(
    #     template= "suggest me a menu for the {resturent_name}.",
    #     input_variables=["resturent_name"]
    # )
    chain_1 = LLMChain(
        llm = llm, prompt = first_prompt_template,output_key = "aarti"
    )
    # chain_2 = LLMChain(
    #     llm = llm, prompt = second_prompt_template,output_key = "menu"
    # )

    chain = SequentialChain(
        chains=[chain_1],
        input_variables = ["God"],
        output_variables = ["aarti"],
        verbose = 1
    )
    response = chain.invoke({"cuisine":god})

    return response



import streamlit as st

st.title("Prabhu Ji")

cuisine = st.sidebar.selectbox("Pick a aarti", ("Ganesh ji", "Mahadev ji ", "Radha Raman lal  ji", "Ambe Bhavani ", "Hanuman ji","Khatu Shyam ji"))
if cuisine:
    response =generate_chain_rest(cuisine)
    st.header(response['aarti'].strip())
    menu_items = response['aarti'].strip().split(",")
    st.write("** Shri Aarti **")
    for item in menu_items:
        st.write("-", item)
