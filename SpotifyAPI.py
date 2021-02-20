
import requests
import datetime
import json
from urllib.parse import urlencode

class SpotifyAPI(object):
    client_id = None
    client_secret = None

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_user_access_tokens(self, auth_code, redirect):
        url = "https://accounts.spotify.com/api/token"
        data = {
            'grant_type' : 'authorization_code',
            'code' : auth_code,
            'redirect_uri' : redirect,
        }
        r = requests.post(url, auth=(self.client_id, self.client_secret), data=data)
        request_data = r.json()
        tokens = {
            'access_token' : request_data.get('access_token'),
            'refresh_token' : request_data.get('refresh_token')
        }
        return tokens


    def get_top_tracks(self, access_token, time_range):
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
        endpoint = "https://api.spotify.com/v1/me/top/artists"
        data = urlencode({"time_range": time_range, "limit": 10})

        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=headers)

        r_data = r.json()

        #Create list of dictionaries with the artist's name, an image of them, and their popularity score
        artist_info = []
        for item in r_data['items']:
            artist_info.append({'name' : item['name'], 'image' : item['images'][0]['url'], 'popularity' : item['popularity'], 'popularity_rank': "none"})

        #Find the most popular artist based off of poularity score
        min = -1
        index = 0
        for i in range(10):
            if artist_info[i]['popularity'] > min:
                min = artist_info[i]['popularity']
                index = i
        artist_info[index]['popularity_rank'] = "most"  

        #Now find the least popular
        max = 101
        for i in range(10):
            if artist_info[i]['popularity'] < min:
                min = artist_info[i]['popularity']
                index = i
        artist_info[index]['popularity_rank'] = "least"  

        return artist_info


