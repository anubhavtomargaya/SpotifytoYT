from audioop import add
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from spotify_extract import query_builder

credentials = None

# token.pickle stores the user's credentials from previously successful logins
if os.path.exists('token.pickle'):
    print('Loading Credentials From File...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=[
                'https://www.googleapis.com/auth/youtube'
            ]
        )

        flow.run_local_server(port=8080, prompt='consent',
                              authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)

service = build(serviceName='youtube',version='v3',credentials=credentials)

def makePlaylist(serv,name):
    request = youtube.playlists().insert(
        part="snippet",
        body={
            "snippet": {
            "title": name
            }
        }
    )

    response = request.execute()
    return response.id


test_pl_id = 'PLZ_InQ-iKUHOM2w4K-5OyER_gYul7F-2s'
video_ids = ['oyLVu753XJw', 'rQeUwx7IKFo', '13z2kF6TiCc', 'jAUSF4_ygJg', 'BlHjfL0pcsw', 'utmSky40VCc', '1xYZeDReUz4', 'Y7G-tYRzwYY', '6ZnnjW6Jj1g', '82eGj8wpzoo', 'dv_Qjzca56k', '0KozfDYK1EU', 'Sjh1PQ9B73Y', 'vcH5RCEzyD0']


def addItemToPlaylist(pl_id,items):
    res = []
    for i in items:
        request = service.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                "playlistId": pl_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": i
                }
                }
            }
        )
        response = request.execute()
        print("Added")
        res.append(response)
    
    return res

addItemToPlaylist(test_pl_id,video_ids)