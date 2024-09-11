import streamlit as st
import pandas as pd
#
st.title("My Dashboard TCE") 
df=pd.read_csv('data.csv')

#
st.write(df)


