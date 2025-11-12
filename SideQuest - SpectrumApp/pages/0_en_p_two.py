# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 17:28:45 2025

@author: @genxcode - Form with Cluster
"""

# Streamlit
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

# OS
import os


# Page Icon, side bar collpase
st.set_page_config(page_title="Spectrum App Test", page_icon="📋", 
                   initial_sidebar_state="collapsed")


# Session State
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "horizontal" not in st.session_state:
    st.session_state.horizontal = True
if "score" not in st.session_state:
    st.session_state.score = 0
if "bar" not in st.session_state:
    st.session_state.bar = 0
if "progress_value" not in st.session_state:
    st.session_state.progress_value = 0
    
# Disable sidebar
st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)
            
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
            
# CSS Background
css_path = os.path.join('css', 'css.css')
print(css_path)
with open(css_path) as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    

# Dictionnary answers / points
q4_dict = {
    
        "0-3" : 3,
        "4-7" : 7,
        "8-15" : 10,
        "15+" : 15
    }

q5_dict = {
    
        "Yes" : 15,
        "Rarely" : 5,
        "Never" : 0
    }

q6_dict = {
    
        "Less than 1h" : 5,
        "1-3h" : 10,
        "More than 3h" : 18
    }

st.progress(st.session_state.progress_value)

# Q/A Part
st.title("Spectrum App Test")

st.subheader("Question 4")
# Question 1
q4 = st.radio("How many different online tools/services do you use on a daily basis for work?", 
         list(q4_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("") # Space

st.subheader("Question 5")
# Question 2
q5 = st.radio("Do you regularly work with data (CSV, Excel, databases, APIs)?", 
         list(q5_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("")

st.subheader("Question 6")
# Question 3
q6 = st.radio("How much time do you waste managing/synchronizing your tools?", 
         list(q6_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

# Notification for the user
def notif_score():
    msg = st.toast(f"Points added !")
 
# Tracking the progression
def progress(step=10):
    new_value = st.session_state.progress_value + step
    st.session_state.progress_value = min(new_value, 100)
    st.session_state.bar.progress(st.session_state.progress_value)

col1, spacer, col2 = st.columns([1, 4, 1])

with col2:
    # Navigation through the test
    if st.button("Next"):
        
        try:
            
            liste = q4_dict[q4], q5_dict[q5], q6_dict[q6]
            points = sum(liste)
            st.session_state.score += points
            notif_score()
            progress(step=33)
            st.switch_page("pages/0_en_p_three.py")
        except Exception as e:
            st.info("Not all questions were answered !", icon="⚠️")

with col1:    
    if st.button("Previous"):
        progress(step=-33)
        st.switch_page("pages/0_en_p_one.py")