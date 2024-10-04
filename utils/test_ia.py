
import requests
import os
#se connecter au bon ficheir .env
from dotenv import load_dotenv
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
print(client_id)
print(client_secret)
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']



def search_track(track_name, artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    query_params = {
        'q': f'track:{track_name} artist:{artist_name}',
        'type': 'track',
        'limit': 1  # Augmenter le nombre de résultats pour plus de choix
    }
    response = requests.get(search_url, headers=headers, params=query_params)
    results = response.json()
    artist_id = results['tracks']['items'][0]['album']['artists'][0]['id']
    print("L'ID de l'artiste est :", artist_id)
    tracks = results['tracks']['items']
    if tracks:
        for track in tracks:
            # Vérifier que le nom de l'artiste et le titre correspondent exactement
            if track_name.lower() in track['name'].lower() and any(artist_name.lower() in artist['name'].lower() for artist in track['artists']):
                return track['id'], track['name'], track['artists'][0]['name'], track['preview_url'], artist_id
    return None, None, None, None


def get_track_features(track_id, access_token):
    track_features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(track_features_url, headers=headers)
    return response.json()



def get_artist_genres(artist_id, access_token):
    artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(artist_url, headers=headers)
    artist_info = response.json()
    return artist_info.get('genres', [])  # Retourne une liste de genres

# Utiliser le code précédent pour obtenir access_token, track_id, etc.
access_token = get_access_token(client_id, client_secret)
track_id, found_track_name, found_artist_name, preview_url, artiste_id = search_track("Fever", "Vybz Kartel", access_token)
if track_id:
    print(f"Found track ID: {track_id}")
    print(f"Track name: {found_track_name}")
    print(f"Artist name: {found_artist_name}")
    print(f"Preview URL: {preview_url}")
    
    # Utiliser track_id pour obtenir les détails de la piste, puis artist_id pour obtenir les genres
    track_features = get_track_features(track_id, access_token)
    artist_genres = get_artist_genres(artiste_id, access_token)
    print("Genres de l'artiste :", artist_genres)
else:
    print("No track found matching the criteria.")


def search_artist(artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    query_params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 1  # Limite à un résultat pour obtenir le plus pertinent
    }
    response = requests.get(search_url, headers=headers, params=query_params)
    results = response.json()
    artists = results['artists']['items']
    following = results['artists']['items'][0]['followers']['total']
    if artists and following :
        artist_id = artists[0]['id']
        return artist_id, artists[0]['name'], artists[0]['popularity'], artists[0]['genres'], following
    return None, None, None, None

access_token = get_access_token(client_id, client_secret)
artist_id, artist_name, artist_popularity, artist_genres, following= search_artist("PNL", access_token)
if artist_id:
    print(f"Artist ID: {artist_id}")
    print(f"Artist Name: {artist_name}")
    print(f"Popularity: {artist_popularity}")
    print(f"Genres: {artist_genres}")
    print(f"Nombre de followers : {following}")
else:
    print("No artist found matching the criteria.")
