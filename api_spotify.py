#client id : d93d4a8bdb184e898082ab907dc313b4
#client secret : 1c72f524f0e24c2787c945e9c3f5df54

import requests
client_id = "d93d4a8bdb184e898082ab907dc313b4"
client_secret = "1c72f524f0e24c2787c945e9c3f5df54"
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