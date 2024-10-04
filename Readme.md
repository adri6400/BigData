# Projet BIG DATA 

## Créer l'environnement python : 
```
python3 -m venv env
```

## Activez l'environnement Python : 
``` 
source env/bin/activate
```

## Mettre les lib dans l'environnement : 
```
pip install -r requirements.txt 
```

## Lancez l'application streamlit : 
``` 
streamlit run app.py
```


## Mettre les variables d'environnement comme ceci dans le fichier .env: 
```
CLIENT_ID
CLIENT_SECRET
user_name
user_password
DATABASE
COLLECTION
```

## Lancer le docker : 
```
docker compose up --build
```
