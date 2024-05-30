import streamlit as st

# Title of the app
st.title("Student Information")
title = st.text_input("Enter the student name", "Tintin")

age = st.slider("Select student Age", 0, 130, 25)

if st.button("Display Information"):
    st.write("Student's name: ",title)
    st.write("Student's age: ",age)