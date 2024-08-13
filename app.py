import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title of the web app
st.title("Anemia Prediction")

# Input fields for the features
red_pixel = st.text_input("Red Pixel %", "")
green_pixel = st.text_input("Green Pixel %", "")
blue_pixel = st.text_input("Blue Pixel %", "")
hb = st.text_input("Hb", "")

# Ensure that all inputs are provided
if st.button("Predict"):
    if red_pixel and green_pixel and blue_pixel and hb:
        try:
            # Convert inputs to float and create a feature array
            features = np.array([[float(red_pixel), float(green_pixel), float(blue_pixel), float(hb)]])
            # Make prediction
            prediction = model.predict(features)
            output = prediction[0]
            
            # Display the prediction result
            st.success(f"The result is: {'Anaemic' if output == 1 else 'Not Anaemic'}")
        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")
    else:
        st.error("Please provide all input values.")

