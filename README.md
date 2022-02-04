# SpotifytoYT

main - contains the main function that requires a playlist id from spotify 
spotify_extract - functions to connect to spotify api and extract the playlist's data into a list to make search queries on youtube. requires api keys of spotify (client id, secret)
ytOauth - functions that need private data access on youtube and require oAuth credentials(client_secrets.json). i.e. making playlist on  user's behalf, adding videos to it.
ytapi - functions that access public data on youtube. i.e. youtube search api to get video ids of tracks in spotify playlist. requires api key