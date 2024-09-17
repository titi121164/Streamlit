import streamlit as st
with st.form("my_form"):
  st.write("my form")
  name = st.text_input("ton nom ?")
  submitted = st.form-submit_button("submit")
  if submitted:
    st.write(f"hello {name}")
