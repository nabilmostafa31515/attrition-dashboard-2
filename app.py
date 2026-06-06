"""
Week #1 Task: Employee Attrition Dashboard
Entry point — multipage navigation
"""
import streamlit as st

st.set_page_config(
    page_title="Week #1 Task: Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation([
    st.Page("1_Dashboard.py",  title="📊 Dashboard"),
    st.Page("2_Analysis.py",   title="🔍 Analysis Answers"),
])
pg.run()
