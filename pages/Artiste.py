import streamlit as st
import pandas as pd
import numpy as np
import utils.api_spotify as api_spotify


st.set_page_config(layout="wide")
st.write("Bienvenue sur notre page de recherche d'artiste")

artist_name = st.text_input('Nom de l\'artiste')
if len(artist_name) >= 3:
        access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
        artists = api_spotify.search_artist_barre_recherche(artist_name, access_token)
        if artists:
            for artist in artists:
                st.subheader(artist['name'])
                st.write(f"Genres: {artist['genres']}")
                st.write(f"Popularity: {artist['popularity']}")
                if artist['image_url'] != 'No image available':
                    st.image(artist['image_url'], width=200)
                st.write("---")


if st.button('Rechercher les informations de l\'artiste') and len(artist_name)>=1 :
    access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
    artist_id, name, popularity, genre, following, artiste_image_url = api_spotify.search_artist(artist_name, access_token) 
    if artist_id : 
        st.write(f"Non de l'artiste : {name}")
        st.write(f"Popularité de l'artiste : {popularity}")
        st.write(f"Genre de l'artiste : {genre}")
        st.write(f"Nombres de Followers : {following}")
        html_code = f"""
        <div style="display: flex; justify-content: space-around;">
            <div>
                <img src="{artiste_image_url}" style="border-radius: 50%; width: 250px; height: 250px;">
                <p style="text-align: center;">1. <b>Ninho</b> de {name}</p>
            </div>
            
        </div>
        """

# Utiliser Streamlit components pour intégrer du HTML
        st.components.v1.html(html_code, height=350)
#Récupération du dataframe 
