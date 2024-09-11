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
pro = df.Profession.unique()
# affichage selectbox avec 1,2,3,4
# st.selectbox('Sélectionner une profession',[1,2,3,4])
#
# affichage de la liste  pro  dans selectbox
user_selection = st.selectbox('Sélectionner une profession',pro)

#
#
st.slider("Selectionner un age ",min_value=20,max_value=100,value=30,step=1)

#
st.write(df[df.Profession == user_selection])
