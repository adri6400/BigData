# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

class GenrePredictor:
    def __init__(self, data_path):
        # Charger les données
        self.df = pd.read_csv(data_path)
        
        # Initialiser les encodeurs et le scaler
        self.label_encoder = LabelEncoder()
        self.scaler = StandardScaler()

        # Préparer les données
        self.prepare_data()

    def prepare_data(self):
        # Encoder le genre
        self.df['genre'] = self.label_encoder.fit_transform(self.df['genre'])
        
        # Normaliser les attributs pertinents
        features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 
                    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
        self.df[features] = self.scaler.fit_transform(self.df[features])
        
        # Séparer les features et la target
        self.X = self.df[features]
        self.y = self.df['genre']

        # Diviser les données
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Entraîner le modèle
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.model.fit(self.X_train, self.y_train)

    def predict(self, new_data):
        # Normaliser la nouvelle donnée
        new_data_scaled = self.scaler.transform(new_data)
        
        # Prédire le genre
        predicted_genre = self.model.predict(new_data_scaled)
        return self.label_encoder.inverse_transform(predicted_genre)

    def evaluate(self):
        # Évaluer le modèle
        y_pred = self.model.predict(self.X_test)
        return confusion_matrix(self.y_test, y_pred), classification_report(self.y_test, y_pred)

