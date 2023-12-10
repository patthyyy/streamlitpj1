import streamlit as st
import openai
# import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type= "password")

client = OpenAI(api_key = user_api_key)

user_input = st.text_area("Enter some text to correct:", "your text heare")
