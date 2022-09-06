import requests 
import base64 # used to encode binary data to ASCII chars
import json
from secrets import clientSecret, clientID
authurl = "https://accounts.spotify.com/api/token"
authheaders = {}
authdata = {}

def getAccessToken(clientID, clientSecret):
    message=f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii') #base64 encoded to handle messages not being corrupted
                                                #when transmitted so it can be processed correctly
    authheaders['Authorization'] = "Basic " + base64_message
    authdata['grant_type'] = "client_credentials"
    res = requests.post(authurl, headers=authheaders, data=authdata)

    responseObject = res.json()
    #print(json.dumps(responseObject, indent=2))

    accessToken = responseObject['access_token']

    return accessToken

def getPlaylistTracks(token, playlistID):

    playlistEndPoint=f"https://api.spotify.com/v1/playlists/{playlistID}"
    getHeader= {
        "Authorization": "Bearer " + token
    }
    res = requests.get(playlistEndPoint,headers=getHeader)
    playlistObject = res.json()

    return playlistObject
#API requests
token = getAccessToken(clientID, clientSecret)
playlistID = "6bPeS26FtfWK0a8rLZhCja?si=e148690db0ec4725" #copy id of your spotify playlist

tracklist = getPlaylistTracks(token, playlistID)
# print(json.dumps(tracklist, indent=2))
# with open('tracklist.json', 'w') as f:
   # json.dump(tracklist, f) #this opens the tracklist.json data structure as a file

for t in tracklist['tracks']['items']:
    print('-----------------------')
    for a in t['track']['artists']:
        print(a['name'])
   # artist = t['track']['artist'][0]
    songName = t['track']['name']
    print(songName)
