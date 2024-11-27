import streamlit as st
import plotly.express as px
from data import get_files, get_date, get_sentiment_analysys

files = get_files('diary/*')
date = get_date('diary/*')


scores_pos = []
scores_neg = []

for file in files:
    scores = get_sentiment_analysys(file)
    scores_pos.append(scores['pos'])
    scores_neg.append(scores['neg'])

#print(scores_pos)
#print(scores_neg)
st.title("Diary Tone")
st.subheader("Positivity")
figure = px.line(x=date, y=scores_pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)
st.subheader("Negativity")
figureNeg = px.line(x=date, y=scores_neg, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figureNeg)

