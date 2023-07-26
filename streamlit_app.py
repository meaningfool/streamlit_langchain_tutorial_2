import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

st.title('🎈 Sightseeing guide')

openai_api_key = st.sidebar.text_input("Your OpenAI API key")


def generate_response(keyword):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
  # Prompt
  template = '''You are an expert city guide. But you are also a bit quircky. So you tend to recommend sightseeing 
that are not the usual ones that any guide would recommend to a tourist visiting the city for the first time. When you 
recommend a site, you add a sentence to say why you selected it. Please recomment 3 sites for {city}.'''
  prompt = PromptTemplate(input_variables=['city'], template=template)
  prompt_query = prompt.format(city=keyword)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form(key='my_form'):
    keyword = st.text_input("Enter a keyword:")
    submitted = st.form_submit_button("OK")
    
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
       generate_response(keyword)

