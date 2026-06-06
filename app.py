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
    st.Page("pages/1_Dashboard.py",  label="📊 Dashboard",         icon="📊"),
    st.Page("pages/2_Analysis.py",   label="🔍 Analysis Answers",  icon="🔍"),
])
pg.run()
