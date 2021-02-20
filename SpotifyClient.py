from SpotifyAPI import *

client_id = 'cff101e2e4334f3ea74a73ca652a96c6'
client_secret = '764736f71c5c49ec8009befd251e7576'

spotify = SpotifyAPI(client_id, client_secret)

def get_auth_link(redirect):
    link = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect}&scope=user-top-read&state=34fFs29kd09&show_dialog=true"
    return link

def get_user_access_tokens(auth_code, redirect):
    return spotify.get_user_access_tokens(auth_code, redirect)

def get_top_tracks(access_token, time_range):
    return spotify.get_top_tracks(access_token, time_range)