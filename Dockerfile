# Utiliser une image de base officielle Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt ./requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8501 

# Commande pour démarrer l'application
CMD ["streamlit", "run", "app.py"]
