import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils.api_spotify as api_spotify
import matplotlib.pyplot as plt
from PIL import Image


st.set_page_config(layout="wide")

#Chargement dataset
df = pd.read_csv('Spotify_Song_Attributes.csv')

st.title('Tendances')

st.write("### Artistes populaires")
total_plays_by_artist = df.groupby('artistName')['msPlayed'].sum().reset_index()
top_3_artistes = total_plays_by_artist.nlargest(3, 'msPlayed')
st.write(top_3_artistes)

#récupération des images de chacun
access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
imagetop1 = api_spotify.search_artist_image(top_3_artistes.iloc[0]['artistName'], access_token)
imagetop2 = api_spotify.search_artist_image(top_3_artistes.iloc[1]['artistName'], access_token)
imagetop3 = api_spotify.search_artist_image(top_3_artistes.iloc[2]['artistName'], access_token)

#Mise en page
# html_code = f"""
# <div style="display: flex; justify-content: space-around;">
#     <div>
#         <img src="{imagetop1[1]}" style="border-radius: 50%; width: 250px; height: 250px;">
#         <p style="text-align: center;">1. {imagetop1.iloc[1]}</p>
#     </div>
#     <div>
#         <img src="{imagetop2[1]}" style="border-radius: 50%; width: 250px; height: 250px;">
#         <p style="text-align: center;">2. <b>{top_artist.iloc[1]['trackName']}</b> de  {imagetop2[0]}</p>
#     </div>
#     <div>
#         <img src="{imagetop3[1]}" style="border-radius: 50%; width: 250px; height: 250px;">
#         <p style="text-align: center;">3. <b>{top_artist.iloc[2]['trackName']}</b> de {imagetop3[0]}</p>
#     </div>
# </div>
# """

# # Utiliser Streamlit components pour intégrer du HTML
# st.components.v1.html(html_code, height=350)

a = api_spotify.search_artist_image('Ninho', access_token)
st.image(a[1], caption='Ceci est un exemple d\'image', use_column_width=True)

st.write("### Genres populaires")



st.write("### Top du moment")

#Récupération du top3 des chansons les plus écoutées
top_artist = df.nlargest(5, 'msPlayed')[['artistName', 'genre', 'msPlayed', 'trackName']].drop_duplicates()

#récupération des images de chacun
access_token = api_spotify.get_access_token(api_spotify.client_id, api_spotify.client_secret)
imagetop1 = api_spotify.search_artist_image(top_artist.iloc[0]['artistName'], access_token)
imagetop2 = api_spotify.search_artist_image(top_artist.iloc[1]['artistName'], access_token)
imagetop3 = api_spotify.search_artist_image(top_artist.iloc[2]['artistName'], access_token)

#Mise en page
html_code = f"""
<div style="display: flex; justify-content: space-around;">
    <div>
        <img src="{imagetop1}" style="border-radius: 50%; width: 250px; height: 250px;">
        <p style="text-align: center;">1. <b>{top_artist.iloc[0]['trackName']}</b> de {imagetop1[0]}</p>
    </div>
    <div>
        <img src="{imagetop2}" style="border-radius: 50%; width: 250px; height: 250px;">
        <p style="text-align: center;">2. <b>{top_artist.iloc[1]['trackName']}</b> de  {imagetop2[0]}</p>
    </div>
    <div>
        <img src="{imagetop3}" style="border-radius: 50%; width: 250px; height: 250px;">
        <p style="text-align: center;">3. <b>{top_artist.iloc[2]['trackName']}</b> de {imagetop3[0]}</p>
    </div>
</div>
"""

# Utiliser Streamlit components pour intégrer du HTML
st.components.v1.html(html_code, height=350)




