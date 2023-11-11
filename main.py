import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")
st.write("DateFrame")

df = pd.DataFrame({
    "一列目": [1, 2, 3, 4], 
    "２列目": [10, 20, 30, 40]
})
st.table(df.style.highlight_max(axis = 0)) 