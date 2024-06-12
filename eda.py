import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import plotly.express as px
import nltk

# Download NLTK data
nltk.download('punkt')

# Load your data into a DataFrame
df_eda = pd.read_csv('Tweets.csv')

def run():
    # Streamlit app
    st.title('Exploratory Data Analysis (EDA) of Tweet Sentiment Dataset')

    # Display distribution of tweet sentiments
    st.subheader('Tweet Type Distribution')


    # Select options
    options = [
        "Bar Chart","Pie Chart"
    ]

    # Selectbox for visualization selection
    selected_option = st.selectbox('Select Visualization', options)

    # Display selected visualization
    if selected_option == "Bar Chart":
        # Countplot using Plotly
        sentiment_count = df_eda['sentiment'].value_counts().reset_index()
        sentiment_count.columns = ['sentiment', 'count']
        fig_bar = px.bar(sentiment_count, x='sentiment', y='count', color='sentiment', title="Distribution of Tweet Sentiments")
        st.plotly_chart(fig_bar)
        
        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            The data appears to be balanced. There are 11,117 neutral tweets, accounting for 40.5% of the dataset, followed by 8,582 positive tweets, accounting for 31.2%, and 7,781 negative tweets, accounting for 28.3%.
        ''')
    elif selected_option == "Pie Chart":    
        # Pie chart using Plotly
        sentiment_count = df_eda['sentiment'].value_counts().reset_index()
        sentiment_count.columns = ['sentiment', 'count']
        fig_pie = px.pie(sentiment_count, values='count', names='sentiment', title="Proportion of Tweet Sentiments")
        st.plotly_chart(fig_pie)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            The data appears to be balanced. There are 11,117 neutral tweets, accounting for 40.5% of the dataset, followed by 8,582 positive tweets, accounting for 31.2%, and 7,781 negative tweets, accounting for 28.3%.
        ''')
    # Sample tweets
    st.markdown('---')
    st.subheader('Sample Tweets')

    sample_neutral = df_eda[df_eda['sentiment'] == 'neutral'].sample(n=3)
    sample_positive = df_eda[df_eda['sentiment'] == 'positive'].sample(n=3)
    sample_negative = df_eda[df_eda['sentiment'] == 'negative'].sample(n=3)

    st.markdown('---')
    st.write('**Neutral Tweets:**')
    for tweet in sample_neutral['text']:
        st.write(tweet)

    st.markdown('---')
    st.write('**Positive Tweets:**')
    for tweet in sample_positive['text']:
        st.write(tweet)

    st.markdown('---')
    st.write('**Negative Tweets:**')
    for tweet in sample_negative['text']:
        st.write(tweet)

    # Create and display WordCloud for all tweets
    st.markdown('---')
    st.subheader('Word Cloud of All Tweets')

    # Make sure all text values are strings and handle NaN values
    df_eda['text'] = df_eda['text'].astype(str).fillna('')

    text_all = " ".join(df_eda['text'].values)

    cloud_all = WordCloud(
        background_color='white',
        colormap="cool",
        collocations=False,
        width=2000,
        height=1000
    ).generate(text_all)

    fig_wc_all, ax_wc_all = plt.subplots(figsize=(15, 10))
    ax_wc_all.imshow(cloud_all, interpolation='bilinear')
    ax_wc_all.axis('off')
    st.pyplot(fig_wc_all)

    # Create and display WordCloud and common words for each sentiment
    def create_wordcloud(sentiment):
        text = " ".join(df_eda[df_eda['sentiment'] == sentiment]['text'].values)
        wordcloud = WordCloud(
            background_color='black',
            colormap="cool",
            collocations=False,
            width=2000,
            height=1000
        ).generate(text)
        return wordcloud, text

    sentiments = ['neutral', 'positive', 'negative']

    for sentiment in sentiments:
        st.markdown('---')
        st.subheader(f'Word Cloud of {sentiment.capitalize()} Tweets')
        wordcloud, text = create_wordcloud(sentiment)
        fig_wc_sent, ax_wc_sent = plt.subplots(figsize=(15, 10))
        ax_wc_sent.imshow(wordcloud, interpolation='bilinear')
        ax_wc_sent.axis('off')
        st.pyplot(fig_wc_sent)
    

if __name__ == '__main__':
    run()