# Utiliser l'image officielle Python 3.9 comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le code de l'application dans le conteneur
COPY app.py .

# Définir la commande à exécuter lorsque le conteneur démarre
CMD [ "python3", "app.py" ]
