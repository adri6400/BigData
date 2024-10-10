import streamlit as st
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Charger le fichier .env
load_dotenv()

# Accéder aux variables d'environnement
user_name = os.environ.get('user_name')
user_password = os.environ.get('user_password')
database_name = os.environ.get('DATABASE')
collection_name = os.environ.get('COLLECTION')

# Connexion à MongoDB
client = MongoClient(f'mongodb://{user_name}:{user_password}@mongo:27017/')
db = client[database_name] 
collection = db[collection_name]  

# Page pour filtrer les musiques par chanteur
st.title('Filtrer les musiques par artiste')

# Créer un bouton pour filtrer les musiques de Jul
if st.button('Afficher les musiques de SyKo'):
    # Requête pour filtrer les musiques selon l'artiste Jul
    data = list(collection.find({'artistName': 'SyKo'}))  # Assurez-vous que 'artist' est le nom correct du champ dans MongoDB
    
    if data:
        df = pd.DataFrame(data)
        
        # Suppression de la colonne _id si elle existe
        if '_id' in df.columns:
            df = df.drop('_id', axis=1)

        st.write(df)  # Afficher le DataFrame filtré
    else:
        st.write("Aucune musique trouvée pour SyKo.")
