import streamlit as st
from transformers import pipeline
import torch



st.header("Определение тональности текстов")
st.subheader("Введите текст для анализа")

@st.cache

text = st.text_area(" ",height=100)

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

st.write ("Тональность текста:")
st.write(classifier(text)[0]["label"])
#end program 
