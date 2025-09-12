import streamlit as st
import base64
import openai
import os
from dotenv import load_dotenv
from googletrans import Translator
load_dotenv()
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
openai.api_key = os.getenv("OPENAI_API_KEY")

set_background("assets/borders"
".jpeg")

# --- Custom CSS for attention-grabbing style ---
st.markdown(
    """<style>

    .main {

        background: linear-gradient(135deg, #f8ffae 0%, #43c6ac 100%);

    }

    .stButton>button {

        background-color: #ff5858;

        color: white;

        font-weight: bold;

        border-radius: 8px;

        font-size: 18px;

        padding: 0.5em 2em;

        margin-top: 1em;

    }

        background: #211f1d;
        border: 2px solid #43c6ac;
        border-radius: 8px;
        color: #222 !important;
    }

    .stTextInput>div>div>input {
        background: #fffbe7;
        border: 2px solid #43c6ac;
        border-radius: 8px;
        color: #000 !important;
    }

        background: #fffbe7;
        border: 2px solid #43c6ac;
        border-radius: 8px;
        color: #222 !important;
    }

    .stSelectbox>div>div>div>div {
        background: #fffbe7;
        border: 2px solid #43c6ac;
        border-radius: 8px;
        color: #000 !important;
    }



    /* Force all label and placeholder text to black */
    .stTextInput label, .stSelectbox label, .stSelectbox span, label[data-testid="stWidgetLabel"] {
        color: #000 !important;
    }
    .stTextInput>div>div>input::placeholder {
        color: #000 !important;
        opacity: 1 !important;
    }

    </style>

    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
st.sidebar.image(
    "https://img.icons8.com/color/96/000000/idea-sharing.png",
    width=80,
)
st.sidebar.title("✨ Social Caption Genie ✨")
st.sidebar.markdown(
    """
    <span style='font-size:18px;'>Generate viral, catchy, and creative captions for all your social media platforms in seconds!</span>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown("---")
st.sidebar.info("Powered by OpenAI GPT-4o and Google Translate")

# --- Main Title ---
st.markdown("<h1 style='text-align:center; color:#fff;'>YOUR CAPTION ZONE!!✨🚀</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid #43c6ac;'>", unsafe_allow_html=True)

# --- Input Section ---
col1, col2 = st.columns([2, 1])
with col1:
    keyword = st.text_input("🔑 Enter a keyword or theme:", help="What is your post about?")
with col2:
    platform = st.selectbox("📱 Platform:", ["Instagram", "LinkedIn", "Twitter", "Facebook", "Youtube"])

col3, col4 = st.columns(2)
with col3:
    language = st.selectbox("🌐 Language:", ["English", "Hinglish", "Hindi"])
with col4:
    sentiment = st.selectbox("🎭 Sentiment:", ["Motivational", "Emotional","Poetic", "Promotional", "Sarcastic", "Thankful", "Enthusiastic", "Trendy/Slang", "Festive"])

st.markdown("<hr style='border:1px dashed #ff5858;'>", unsafe_allow_html=True)

# --- Generate Button ---
if st.button("✨ Generate AI Caption ✨"):
    if keyword:
        with st.spinner("Generating your viral caption..."):
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

            st.markdown("<h3 style='color:#43c6ac;'>🎉 Your AI-generated Caption:</h3>", unsafe_allow_html=True)
            st.success(caption)
    else:
        st.warning("Please enter a keyword or theme to generate a caption.")
