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
q7_dict = {
    
        "0-20€" : 7,
        "20-100€" : 6,
        "100-300€" : 8,
        "300€+" : 2
    }

q8_dict = {
    
        "Facilité d'utilisation" : 1,
        "Prix" : 8,
        "Sécurité des données" : 15,
        "Efficacité" : 9
    }

q9_dict = {
    
        "Jongler avec 10 tâches en même temps" : 3,
        "Méthodiquement et organisé" : 20,
        "J'expérimente constamment de nouvelles choses" : 6,
        "Je délègue si possible" : 10
    }

st.progress(st.session_state.progress_value)

# Q/A Part
st.title("Spectrum App Test")

st.subheader("Question 7")
# Question 1
q7 = st.radio("Budget mensuel pour vos outils de travail / services en ligne ?", 
         list(q7_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("") # Space

st.subheader("Question 8")
# Question 2
q8 = st.radio("Que priviliégiez-vous dans un nouvel outil ?", 
         list(q8_dict.keys()), index=None, 
         help=None, 
         on_change=None,
         horizontal=st.session_state.horizontal)

st.text("")

st.subheader("Question 9")
# Question 3
q9 = st.radio("Comment décririez-vous votre façon de travailler ?", 
         list(q9_dict.keys()), index=None, 
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
    
        liste = q7_dict[q7], q8_dict[q8], q9_dict[q9]
        points = sum(liste)
        st.session_state.score += points
        notif_score()
        progress(step=33)
        st.switch_page("pages/1_fr_p_result.py")
        
    except Exception as e:
        st.info("Vous n'avez pas répondu à toutes les questions !", icon="⚠️")
    
if st.button("Précédent"):
    progress(step=-33)
    st.switch_page("pages/1_fr_p_two.py")