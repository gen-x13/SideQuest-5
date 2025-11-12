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

# Badges
from streamlit_extras.badges import badge

# Pandas for the df type
import pandas as pd

# Model for Clustering
from sklearn.cluster import KMeans

# False data for clustering
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs # using "blobs" for cluster

# Display the results
import plotly.express as px

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

# Storing the data in JSON


# Clustering all the data


# Result Part
st.title("Spectrum App Test : Résultats")
st.header("Vos résultats :")

# Visual Results part

# Samples as blobs 
X, y = make_blobs(
    n_samples=1000,
    centers=[[-30, -30], [30, 30], [-30, 30], [30, -30]], # Coordonates
    cluster_std=5,
    random_state=1
)

# KMEANS
model = KMeans(n_clusters=4)

# Training
model.fit(X)

# Prediction
pred = model.predict(X)

# Turning it into a dataframe : scatter can't build graphic without y
df = pd.DataFrame(X, columns=["x", "y"])
df["pred"] = pred

# Figure of the clusters
fig2 = px.scatter(df, x="x", y="y", color=df["pred"].astype(str)) # int -> str

fig2.update_xaxes(
    tickvals=[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],
    ticktext=["-50", "-40", "-30", "-20", "-10", "0", "10", "20", "30", "40", "50"]
)

fig2.update_yaxes(
    tickvals=[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],
    ticktext=["-50", "-40", "-30", "-20", "-10", "0", "10", "20", "30", "40", "50"]
)

if st.session_state.score < 25:
    
    fig2.add_scatter(x=[-30],
                    y=[30],
                    marker=dict(
                        color='black',
                        size=10
                    ),
                   name='Multitask Mind User Type') 

elif 25 < st.session_state.score < 49:
    
    fig2.add_scatter(x=[30],
                    y=[-30],
                    marker=dict(
                        color='black',
                        size=10
                    ),
                   name='Early Adopters User type')

elif 50 < st.session_state.score < 74:
    
    fig2.add_scatter(x=[30],
                    y=[30],
                    marker=dict(
                        color='black',
                        size=10
                    ),
                   name='Delegator User Type')

elif 75 < st.session_state.score < 100:
    
    fig2.add_scatter(x=[-30],
                    y=[-30],
                    marker=dict(
                        color='black',
                        size=10
                    ),
                   name='Data Sovereign User Type')
    
st.plotly_chart(fig2)

# Results Written Part


st.subheader(f"Vous avez un score de {st.session_state.score} %")

st.markdown("""
    <style>
    [data-testid="stWidgetContainer"] > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 20px;
        margin: 10px 0;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.score < 25:
    
    st.subheader("Multitask Mind User Type : Utilisateur Type « Esprit Multitâche »")
    
    st.markdown("En tant que multitâche vous avez tendance à vous disperser.")
    st.markdown("Vous êtes très probablement multi-passionné aussi.")
    st.markdown("Nous avons donc une série de sites / applications à vous proposer :")
    
    one = "https://mindscout.net/"
    two = "https://www.notion.com/"
    three = "https://obsidian.md/"
    
    liste = [one, two, three]
        
    row1 = st.columns(3)
    
    for i, l in enumerate(liste):
        with row1[i % 3]:
            st.container(height=500).markdown(l)

elif 25 < st.session_state.score < 49:
    
    st.subheader("Early Adopters User Type : Utilisateur Type « Adopteurs Précoces »")
    
    st.markdown("En tant qu'adopteur précoce vous appréciez tester les nouveautés avant tout le monde et les partager.")
    st.markdown("Vous êtes aussi ce qu'on appelle un beta tester, testant même des prototypes avant le modèle fini.")
    st.markdown("Nous avons donc une série de sites / applications à vous recommander :")
    
    one = " https://www.producthunt.com/"
    two = " https://betalist.com/"
    three = " https://www.indiehackers.com/"
    four = " https://lookerstudio.google.com/"
    
    liste = [one, two, three, four]
        
    row1 = st.columns(4)
    
    for i, l in enumerate(liste):
        with row1[i % 4]:
            st.container(height=500).markdown(l)
    

elif 50 < st.session_state.score < 74:
    
    st.markdown("Delegator User Type : Utilisateur Type « Déléguant »")
    
    st.markdown("En tant que délégant vous appréciez attribuer vos tâches plutôt que de les exécuter vous-mêmes.")
    st.markdown("Vous préférez avoir du sur-mesure, payer pour des professionnels et ne pas avoir à apprendre ce qui vous ferait perdre du temps.")
    st.markdown("Nous avons donc cette série de sites / applications à présenter à votre type de profil :")
    
    one = " https://freelancer.com/"
    two = " https://www.upwork.com/"
    three = " https://www.noteboards.co.uk/"
    
    liste = [one, two, three]
        
    row1 = st.columns(3)
    
    for i, l in enumerate(liste):
        with row1[i % 3]:
            st.container(height=500).markdown(l)

elif 75 < st.session_state.score < 100:
    
    st.markdown("Data Sovereign User Type : Utilisateur Type « Souverain des données »")
    
    st.markdown("En tant que souverain des données vous aimez l'autonomie, la simplicité, et vous voulez contrôler vos données.")
    st.markdown("Vous êtes ouverts au monde de la tech et méfiant concernant l'utilisation de vos données sensibles par des services en ligne.")
    st.markdown("Nous avons donc une série de sites / applications à faire découvrir à votre catégorie :")
    
    one = " https://live-report-generator.streamlit.app/"
    two = " https://nextcloud.com/"
    three = " https://plausible.io/"
    
    liste = [one, two, three]
        
    row1 = st.columns(3)
    
    for i, l in enumerate(liste):
        with row1[i % 3]:
            st.container(height=500).markdown(l)
    
    
st.caption(f"👥 You are the visitor #{len(st.session_state.get('visitors', []))+1}")

# Notification for the user
def notif_score():
    msg = st.toast(f"Vos résultats !")
 

if st.button("Retour à la page principal"):
    st.session_state.score = 0
    st.switch_page("pages/1_fr_intro.py")