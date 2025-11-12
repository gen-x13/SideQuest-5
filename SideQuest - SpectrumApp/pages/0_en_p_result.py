# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 17:28:45 2025

@author: @genxcode - Form with Cluster
"""
# OS
import os

# Convertor
import base64

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
st.title("Spectrum App Test : Results")
st.header("Your results :")

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

# Pictures Path
path = os.path.join('assets', 'sites')

# Transform Picture to inject in HTML
def get_base64_image(path):
    with open(path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode('utf-8')
    return f"data:image/png;base64,{b64_data}"

# Screenshots
notion = os.path.join(path, 'notion.png')
notion = get_base64_image(notion)

obsidian = os.path.join(path, 'obsidian.png')
obsidian = get_base64_image(obsidian)

pro_hun = os.path.join(path, 'product_hunt.avif')
pro_hun = get_base64_image(pro_hun)

loo_stu = os.path.join(path, 'looker_studio.webp')
loo_stu = get_base64_image(loo_stu)

ind_hac = os.path.join(path, 'indie_hacker.jfif')
ind_hac = get_base64_image(ind_hac)

beta_list = os.path.join(path, 'beta_list.png')
beta_list = get_base64_image(beta_list)

look_stu = os.path.join(path, 'lookerstudio.png')
look_stu = get_base64_image(look_stu)

freelan = os.path.join(path, 'freelancer.png')
freelan = get_base64_image(freelan)

upwork = os.path.join(path, 'upwork.png')
upwork = get_base64_image(upwork)

nextcloud = os.path.join(path, 'nextcloud.png')
nextcloud = get_base64_image(nextcloud)

plausible = os.path.join(path, 'plausible.jfif')
plausible = get_base64_image(plausible)

# Results Written Part

st.subheader(f"Your score is {st.session_state.score} %")

if st.session_state.score < 25:
    
    st.subheader("Multitask Mind User Type:")
    
    st.markdown("As a multitasker, you tend to spread yourself thin.")
    st.markdown("You are also very likely to have multiple passions.")
    st.markdown("We therefore have a series of websites/applications to offer you:")
    
    one = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://www.notion.so" target="_blank">
            <img class="zoom" src="{notion}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    two = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://obsidian.md" target="_blank">
            <img class="zoom" src="{obsidian}" alt="Obsidian"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
           
    liste = [one, two] # Puisque ça ne veut pas : Image cliquable !
        
    row1 = st.columns(2)
    
    for i, l in enumerate(liste):
        with row1[i % 3]:
            st.container(height=250).markdown(l, unsafe_allow_html=True)

elif 25 < st.session_state.score < 49:
    
    st.subheader("Early Adopters User Type :")
    
    st.markdown("As an early adopter, you enjoy testing new features before anyone else and sharing them.")
    st.markdown("You are also what we call a beta tester, testing even prototypes before the finished model.")
    st.markdown("We therefore have a series of sites/applications to recommend to you:")
    
    one = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://www.producthunt.com" target="_blank">
            <img class="zoom" src="{pro_hun}" alt="Product Hunt"
                 style="width:100%; max-width:900px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    two = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://betalist.com" target="_blank">
            <img class="zoom" src="{beta_list}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    

    three = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://www.indiehackers.com" target="_blank">
            <img class="zoom" src="{ind_hac}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    
    four = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://lookerstudio.google.com" target="_blank">
            <img class="zoom" src="{look_stu}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    
    liste = [one, two, three, four]
       
    row = st.columns(2)

    for i, l in enumerate(liste):
        with row[i % 2]:
            st.container(height=250).markdown(l, unsafe_allow_html=True)
        
        if i % 2 == 1:
            row = st.columns(2)
    

elif 50 < st.session_state.score < 74:
    
    st.markdown("Delegator User Type :")
    
    st.markdown("As a delegator, you prefer to assign tasks rather than do them yourself.")
    st.markdown("You prefer to have tailor-made solutions, pay for professionals, and not have to learn new skills that would waste your time.")
    st.markdown("We therefore have this series of websites/applications to present to your profile type:")
    
    one = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://freelancer.com" target="_blank">
            <img class="zoom" src="{freelan}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    two = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://www.upwork.com" target="_blank">
            <img class="zoom" src="{upwork}" alt="Obsidian"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
           
    liste = [one, two] # Puisque ça ne veut pas : Image cliquable !
        
    row1 = st.columns(2)
    
    for i, l in enumerate(liste):
        with row1[i % 3]:
            st.container(height=250).markdown(l, unsafe_allow_html=True)

elif 75 < st.session_state.score < 100:
    
    st.markdown("Data Sovereign User Type :")
    
    st.markdown("As a data sovereign, you value autonomy and simplicity, and you want to control your data.")
    st.markdown("You are open to the world of technology but wary of how online services use your sensitive data.")
    st.markdown("We therefore have a series of websites/applications for your category to discover:")
    
    one = " https://live-report-generator.streamlit.app/" 
    two = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://nextcloud.com" target="_blank">
            <img class="zoom" src="{nextcloud}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    three = f"""
    <style>
    .zoom:hover {{
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }}
    </style>
    <div style="display:flex; justify-content:center;">
        <a href="https://plausible.io" target="_blank">
            <img class="zoom" src="{plausible}" alt="Notion"
                 style="width:100%; max-width:800px; height:auto; border-radius:10px;">
        </a>
    </div>
    """
    
    liste = [one, two, three]
        
    row1 = st.columns(2)
    
    for i, l in enumerate(liste):
        with row1[i % 2]:
            st.container(height=250).markdown(l, unsafe_allow_html=True)
        if i % 2 == 1:
            row = st.columns(2)

# Notification for the user
def notif_score():
    msg = st.toast(f"Your results !")
 

if st.button("Return to the Main Page"):
    st.session_state.score = 0
    st.switch_page("pages/0_en_intro.py")