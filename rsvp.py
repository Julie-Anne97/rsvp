import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file("Documents/Mariage/rsvp/rsvpmariage-3b302fac2ed3.json")

client = gspread.authorize(creds)


# Open the Google Sheet
spreadsheet_id = "1pPZtxn5rgesmWm4FZ5w6w2oVh9rOalgdJBDhN0Qou4w"  # Replace with your actual ID
spreadsheet = client.open_by_key(spreadsheet_id)
sheet = spreadsheet.worksheet("rsvp")


st.title("RSVP for Our Wedding 🎉")

# Form
with st.form(key="rsvp_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    attendance = st.radio("Will you attend?", ["Yes", "No", "Maybe"])
    guests = st.number_input("Number of Guests (including you)", min_value=1, max_value=10, value=1)
    message = st.text_area("Leave us a message (optional)")

    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Append data to Google Sheets
    sheet.append_row([name, email, attendance, guests, message])
    st.success("Thank you! Your RSVP has been recorded. 🎉")
