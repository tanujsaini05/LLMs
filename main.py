import google.generativeai as genai
from key import google_api_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import SequentialChain
import os
import streamlit as st

# Set the environment variable correctly

os.environ[google_api_key]=google_api_key
genai.configure(api_key=google_api_key)

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1, google_api_key=google_api_key)

def generate_chain_rest(god):
    first_prompt_template = PromptTemplate(
        template="Create the aarti of Hindu for {God}.",
        input_variables=["God"],
    )

    chain_1 = LLMChain(
        llm=llm, prompt=first_prompt_template, output_key="aarti"
    )

    chain = SequentialChain(
        chains=[chain_1],
        input_variables=["God"],
        output_variables=["aarti"],
        verbose=1
    )

    # Correctly invoke the chain with the right input variable
    response = chain.invoke({"God": god})

    return response

# Streamlit UI
st.title("Prabhu Ji")

cuisine = st.sidebar.selectbox("Pick a aarti", ("Ganesh ji", "Mahadev ji", "Radha Raman lal ji", "Ambe Bhavani", "Hanuman ji", "Khatu Shyam ji"))
if cuisine:
    response = generate_chain_rest(cuisine)
    st.header(response['aarti'].strip())
    
    # Assuming the aarti is a single string, you may not need to split it
    st.write("** Shri Aarti **")
    st.write(response)  # Display the aarti directly