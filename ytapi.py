from distutils.command.build import build
from re import search
from googleapiclient.discovery import build
from credentials import yt_api,yt_client_secrent,yt_client_id
import json
from spotify_extract import query_builder
import time



def makePublicService(api_key):
    service = build(serviceName='youtube',version='v3',developerKey=api_key)
    return service


# queries = ['Tere Mast Mast Do Nain Dabangg Rahat Fateh Ali Khan', 'Rishte Naate - From "De Dana Dan" Tera Mera Saath Ho Rahat Fateh Ali Khan', 'Sanu Ek Pal Chain (From "Raid") Sanu Ek Pal Chain (From "Raid") Rahat Fateh Ali Khan', 'Aas Paas Khuda Anjaana Anjaani Rahat Fateh Ali Khan', 'Dil To Bachcha Hai Ishqiya Rahat Fateh Ali Khan', 'Yeh Jo Halki Halki Khumariya Son Of Sardaar Rahat Fateh Ali Khan', 'Milegi Milegi (From "Stree") Milegi Milegi (From "Stree") Mika Singh', 'Tu Mera Hero Desi Boyz Pritam', 'Jugni Tanu Weds Manu Mika Singh', 'Saawan Mein Lag Gayee Aag Saawan Mein Lag Gayee Aag Mika Singh', 'Jumme Ki Raat Kick Mika Singh', 'Dagabaaz Re Dabangg 2 Rahat Fateh Ali Khan', 'Pungi Agent Vinod Pritam', 'Tu Mere Agal Bagal Hai Phata Poster Nikhla Hero (Original Motion Picture Soundtrack) Mika Singh']

def getVideoIds(queris,api):
    service = makePublicService(api)
    ids = []
    for i in range(len(queris)):
        request = service.search().list(part="snippet",
                maxResults=2,
                q = queris[i]
            )
        response = request.execute()
        videoid = response['items'][0]['id']['videoId']
        print(videoid)

        ids.append(videoid)
        time.sleep(3)
    return ids

# print(getVideoIds(queries))
# req_vdo = service.videos().list(part='snippet', id=id)

# x = req_vdo.execute()
# y = json.dumps(x)
# print(y)

