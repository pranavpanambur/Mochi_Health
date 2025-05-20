from datetime import datetime
import streamlit as st

# On submit, Append to Google Sheet
def submit_mood(sheet, mood_input, user_note):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        sheet.append_row([timestamp, mood_input.split()[0], user_note])  # store only emoji
        st.success("Mood logged successfully!")
    except Exception as e:
        st.error(f"Something went wrong while logging: {e}")
