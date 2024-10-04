from utils.KNN import GenrePredictor
import utils.api_spotify as api_spotify


import streamlit as st
import pandas as pd


# Initialiser le prédicteur
predictor = GenrePredictor('spotify_songs.csv')

# Champs de saisie pour le nom de l'artiste et le titre
artist_name = st.text_input('Nom de l\'artiste')
track_name = st.text_input('Titre de la chanson')

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
    else:
        st.write("No track found matching the criteria.")

# Convertir le JSON en DataFrame (assurez-vous que le JSON a un format adéquat)
    new_data = pd.DataFrame([track_features])
    
    st.write("Nouvelles données pour la prédiction :")
    st.write(new_data)

     # Bouton pour prédire le genre
    if st.button('Prédire le Genre'):
        try:
            predicted_genre = predictor.predict(new_data)
            st.write(f"Le genre prédit est : {predicted_genre[0]}")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")

# Évaluation du modèle
if st.button('Évaluer le Modèle'):
    accuracy = predictor.evaluate()
    st.write(f"Accuracy du modèle : {accuracy:.2f}")


