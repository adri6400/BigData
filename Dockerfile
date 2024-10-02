# Utiliser une image de base officielle Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt ./requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

<<<<<<< HEAD
# Copier le code de l'application dans le conteneur
COPY . .

# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["streamlit", "run", "app.py"]

=======
# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8501

# Commande pour démarrer l'application
CMD ["streamlit", "run", "app.py"]
>>>>>>> 45d179f56400ab945c1347df9aaa3bec9f16921b
