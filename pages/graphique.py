import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#
#
# bouton upload file 

uploaded_file = st.file_uploader("Choose a file",type='csv')
if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    liste_colonne = dataframe.columns
    selection_col = st.selectbox('Sélectionner un axe ',liste_colonne)
  
  #  st.write(dataframe[selection_col])    
  ## Create a histogram of the 'age' column  
    cols_selected=dataframe[selection_col]    
    fig, ax = plt.subplots()
    ax.hist(cols_selected, bins=20)
    st.pyplot(fig)
