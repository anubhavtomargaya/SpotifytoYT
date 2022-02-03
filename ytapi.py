from distutils.command.build import build
from re import search
from googleapiclient.discovery import build
from credentials import yt_api,yt_client_secrent,yt_client_id
import json

service = build(serviceName='youtube',version='v3',developerKey=yt_api)

request = service.search().list(part="snippet",
        maxResults=2,
        q = 'Rishte Naate - From "De Dana Dan" Tera Mera Saath Ho Rahat Fateh Ali Khan'
    )

response = request.execute()

id = response['items'][0]['id']['videoId']
print(id)

req_vdo = service.videos().list(part='snippet', id=id)
x = req_vdo.execute()

y = json.dumps(x)
print(y)