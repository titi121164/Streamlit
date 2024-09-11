import streamlit as st
import pandas as pd
#
st.title("My Dashboard TCE") 
# Lecture du fichier 
df=pd.read_csv('data.csv')


# 
#
pro = df.Profession.unique()
# affichage selectbox avec 1,2,3,4
# st.selectbox('Sélectionner une profession',[1,2,3,4])
#
# affichage de la liste  pro  dans selectbox
user_selection = st.selectbox('Sélectionner une profession',pro)

#
# affiche barre de progression demarre à 30 
age = st.slider("Selectionner un age ",min_value=20,max_value=100,value=30,step=1)

#
if st.checkbox('Afficher le jeu de donnée'):
# affichage Data Frame 
#  st.write(df)
  st.write(df[(df.Profession == user_selection) & (df.Age == age)])
#
# bouton upload file 

uploaded_file = st.file_uploader("Choose a file",type='csv')
if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
#  
liste_colonne = dataframe.columns.toliste()
selection_col = st.selectbox('Sélectionner un axe ',liste_colonne)

