import streamlit as st
import pandas as pd
from io import StringIO

# Настройка заголовка и текста 
st.title("Анализ тональности текста\n")
st.subheader("""Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.""")

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(
    """
    This app is Open Source dashboard.
    """

# Загружаем новые оптимизированные данные
DATA = ('data.csv')