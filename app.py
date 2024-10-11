
import utils.api_spotify as api_spotify
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pytest


 
def test_user_name():
    # Accéder à la variable d'environnement
    user_name = os.getenv('user_name')
    
    # Vérifier que la variable user_name est bien égale à "user_name"
    assert user_name == "user_name", f"Expected 'user_name', but got {user_name}"


# Charger le fichier .env
load_dotenv()

# Accéder aux variables d'environnement
user_name = os.environ.get('user_name')
user_password = os.environ.get('user_password')
database_name = os.environ.get('DATABASE')
collection_name = os.environ.get('COLLECTION')

st.set_page_config(layout="wide")


st.title('App Musique')

#Affichage de la bdd
# Connexion à MongoDB

client = MongoClient(f'mongodb://{user_name}:{user_password}@mongo:27017/')


db = client[database_name] 
collection = db[collection_name]  

data = list(collection.find())

df = pd.DataFrame(data) 

if '_id' in df.columns:
    df = df.drop('_id', axis=1)
    
    

 
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


# # Afficher l'image
# st.image(image_path, caption='Ceci est un exemple d\'image', use_column_width=True)

# image_paths = [
#     "./img/aa.jpeg",  
#     "./img/aa.jpeg",  
#     "./img/aa.jpeg",  
#     "./img/aa.jpeg",  
#     "./img/aa.jpeg",  
# ]

# # Affichage des images dans des colonnes
# cols = st.columns(len(image_paths))

# # Afficher chaque image dans sa colonne
# for col, image_path in zip(cols, image_paths):
#     col.image(image_path, caption='Titre de l\'image', use_column_width=True)
