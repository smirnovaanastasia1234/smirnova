import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image
st.set_page_config(
    page_title="Анализ тональности текста",
    page_icon="👋",
# Title of the application 
st.title('Анализ тональности текста\n', )
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

display = Image.open('images/display.jpg')
display = np.array(display)
st.image(display)