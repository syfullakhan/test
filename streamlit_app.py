
import streamlit as st

# Title of the app
st.title("Hello Streamlit!")

# Displaying a simple text
st.write("This is a basic Streamlit app.")

# Interactive widgets
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

number = st.slider("Pick a number:", 0, 100)
st.write(f"You selected: {number}")
