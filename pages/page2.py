import streamlit as st
import pandas as pd
import numpy as np

#Récupération du dataframe 
df = pd.read_csv('Spotify_Song_Attributes.csv')

if df is not None:
    
    if 'genre' in df.columns:
        genres = df['genre'].unique()
        genres = np.delete(genres, 0)
        
        # # Créer une liste déroulante avec les genres
        genre_selection = st.selectbox("Choisissez un genre", genres)
        st.write("Vous avez choisi", genre_selection)
        
        # # Filtrer le DataFrame en fonction du genre sélectionné
        df_filtered = df[df['genre'] == genre_selection]
        
        # # Afficher le tableau filtré
        st.write(f"Affichage des données pour le genre : {genre_selection}")
        st.dataframe(df_filtered)
    else:
        st.error("La colonne 'Genre' n'existe pas dans ce fichier CSV.")
        
else:
    st.write("Veuillez télécharger un fichier CSV.")