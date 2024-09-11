import streamlit as st
import pandas as pd
#
st.title("My Dashboard TCE") 
# Lecture du fichier 
df=pd.read_csv('data.csv')

if st.checkbox('Afficher le jeu de donnée'):
# affichage Data Frame 
  st.write(df)
# 
#
st.selectbox('Sélectionner une profession',[1,2,3,4])

