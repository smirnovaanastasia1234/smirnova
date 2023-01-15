import streamlit as st
import pandas as pd
from io import StringIO

# Настройка заголовка и текста 
import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image

# Title of the application 
st.title('Анализ тональности текста\n', )
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

# Sidebar options
option = st.sidebar.selectbox('выбрать из списка', 
["Загрузка файла",
 "Определение тональности текста", 
  "Диаграммы", 
 ])

st.set_option('deprecation.showfileUploaderEncoding', False)

if option == 'Загрузка файла':
	st.write(
			"""
				## Описание проекта
				Это инструмент анализа текста, разработанный группой 32. Доступ к инструментам можно получить на левой боковой панели.
			"""
		)
elif option == "Определение тональности текста":

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

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