import streamlit as st
from src.sheets import get_sheet
from src.mood_logger import submit_mood
from src.charting import refresh_chart, load_data, visualize_moods

# Set up the page
st.set_page_config(page_title="Mood of the Queue", layout="centered")

# Title and Intro 
st.title(" Mood of the Queue")

# Mood Logger Section
st.markdown("## Log Your Mood")

# emoji options 
mood_choices = ["😀", "😐", "😠", "😢", "😕", "🎉", "😎", "🤯", "😴", "🤔", "😭", "😍"]

mood_input = st.selectbox("How are you feeling right now?", mood_choices)
user_note = st.text_input("Any quick note you want to add?", placeholder="e.g. 'Mochi Health's assessment is fun'")

sheet = get_sheet()

if st.button("Submit Mood"):
    submit_mood(sheet, mood_input, user_note)

st.markdown("---")

refresh_chart()

df = load_data(sheet)
visualize_moods(df)
