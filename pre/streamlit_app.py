import streamlit as st

# to theterminal, enter the following
# streamlit run streamlit_app.py

#st.write('Hello world!')

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')