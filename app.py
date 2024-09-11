import streamlit as st
import pandas as pd
#
st.title("My Dashboard TCE") 
# Lecture du fichier 
df=pd.read_csv('data.csv')

if st.checkbox('Affciher le jeu de donnée'):
# affichage Data Frame 
  st.write(df)
# 
#


