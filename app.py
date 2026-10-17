import streamlit as st
import numpy as np
from model import train

st.title(" House Price Predictor")
st.subheader("Predict the price of a house based on its area")

model = train()

st.sidebar.header("Input Features")
area = st.sidebar.slider("Select Area (in sq ft)", 500, 3000, 1000)

input_array = np.array([[area]])
prediction = model.predict(input_array)

st.write(f'### House Area: {area} sq ft')
# Safely using [0] to ensure no IndexError occurs!
st.write(f'### Estimated Price: {prediction[0]:.2f} Lakhs')