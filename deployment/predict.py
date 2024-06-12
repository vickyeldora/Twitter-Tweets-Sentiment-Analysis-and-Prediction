import pandas as pd
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

# Library for Pre-Processing
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load model
model = load_model('model_improve')

# Define cleaning function
cleaning_pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
lemmatizer = WordNetLemmatizer()
# Additional Stopwords
additional_stopwords = ['to', 'I', 'the', 'a', 'my', 'and', 'i', 'you', 'is', 'for', 'in', 'of',
 'it', 'on', 'have', 'that', 'me', 'so', 'with', 'be', 'but',
 'at', 'was', 'just', 'I`m', 'not', 'get', 'all', 'this', 'are',
 'out', 'like', 'day', '-', 'up', 'go', 'your', 'good', 'got', 'from',
 'do', 'going', 'no', 'now', 'love', 'work', '****', 'will', 'about',
 'one', 'really', 'it`s', 'u', 'don`t', 'some', 'know', 'see', 'can',
 'too', 'had', 'am', 'back', '&', 'time', 'what', 'its', 'want', 'we',
 'new', 'as', 'im', 'think', 'can`t', '2', 'if', 'when', 'an', 'more',
 'still', 'today', 'miss', 'has', 'they', 'much', 'there', 'last',
 'need', 'My', 'how', 'been', 'home', 'lol', 'off', 'Just', 'feel',
 'night', 'i`m', 'her', 'would', 'The']

# Setting stopwords in English
stpwds_eng = list(set(stopwords.words('english')))
for word in additional_stopwords:
    stpwds_eng.append(word)

# Build text cleaning function
def text_process(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove mentions, links, and non-alphanumeric characters
    text = re.sub(cleaning_pattern, ' ', text)

    # Remove mentions
    text = re.sub("@[A-Za-z0-9_]+", " ", text)

    # Remove hashtags
    text = re.sub("#[A-Za-z0-9_]+", " ", text)

    # Remove newlines
    text = re.sub(r"\\n", " ", text)

    # Remove words with less than 3 characters
    text = re.sub(r'\b\w{1,3}\b', " ", text)

    # Remove URLs
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www.\S+", " ", text)

    # Remove whitespace at the start and end
    text = text.strip()

    # Remove non-letter characters (such as emoticons, symbols, etc.)
    text = re.sub("[^A-Za-z\s']", " ", text)

    # Remove double spaces
    text = re.sub("\s\s+" , " ", text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    text = ' '.join([word for word in tokens if word not in stpwds_eng])

    # Apply lemmatization
    text = lemmatizer.lemmatize(text)

    return text

def run():
    # Create title
    st.title('TWITTER TWEETS SENTIMENT DETECTION')
    st.subheader('Used to detect the category of Twitter tweets')
    st.markdown('---')
    
    # Create form
    with st.form(key='Tweets Prediction'):
        st.write("## Tweet Text")
        # Text input
        text = st.text_input("Enter the tweet:")
        submitted = st.form_submit_button('Predict')
        
        # Perform prediction
        if submitted:
            data_inf = {'text': text}
            data_inf = pd.DataFrame([data_inf])
            # Preprocess the text (apply the same preprocessing steps as used during training)
            data_inf['text'] = data_inf['text'].apply(lambda x: text_process(x))
            # Make the prediction using the loaded model
            y_pred_inf = model.predict(data_inf)
            y_pred_inf = np.argmax(y_pred_inf)

            # Display the prediction result
            if y_pred_inf == 0:
                st.error("Prediction: Negative Tweet", icon="🤐")
                st.snow()
            elif y_pred_inf == 1:
                st.success("Prediction: Neutral Tweet", icon="😎")
                st.balloons()
            else:
                st.warning("Prediction: Positive Tweet", icon="😁")
                st.balloons()

            # Display the extracted text
            st.subheader("Extracted Tweet Text:")
            st.write(text)

if __name__ == '__main__':
    run()
