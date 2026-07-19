#!/usr/bin/env python
# coding: utf-8

# # Streamlit Day!
# 
# Today we will build User Interfaces using the Streamlit
# 

# In[ ]:





# In[1]:


import os
from dotenv import load_dotenv
from openai import OpenAI


# In[2]:


import streamlit as st # oh yeah!


# Use Streamlit Patcher to run notebooks
# 

# In[ ]:


# Or convert notebooks to script then run

# //Convert your notebook to a standard Python file
# jupyter nbconvert --to script day2streamlitnb.ipynb

# //Run the newly generated script with Streamlit
# streamlit run day2streamlitnb.py


# In[3]:


from streamlit_jupyter import StreamlitPatcher
StreamlitPatcher().jupyter()


# In[4]:


# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging
# You can choose whichever providers you like - or all Ollama

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")


# In[5]:


# Connect to OpenAI, Anthropic and Google; comment out the Gemini or Google lines if you're not using them

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)


# In[6]:


# Let's wrap a call to GPT-4.1-mini in a simple function

system_message = "You are a helpful assistant"

def message_gpt(prompt):
    messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
    return response.choices[0].message.content


# In[7]:


# This can reveal the "training cut off", or the most recent date in the training data

message_gpt("What is today's date?")


# ## User Interface time!

# In[8]:


# here's a simple function

def shout(text):
    print(f"Shout has been called with input {text}")
    return text.upper()


# In[9]:


shout("hello")


# ## User Interface time!

# In[15]:


st.title("Shout App")

# 1. Create a form container
with st.form(key="shout_form"):
    # 2. Put your text input inside the form
    text = st.text_input("Enter text")

    # 3. Use st.form_submit_button instead of st.button
    submit_button = st.form_submit_button(label="Submit")

# 4. Handle the logic outside or inside the form block
if submit_button:
    st.text_area("Result", shout(text), height=100)


# ### Authentication

# In[16]:


import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "ed" and password == "bananas":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if st.session_state.logged_in:
    st.write("Your app goes here")


# In[17]:


st.set_page_config(page_title="Shout")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Shout")
text = st.text_input("Enter text")
if text:
    st.write(text.upper())

