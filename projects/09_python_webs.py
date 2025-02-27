import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import io
import inflect

# Set background color
st.markdown(
    """
    <style>
    .reportview-container {
        background: #ADD8E6;  /* Light blue color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the website
st.title("Welcome to My Streamlit Website")

# Description
st.write("This is a simple website built with Streamlit in just 15 minutes!")

# Input field for user interaction
name = st.text_input("What's your name?")

# Button to submit the name
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to my website.")
    else:
        st.error("Please enter your name.")

# Display some information
st.header("About This Website")
st.write("""
    This website is created using Streamlit, a powerful library for building web applications in Python.
    You can use it to create data-driven applications quickly and easily.
""")

# Add a sidebar
# st.sidebar.header("Navigation")
# st.sidebar.write("Use this sidebar to navigate through the website.")


# 🔹 Add an Interactive Chart  
st.sidebar.subheader("Simple Data Visualization")  
chart_data = pd.DataFrame({  
    "X": range(1, 11),  
    "Y": [x**2 for x in range(1, 11)]  
})  
st.sidebar.line_chart(chart_data) 

# New Feature: File Upload
st.sidebar.header("Upload a CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data from the uploaded CSV file:")
    st.dataframe(data)

    # New Feature: Display a simple line chart
    st.line_chart(data)

# New Feature: Random Data Visualization
st.header("Random Data Visualization")
if st.button("Generate Random Data"):
    # Generate random data
    data = np.random.randn(100)
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=20, color='green', alpha=0.7)
    plt.title("Random Data Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    st.pyplot(plt)

# New Feature: Display a static image
st.header("Sample Image")
st.image("https://www.cryan.com/daily/2023/PythonCodeChrome.jpg", caption="Sample Image", use_column_width=True) 



