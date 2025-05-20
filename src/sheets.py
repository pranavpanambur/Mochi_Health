import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Auth to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Allow dynamic sheet selection
def get_sheet(sheet_name="Mood Tracker"):
    try:
        sheet = client.open(sheet_name).sheet1
        return sheet
    except Exception as e:
        st.error("Could not load the Google Sheet. Check the name or sharing settings.")
        st.stop()
