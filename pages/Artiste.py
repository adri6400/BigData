import streamlit as st
import pandas as pd
import numpy as np
import utils.api_spotify as api_spotify


st.set_page_config(layout="wide")
st.write("Bienvenue sur notre page de recherche d'artiste")

artist_name = st.text_input('Nom de l\'artiste')

if st.button('Rechercher les informations de l\'artiste') :
    access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
    artist_id, name, popularity, genre, following = api_spotify.search_artist(artist_name, access_token) 
    if artist_id : 
        st.write(f"Non de l'artiste : {name}")
        st.write(f"Popularité de l'artiste : {popularity}")
        st.write(f"Genre de l'artiste : {genre}")
        st.write(f"Nombres de Followers : {following}")
#Récupération du dataframe 
