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
    
        "Oui" : 15,
        "Rarement" : 5,
        "Jamais" : 0
    }

q6_dict = {
    
        "Moins d'1h" : 5,
        "1-3h" : 10,
        "Plus de 3h" : 18
    }

st.progress(st.session_state.progress_value)

# Q/A Part
st.title("Spectrum App Test")


st.subheader("Question 4")
# Question 1
q4 = st.radio("Combien d'outils/services en ligne différents utilisez-vous quotidiennement pour travailler ?", 
         list(q4_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("") # Space

st.subheader("Question 5")
# Question 2
q5 = st.radio("Travaillez-vous régulièrement avec des données (CSV, Excel, base de données, APIs) ?", 
         list(q5_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("")

st.subheader("Question 6")
# Question 3
q6 = st.radio("Combien de temps perdez-vous à gérer / syncroniser vos outils ?", 
         list(q6_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

# Notification for the user
def notif_score():
    msg = st.toast(f"Points ajoutés !")
 
# Tracking the progression
def progress(step=10):
    new_value = st.session_state.progress_value + step
    st.session_state.progress_value = min(new_value, 100)
    st.session_state.bar.progress(st.session_state.progress_value)

# Navigation through the test
if st.button("Suivant"):
    
    try:
    
        liste = q4_dict[q4], q5_dict[q5], q6_dict[q6]
        points = sum(liste)
        st.session_state.score += points
        notif_score()
        progress(step=33)
        st.switch_page("pages/1_fr_p_three.py")
    except Exception as e:
        st.info("Vous n'avez pas répondu à toutes les questions !", icon="⚠️")
    
if st.button("Précédent"):
    progress(step=-33)
    st.switch_page("pages/1_fr_p_one.py")