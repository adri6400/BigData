import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#Chargement dataset
df = pd.read_csv('Spotify_Song_Attributes.csv')

st.title('Tendances')

st.write("### Chanteurs populaires")
st.write(df[['artistName', 'genre', 'msPlayed']].drop_duplicates())



st.write("### Genres populaires")


st.write("### Top du moment")
top_artist = df.nlargest(3, 'msPlayed')[['artistName', 'genre', 'msPlayed']]
st.write(df.nlargest(3, 'msPlayed')[['artistName', 'genre', 'msPlayed']])


