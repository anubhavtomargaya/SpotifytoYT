
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f82b1ec8efbe4046be621bff39f31ff9",
                                                           client_secret="89fe075de282419eaff569d56a8af2a6"))

# results = sp.search(q='atif', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
    # print(idx, track['name'])

playlist = sp.playlist(playlist_id="19Qd1TPko613J71jdkNKnP")
for u in range(len(playlist)-1):
    print(playlist['tracks']['items'][u]['track']['name'])

# print(playlist['tracks']['items'][0]['track']['name'])
# print(playlist['tracks']['items'][0]['track']['album']['name'])
# print(playlist['tracks']['items'][0]['track']['artists'][0]['name'])