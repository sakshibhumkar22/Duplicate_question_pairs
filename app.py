import streamlit as st
import healper
import joblib

model = joblib.load("model.pkl")

st.header('Duplicate Question Pairs')
st.write("Enter two questions and check if they are duplicates!")
q1 = st.text_input('Enter Question 1')
q2 = st.text_input('Enter Question 2')

if st.button('Find'):
    query = healper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
