import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng
from io import StringIO
import pandas as pd

st.title("Welcome to My Streamlit App")
st.write(":zap: This is a simple Streamlit application.")
st.image("../images/banner.png")

st.sidebar.title("Navigation")
st.sidebar.text_input("Search", placeholder="Type to search...")

with st.sidebar.form("sidebar_form"):
    st.write("This is a sidebar form.")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.sidebar.write(f"Hello {name}, you are {age} years old!")

with st.expander("Upload and View a File"):
    st.write("You can upload a file to view its contents.")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        data = json.loads(string_data)
        st.json(data)

with st.expander("Statistics and Visualization"): 

    df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
    st.bar_chart(df)

with st.expander("User Profile"): 
    st.write("This is a user profile section.")
    col1, col2 = st.columns(2)
    col1.text_input("First Name")
    col2.text_input("Last Name")