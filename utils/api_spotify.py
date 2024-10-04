import requests
import os
#se connecter au bon ficheir .env
from dotenv import load_dotenv
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

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
        'limit': 10  # Augmenter le nombre de résultats pour plus de choix
    }
    response = requests.get(search_url, headers=headers, params=query_params)
    results = response.json()
    tracks = results['tracks']['items']
    if tracks:
        for track in tracks:
            # Vérifier que le nom de l'artiste et le titre correspondent exactement
            if track_name.lower() in track['name'].lower() and any(artist_name.lower() in artist['name'].lower() for artist in track['artists']):
                return track['id'], track['name'], track['artists'][0]['name'], track['preview_url']
    return None, None, None, None


def get_track_features(track_id, access_token):
    track_features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(track_features_url, headers=headers)
    return response.json()

access_token = get_access_token(client_id, client_secret)

track_id, found_track_name, found_artist_name, preview_url = search_track("La vie qu'on mène", "Ninh", access_token)
if track_id:
    print(f"Found track ID: {track_id}")
    print(f"Track name: {found_track_name}")
    print(f"Artist name: {found_artist_name}")
    print(f"Preview URL: {preview_url}")
    track_features = get_track_features(track_id, access_token)
    print(track_features)
else:
    print("No track found matching the criteria.")

def search_artist_barre_recherche(artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    query_params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 10  # Limite à 10 résultats pour obtenir une liste des artistes pertinents
    }
    response = requests.get(search_url, headers=headers, params=query_params)
    results = response.json()
    artists_info = []

    # Parcourir chaque artiste trouvé et collecter les noms et genres
    for artist in results['artists']['items']:
        artist_info = {
            'name': artist['name'],
            'genres': artist['genres'],
            'popularity': artist['popularity'],
            'image_url': artist['images'][0]['url'] if artist['images'] else None  # Si des images sont disponibles, prendre la première
        }
        artists_info.append(artist_info)

    return artists_info

def search_artist_image(artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    query_params = {
        'q': f'artist:{artist_name}',
        'type': 'artist',
        'limit': 1  
    }
    response = requests.get(search_url, headers=headers, params=query_params)
    results = response.json()
    
    if results['artists']['items']:
        artist = results['artists']['items'][0]  
        artist_name = artist['name']
        artist_image_url = artist['images'][0]['url'] if artist['images'] else 'Aucune image trouvée'
        return artist_image_url
    
    return None, None
    
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
    if results['artists']['items']:
        artist = results['artists']['items'][0]  
        artist_name = artist['name']
        artist_image_url = artist['images'][0]['url'] if artist['images'] else 'Aucune image trouvée'
    artists = results['artists']['items']
    following = results['artists']['items'][0]['followers']['total']
    if artists and following :
        artist_id = artists[0]['id']
        return artist_id, artist_name, artists[0]['popularity'], artists[0]['genres'], following, artist_image_url
    return None, None, None, None

