import streamlit as st
 
st.title("FAQ Streamlit Thierry")
 
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
 
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Send the question to OpenAI and get the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    assistant_response = response.choices.text.strip()


#response = f"Echo: {prompt}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(assistant_response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": assistant_response})
