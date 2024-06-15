import streamlit as st
import wolframalpha

st.title("Doubt Clearing Web App")

import openai

# OpenAI API key (replace with your actual API key)
openai_api_key = "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"

openai.api_key = openai_api_key

# Function to get responses from ChatGPT
def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=80,

    )
    return response.choices[0].text

# Input for students to upload their doubts
doubt = st.text_area("Upload your doubt:")





# Wolfram Alpha API key (replace with your actual API key)
wolfram_alpha_key = "5R49J7-J888YX9J2V"

client = wolframalpha.Client(wolfram_alpha_key)

# Function to query Wolfram Alpha and get clarifications
def get_wolfram_alpha_response(query):
    res = client.query(query)
    try:
        clarification = next(res.results).text
        return clarification
    except StopIteration:
        return "Sorry, I couldn't find a clarification."





# Button to submit the doubt
if st.button("Submit"):
    # Handle the doubt submission and retrieval of clarification here
    pass  # Placeholder for now
    if doubt:
        clarification = get_wolfram_alpha_response(doubt)
        st.write("Clarification from Wolfram Alpha:")
        st.write(clarification)

        # Use ChatGPT to provide additional explanation
        chatgpt_prompt = f"Explain further: {doubt}"
        chatgpt_response = get_chatgpt_response(chatgpt_prompt)

        st.write("Additional Explanation:")
        st.write(chatgpt_response)