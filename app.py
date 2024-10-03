
import BigData.utils.api_spotify as api_spotify

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

# Chargement du fichier CSV avec des options supplémentaires
try:
    df = pd.read_csv('Spotify_Song_Attributes.csv')
except pd.errors.ParserError as e:
    st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
    df = pd.DataFrame()  # Créer un DataFrame vide en cas d'erreur

# Champs de saisie pour le nom de l'artiste et le titre
artist_name = st.text_input('Nom de l\'artiste')
track_name = st.text_input('Titre de la chanson')

# Filtrer le DataFrame en fonction des valeurs saisies




# Bouton pour rechercher la chanson sur Spotify
if st.button('Rechercher dans spotify') : 
    access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
    track_id, found_track_name, found_artist_name, preview_url = api_spotify.search_track(track_name, artist_name, access_token)
    if track_id:
        st.write(f"Found track ID: {track_id}")
        st.write(f"Track name: {found_track_name}")
        st.write(f"Artist name: {found_artist_name}")
        st.write(f"Preview URL: {preview_url}")
        track_features = api_spotify.get_track_features(track_id, access_token)
        st.write(track_features)
    else:
        st.write("No track found matching the criteria.")
# Afficher le DataFrame filtré
st.write(df)



st.write('Plus de ', len(df) , 'musiques sur notre site')



# image_path = "./aa.jpeg"  

# # Afficher l'image
# st.image(image_path, caption='Ceci est un exemple d\'image', use_column_width=True)

image_paths = [
    "./img/aa.jpeg",  
    "./img/aa.jpeg",  
    "./img/aa.jpeg",  
    "./img/aa.jpeg",  
    "./img/aa.jpeg",  
]

# Affichage des images dans des colonnes
cols = st.columns(len(image_paths))

# Afficher chaque image dans sa colonne
for col, image_path in zip(cols, image_paths):
    col.image(image_path, caption='Titre de l\'image', use_column_width=True)
