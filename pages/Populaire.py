import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#Chargement dataset
df = pd.read_csv('Spotify_Song_Attributes.csv')

st.title('Tendances')

st.write("### Chanteurs populaires")
st.write(df[['artistName', 'genre']].drop_duplicates())



st.write("### Genres populaires")




