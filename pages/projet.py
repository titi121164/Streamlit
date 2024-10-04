import streamlit as st
import requests
# URL de l'API FastAPI
API_URL = st.sidebar.text_input("Base URL")
#
#
# Barre latérale avec une liste déroulante
option = st.sidebar.selectbox(
    'Choisissez votre modele  :',
    ('gpt-3.5-turbo', 'gpt-4','sora')
)

#st.title("FAQ kimono de karate")
# URL de l'image
image_url = "https://www.google.com/imgres?q=shureido%20kimono&imgurl=https%3A%2F%2Fwww.kumasport.fr%2Fwp-content%2Fuploads%2F2020%2F03%2Fshureido-2-600x600.jpg&imgrefurl=https%3A%2F%2Fwww.kumasport.fr%2Fproduit%2Fkarate-gi-shureido-new-wave-3%2F&docid=k02nHY_JbpnUAM&tbnid=vFArV5n3KQQm9M&vet=12ahUKEwif3bzL5vSIAxV6TqQEHaRQPHMQM3oECEoQAA..i&w=600&h=600&hcb=2&ved=2ahUKEwif3bzL5vSIAxV6TqQEHaRQPHMQM3oECEoQAA"


# Titre avec image
st.markdown(
    f"""
    <h1 style="display: flex; align-items: center;">
        <img src="{image_url}" width="50" style="margin-right: 10px;">
        FAQ sur les kimonos
    </h1>
    """,
    unsafe_allow_html=True
)
 
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
