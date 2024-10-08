import streamlit as st
import requests
import os
# URL de l'API FastAPI
API_URL = st.sidebar.text_input("Base URL")
#
#
# Barre latérale avec une liste déroulante
option = st.sidebar.selectbox(
    'Choisissez votre modele  :',
    ('gpt-3.5-turbo', 'gpt-4')
)

st.title("FAQ kimono de karate")

 
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
 
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
 #
 # Appel à la méthode insert_data de FastAPI
   #data = {"question":prompt}
    data = {
    "question": prompt,
    "modele_ai": option  # Ajoutez votre deuxième paramètre ici
    }
    response = requests.post(API_URL+'/Insert_data', params=data)

# Affichage de la réponse
# 
    if response.json()["status"] == "ok":
       with st.chat_message("assistant"):
            retour = response.json()['reponse_openai']
            st.markdown(retour)
    else:
       st.markdown(f"Erreur lors de l'insertion : {response.json()['reponse_openai']}")
# Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": retour})
