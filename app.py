import streamlit as st
import openai
import os
from dotenv import load_dotenv
from googletrans import Translator

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Social Media Post & Caption Generator")

keyword = st.text_input("Enter a keyword or theme:")
platform = st.selectbox("Choose platform:", ["Instagram", "LinkedIn", "Twitter", "Facebook", "Youtube"])
language = st.selectbox("Choose language:", ["English", "Hinglish", "Hindi"])
sentiment = st.selectbox("Choose sentiment:", ["Funny", "Motivational", "Emotional", "Promotional"])

if st.button("Generate AI Caption"):
    if keyword:
        with st.spinner("Generating..."):
            prompt = (
                f"You are a viral {platform} content creator. Create a {sentiment} post about '{keyword}'. "
                f"Write 2-3 catchy lines, include 6-8 trending hashtags, and 4-5 relevant emojis."
            )

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.9
            )

            caption = response.choices[0].message["content"].strip()

            if language != "English":
                translator = Translator()
                lang_code = "hi" if language == "Hindi" else "en"
                caption = translator.translate(caption, dest=lang_code).text

            st.subheader("AI-generated Caption:")
            st.write(caption)
    else:
        st.warning("Please enter a keyword!")




