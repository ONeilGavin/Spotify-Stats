from flask import Flask, render_template, request, redirect, url_for
import SpotifyClient
import requests

app = Flask(__name__)
redirect_uri = "http://localhost:8000/callback"


@app.route('/')
def index():
    #Get link that will be used to take the user to the sign in page
    auth_link = SpotifyClient.get_auth_link(redirect_uri)
    return render_template('index.html', auth_link=auth_link)

@app.route('/callback')
def callback():
    #If the user does not agree to authenticate on Spotify's side
    if request.args.get('error', type = str) == "access_denied":
        #Get a new auth link for the request
        auth_link = SpotifyClient.get_auth_link(redirect_uri)
        return render_template('error.html', auth_link=auth_link)

    #Pull authorization code from url to be used in getting the access token
    auth_code = request.args.get('code', default = '', type = str)
    access_tokens = SpotifyClient.get_user_access_tokens(auth_code, redirect_uri)

    artist_info = SpotifyClient.get_top_tracks(access_tokens['access_token'], 'long_term')
    return render_template('toptracks.html', info=artist_info)

def top_tracks(info):
    return render_template('toptracks.html', info=info)


