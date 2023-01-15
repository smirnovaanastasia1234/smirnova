import streamlit as st
import pandas as pd
from io import StringIO

# Настройка заголовка и текста 
st.title("COVID 19 IN THE WORLD DASHBOARD")
st.write("""This dashboard will present the spread of COVID-19 in the world by visualizing the timeline of the total cases and deaths. As well as the total number of vaccinated people.""")

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(
    """
    This app is Open Source dashboard.
    """
)
st.sidebar.info("Feel free to collaborate and comment on the work. The github link can be found "
                "[here](https://github.com/yuliianikolaenko/COVID_dashboard_proglib).")
# Загружаем новые оптимизированные данные
DATA = ('data.csv')