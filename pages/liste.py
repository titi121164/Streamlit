import streamlit as st
import requests
import pandas as pd

# URL de l'API
api_url = "  https://cfa4-35-237-200-45.ngrok-free.app/table"
API_URL = st.sidebar.text_input("Base URL")
# Appel de l'API
response = requests.get(api_url)

# Vérification de la réponse
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.title('Contenu de la table aichat')
    st.dataframe(df)
else:
    st.error("Erreur lors de la récupération des données de l'API")
