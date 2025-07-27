import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    # Generate the response using Gemini
    response = model.generate_content(prompt)
    return response.text
