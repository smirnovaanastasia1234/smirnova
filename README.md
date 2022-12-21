# Практическое задание 4 

Web-приложение для определения тональности текста. Используются библиотеки:

- [TensorFlow](https://www.tensorflow.org/).
- [Streamlit](https://streamlit.io/).

Для распознавания текста используется модель DeepPavlov/rubert-base-case-conversational (https://huggingface.co/DeepPavlov/rubert-base-cased-conversational/)

- ["sentiment-analysis","blanchefort/rubert-base-cased-sentiment"](https://huggingface.co/DeepPavlov/rubert-base-cased-conversational/).

## Streamlit app

Приложение можно найти , щелкнув по значку Streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smirnovaanastasia1234-smirnova-app-ls6d5v.streamlit.app/)

[Ссылка на развернутое приложение](https://smirnovaanastasia1234-smirnova-app-ls6d5v.streamlit.app/).

## Результаты анализа тональности текста
    0: NEUTRAL
    1: POSITIVE
    2: NEGATIVE

## Код 
```python
import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)

def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    return model

model = load_model()
st.header ("Определение тональности текстов")
st.subheader ("Введите текст для анализа")
text = st.text_area(" ",height=100)
result = st.button("Определить тональность текста")


if result:
    res = model(text)
    sent = res[0]['label'] 
    st.write(model(text)[0]["label"])
```


## Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В. 


