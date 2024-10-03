import streamlit as st
import pandas as pd

x = st.text_input("Favorite artist?")

st.write("Réponse: ", x)

is_clicked = st.button("Clique")