import streamlit as st


st.title("Google Unit Converter")


st.sidebar.header("Select Units")
from_unit = st.sidebar.selectbox("From", ["Metre", "Centimetre"])
to_unit = st.sidebar.selectbox("To", ["Metre", "Centimetre"])


value = st.number_input("Enter the value to convert", min_value=0.0)


if from_unit == "Metre" and to_unit == "Centimetre":
    result = value * 100
elif from_unit == "Centimetre" and to_unit == "Metre":
    result = value / 100
else:
    result = value
st.write(f"Converted value: {result} {to_unit}")