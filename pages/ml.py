import streamlit as st
with st.form("my_form"):
  st.write("my form")
  name = st.text_input("ton nom ?")
  submitted = st.form_submit_button("submit")
  if submitted:
    st.write(f"hello {name}")
