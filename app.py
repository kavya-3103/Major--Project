import streamlit as st
import nltk
import joblib
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.title(' Sentiment analysis')
user_input = st.text_input("Please enter your text")
nltk.download("vader_lexicon")
vs = SentimentIntensityAnalyzer()
score = vs.polarity_scores(user_input)
st.button("Predict")
st.title("Result....")
if score==0:
   st.write(" ")
elif score["neg"]!=0:
   st.title('PREDICTED OUTPUT IS : NEGATIVE') 
   st.write('AND THE SCORE IS:', score)
elif score["pos"]!=0:
   st.title('PREDICTED OUTPUT IS: POSITIVE')
   st.write(' AND THE SCORE IS:', score)
elif score["neu"]!=0:
  st.title('PREDICTED OUTPUT IS : NEUTRAL')
  st.write(' AND THE SCORE IS:', score)
  
