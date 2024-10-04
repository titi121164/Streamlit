import streamlit as st
import requests
import pandas as pd
#

# Titre centré
st.markdown(
    """
    <h1 style="text-align: center;">Historique de la FAQ sur les kimonos de karaté</h1>
    """,
    unsafe_allow_html=True
)

# URL de l'API
#api_url = "https://60c5-34-41-87-168.ngrok-free.app/table"
API_URL = st.sidebar.text_input("Base URL")
if not API_URL:
    st.sidebar.error("Veuillez entrer une URL de base.")
api_url=API_URL+'/table'
# Appel de l'API
response = requests.get(api_url)

# Vérification de la réponse
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.error("Erreur lors de la récupération des données de l'API")
