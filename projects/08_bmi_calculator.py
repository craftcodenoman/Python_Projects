import streamlit as st

# Title of the app with color
st.markdown("<h1 style='color: blue;'>BMI Calculator</h1>", unsafe_allow_html=True)

# Input fields for height and weight
weight = st.number_input("Enter your weight (kg):", min_value=0.0)
height = st.number_input("Enter your height (m):", min_value=0.0)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: <span style='color: green;'>{bmi:.2f}</span>", unsafe_allow_html=True)
        
        # Determine BMI category with color
        if bmi < 18.5:
            st.markdown("<p style='color: orange;'>You are underweight.</p>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p style='color: green;'>You have a normal weight.</p>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<p style='color: yellow;'>You are overweight.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: red;'>You are obese.</p>", unsafe_allow_html=True)
    else:
        st.error("Height must be greater than 0.")
