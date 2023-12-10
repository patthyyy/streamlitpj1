import streamlit as st
import openai
# import openai
import json
import pandas as pd

st.title('Quickstart App')

user_api_key = st.sidebar.text_input("OpenAI API key", type= "password")

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the tree key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
