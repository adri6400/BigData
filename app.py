
import api_spotify

import streamlit as st
import pandas as pd

# Titre de l'application
st.title('Mon Application Streamlit')

st.write('Voici notre première application avec Streamlit.')

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