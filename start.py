import spotipy
from credentials import my_client_id, my_client_secret

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=my_client_id, client_secret=my_client_secret
    )
)

# results = sp.search(q='atif', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
# print(idx, track['name'])

playlist = sp.playlist(playlist_id="19Qd1TPko613J71jdkNKnP")
for u in range(len(playlist) - 1):
    print(playlist["tracks"]["items"][u]["track"]["name"])

# print(playlist['tracks']['items'][0]['track']['name'])
# print(playlist['tracks']['items'][0]['track']['album']['name'])
# print(playlist['tracks']['items'][0]['track']['artists'][0]['name'])
