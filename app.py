import eda, predict, home
import streamlit as st

navigation = st.sidebar.selectbox('Navigation',['Home Page','EDA','Form Prediction'])

st.sidebar.markdown('# About')
st.sidebar.write("Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet Tweet ")

if navigation == 'EDA':
    eda.run()
elif navigation == 'Form Prediction':
    predict.run()
else:
    home.run()
