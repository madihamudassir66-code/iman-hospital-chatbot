import streamlit as st

# ==========================================================
# IMAN HOSPITAL SMART ASSISTANT - FIXED ANSWERS VERSION
# Only chatbot answers improved
# DO NOT CHANGE ANYTHING ELSE
# ==========================================================

import streamlit as st
import pandas as pd
import os

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Iman Hospital Smart Assistant",
    page_icon="🏥",
    layout="wide"
)

# ==========================================================
# FILE SETUP
# ==========================================================

file_name = "appointments.csv"

if not os.path.exists(file_name):
    df = pd.DataFrame(columns=[
        "Patient Name",
        "Age",
        "Doctor",
        "Service",
        "Date",
        "Time"
    ])
    df.to_csv(file_name, index=False)

# ==========================================================
# DATA
# ==========================================================

doctors = [
    "Dr. Syed Mudassir",
    "Dr. Nisar Fathima",
    "Dr. Ahmed Khan",
    "Dr. Sana Fatima"
]

services = [
    "General Consultation",
    "Fever Treatment",
    "Cold and Cough Treatment",
    "Blood Pressure Checkup",
    "Diabetes Consultation",
    "Heart Checkup",
    "Skin Consultation",
    "Eye Checkup",
    "ENT Consultation",
    "Orthopedic Consultation",
    "Physiotherapy",
    "Lab Tests",
    "X-Ray",
    "ECG",
    "Routine Health Checkup"
]

# ==========================================================
# CHATBOT FUNCTION (FIXED)
# ==========================================================

def get_response(question):

    q = question.lower().strip()

    # greetings
    if q in ["hi", "hello", "hey", "hii"]:
        return "Hello! Welcome to Iman Hospital. How may I help you?"

    # timings
    elif ("timing" in q or "time" in q or
          "open" in q or "close" in q or
          "hours" in q):
        return "OPD Timings: 10 AM to 5 PM"

    # fees
    elif ("fee" in q or "fees" in q or
          "cost" in q or "price" in q or
          "charge" in q):
        return "Consultation Fee: Rs.300"

    # doctors
    elif ("doctor" in q or "doctors" in q or
          "physician" in q):
        return "Available Doctors: " + ", ".join(doctors)

    # services
    elif ("service" in q or "services" in q or
          "treatment" in q or "treatments" in q):
        return "Available Services: " + ", ".join(services)

    # appointment
    elif ("appointment" in q or "book" in q or
          "booking" in q):
        return "Please use the Book Appointment page from sidebar."

    # symptoms
    elif ("fever" in q or "cold" in q or
          "cough" in q):
        return "Recommended Department: General Medicine"

    elif ("skin" in q or "rash" in q or
          "itching" in q):
        return "Recommended Department: Dermatology"

    elif ("eye" in q or "vision" in q):
        return "Recommended Department: Eye Care"

    elif ("ear" in q or "nose" in q or
          "throat" in q):
        return "Recommended Department: ENT"

    elif ("back pain" in q or "knee pain" in q or
          "joint pain" in q or "bone" in q):
        return "Recommended Department: Orthopedics"

    elif ("chest pain" in q or "heart pain" in q):
        return "URGENT: Visit Emergency Room Immediately"

    elif ("diabetes" in q or "sugar" in q):
        return "Recommended Department: Diabetes Clinic"

    elif ("bp" in q or "pressure" in q):
        return "Recommended Department: Blood Pressure Clinic"

    elif ("pregnancy" in q or "period" in q):
        return "Recommended Department: Gynecology"

    elif ("child" in q or "baby" in q):
        return "Recommended Department: Pediatrics"

    # hospital info
    elif ("location" in q or "address" in q or
          "where" in q):
        return "Iman Hospital is located in Hassan."

    else:
        return "Please describe your symptoms or ask about doctors, timings, fees, services or appointments."

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🏥 Iman Hospital")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Smart Chatbot",
        "Book Appointment",
        "View Appointments"
    ]
)

# ==========================================================
# HOME
# ==========================================================

if page == "Home":

    st.title("🏥 Iman Hospital Smart Assistant")
    st.write("Use sidebar to navigate.")

# ==========================================================
# SMART CHATBOT
# ==========================================================

elif page == "Smart Chatbot":

    st.title("🤖 Smart Hospital Chatbot")

    st.write("Ask any question below:")

    question = st.text_input(
        "Type your question here:",
        key="chat_input_box"
    )

    if st.button("Send", key="send_btn"):

        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            answer = get_response(question)
            st.success(answer)

# ==========================================================
# BOOK APPOINTMENT
# ==========================================================

elif page == "Book Appointment":

    st.title("📅 Book Appointment")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 120, 25)

    doctor = st.selectbox(
        "Choose Doctor",
        doctors
    )

    service = st.selectbox(
        "Choose Service",
        services
    )

    date = st.date_input("Appointment Date")
    time = st.time_input("Appointment Time")

    if st.button("Confirm Booking"):

        if name.strip() == "":
            st.error("Enter patient name.")

        else:
            new_data = pd.DataFrame([{
                "Patient Name": name,
                "Age": age,
                "Doctor": doctor,
                "Service": service,
                "Date": str(date),
                "Time": str(time)
            }])

            old_data = pd.read_csv(file_name)

            final_data = pd.concat(
                [old_data, new_data],
                ignore_index=True
            )

            final_data.to_csv(
                file_name,
                index=False
            )

            st.success("Appointment Booked Successfully!")

# ==========================================================
# VIEW APPOINTMENTS
# ==========================================================

elif page == "View Appointments":

    st.title("📋 Saved Appointments")

    data = pd.read_csv(file_name)

    st.dataframe(
        data,
        use_container_width=True
    )