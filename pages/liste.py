import streamlit as st
import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('demo.db')
c = conn.cursor()

# Lecture des données de la table 'toto'
query = "SELECT * FROM aichat"
df = pd.read_sql_query(query, conn)

# Affichage des données avec Streamlit
st.title('Contenu de la table aichat')
st.dataframe(df)

# Fermeture de la connexion
conn.close()
