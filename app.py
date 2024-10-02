import streamlit as st

st.title('Mon Application Streamlit')

st.write('Voici notre première application avec Streamlit.')

# Création d'un slider
# peux tu afficher le csv dans un dataframe Spotify_Song_Attributes.csv
import pandas as pd

df = pd.read_csv('Spotify_Song_Attributes.csv')
st.write(df)
