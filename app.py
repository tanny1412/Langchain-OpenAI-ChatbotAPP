import streamlit as st
from langchain_openai import ChatOpenAI  
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables and print the loaded API key for debugging
load_dotenv()

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(temperature=0.5)  # Assuming the API key is picked from the environment

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize conversation messages if not already present
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content="You are an AI sports assistant.")]

# Function to get responses from the chat model
def get_chatmodel_response(question):
    # Append the human message
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    # Generate the answer from the chat model
    response = chat_model.invoke(st.session_state['flowmessages'])  # Adjusted to use invoke method
    
    # Append the AI message
    st.session_state['flowmessages'].append(AIMessage(content=response.content))
    
    return response.content

# User input handling
input_question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# Display the response when the button is clicked
if submit and input_question:  # Check to ensure input is provided before processing
    response = get_chatmodel_response(input_question)
    st.subheader("The Response is")
    st.write(response)



