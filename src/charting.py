import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Refresh Chart
def refresh_chart():
    if st.button(" Refresh Chart"):
        st.rerun()

# loading data from the sheet
def load_data(sheet):
    try:
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error("Failed to load mood data.")
        st.stop()

# Clean up and visualize
def visualize_moods(df):
    if not df.empty:
        # Clean up column names
        df.columns = [col.strip().lower() for col in df.columns]

        # Parse timestamps 
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])

        # Filter by date
        selected_date = st.date_input("Select a date", datetime.today().date())
        filtered = df[df['timestamp'].dt.date == selected_date]

        if not filtered.empty:
            mood_counts = filtered['mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']
            fig = px.bar(mood_counts, x='Mood', y='Count', title=f"Mood Trend for {selected_date}")
            st.plotly_chart(fig)
        else:
            st.info(f"No moods logged for {selected_date}.")
    else:
        st.info("No mood data found in the sheet yet.")
