# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title= 'TWITTER TWEETS',
    layout= 'wide',
    initial_sidebar_state='expanded'
)

def run():
    # create title
    st.title('Media Social Twitter')

    st.image('https://cdn.analyticsvidhya.com/wp-content/uploads/2018/07/performing-twitter-sentiment-analysis1.jpg'
             ,caption='Free Speech')
    
    st.markdown('---')
    
    # add description
    
    container = st.container(border=True)
    container.write('Welcome to our website dedicated to predict tweet category on twitter')
    st.write("## Backgorund")
    container = st.container(border=True)
    container.write("In today's world, people can easily express their opinions on social media. Therefore, as a company operating in the social media sector, specifically Twitter, we want to identify and classify tweets posted by Twitter users into three categories: neutral, positive, and negative. We aim to do this because it is observed that some people misuse the platform to tweet hateful content __[source](https://news.detik.com/berita/d-2830824/duel-di-depan-istora-senayan-karena-twitwar-ini-klarifikasi-redinparis)__. Twitter is trying to tackle this problem. Hence, we will attempt to create a robust NLP-based classification model to distinguish negative tweets and block such tweets, and if necessary, block the accounts that post these negative tweets.")
    st.write("## Objective")
    container = st.container(border=True)
    container.write("The main objective of this project is to develop an NLP-based classification model aimed at predicting neutral, negative, and positive tweets based on the given dataset. The method used will be a Recurrent Neural Network (RNN). Model evaluation will be conducted using the accuracy metric to determine whether the model is a good fit, underfit, or overfit, which will then facilitate its application for predictive purposes.")
    container = st.container(border=True)

if __name__ == '__main__':
    run()