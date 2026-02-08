import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])


st.title("AI based BMI calculator - Know your health")

name = st.text_input("Enter Your Name: ")
height = st.number_input("Enter Your Height(in cms): ")
weight = st.number_input("Enter Your Weight(in kg): ")
age = st.number_input("Enter your age: ")
gender = st.text_input("Enter youe gender: ")

bmi = round(weight/(height/100)**2,2)

st.write(f"Your BMI is: {bmi}")
prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {height}, weight as {weight}, age as {age}, gender as {gender} and BMI as {bmi}"
