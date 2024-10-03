import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# CSS personnalisé pour styliser le menu
custom_css = """
    <style>
    /* Changer la couleur de fond de la barre de navigation */
    .css-18e3th9 {
        background-color: #4CAF50;  /* Couleur de fond du menu */
        color: red;  /* Couleur du texte */
    }
    
    /* Changer la couleur du texte des boutons dans le menu */
    .css-1q8dd3e a {
        color: white !important;  /* Couleur du texte */
    }
    
    /* Modifier les titres de la sidebar */
    .css-1hynsf2 {
        color: white;  /* Couleur des titres de la sidebar */
    }

    /* Changer la couleur du fond de la sidebar */
    .css-1d391kg {
        background-color: blue !important;  /* Couleur de fond de la sidebar */
    }
    </style>
    """



# Injecter le CSS dans l'application
st.markdown(custom_css, unsafe_allow_html=True)

st.title('App Musique')



#Récupération du dataframe 
df = pd.read_csv('Spotify_Song_Attributes.csv')
st.write('Plus de ', len(df) , 'musiques sur notre site')

st.write(df)

# image_path = "./aa.jpeg"  

# # Afficher l'image
# st.image(image_path, caption='Ceci est un exemple d\'image', use_column_width=True)

image_paths = [
    "./aa.jpeg",  
    "./aa.jpeg",  
    "./aa.jpeg",  
    "./aa.jpeg",  
    "./aa.jpeg",  
]

# Affichage des images dans des colonnes
cols = st.columns(len(image_paths))

# Afficher chaque image dans sa colonne
for col, image_path in zip(cols, image_paths):
    col.image(image_path, caption='Titre de l\'image', use_column_width=True)