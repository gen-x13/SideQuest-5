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

# Timer
import time

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
    st.session_state.bar = st.progress(0)


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
q1_dict = {
    
        "Solo developper" : 3,
        "Freelancer" : 5,
        "Founder" : 10,
        "Other" : 1
    }

q2_dict = {
    
        "18-29" : 2,
        "30-45" : 2,
        "50+" : 2
    }

q3_dict = {
    
        "Concentration" : 3,
        "Lack of control" : 5,
        "Technical complexity" : 5,
        "Confidentiality" : 6
    }

st.session_state.bar = st.progress(0)

# Q/A Part
st.title("Spectrum App Test")

st.subheader("Question 1")
# Question 1
q1 = st.radio("What is your main profile?", 
         list(q1_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("") # Space

st.subheader("Question 2")
# Question 2
q2 = st.radio("What is your age group?", 
         list(q2_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("")

st.subheader("Question 3")
# Question 3
q3 = st.radio("What is your biggest challenge when you work?", 
         list(q3_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

# Notification for the user
def notif_score():
    msg = st.toast(f"Points added !")
    time.sleep(2)
 
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
            
            liste = q1_dict[q1], q2_dict[q2], q3_dict[q3]
            points = sum(liste)
            st.session_state.score += points
            notif_score()
            progress(step=33)
            st.switch_page("pages/0_en_p_two.py")
            
        except Exception as e:
            st.toast("Not all questions were answered !", icon="⚠️")
with col1:
    if st.button("Main Page"):
        progress(step=0)
        st.switch_page("pages/0_en_intro.py")