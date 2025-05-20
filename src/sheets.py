import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import json

# Auth to Google Sheets using st.secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Allow dynamic sheet selection
def get_sheet(sheet_name="Mood Tracker"):
    try:
        st.write("Loaded credentials from secrets")  # For debugging
        sheet = client.open(sheet_name).sheet1
        return sheet
    except Exception as e:
        st.error("Could not load the Google Sheet. Check the name or sharing settings.")
        st.stop()
