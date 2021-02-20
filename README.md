
# Spotify Stats

A flask app to see your top Spotify artists of all time.

## Requirements
- Python 3.6+

## Registration

You will need to create a Spotify developer account at https://developer.spotify.com/ and create a new app to use their API
- Then you will need to [register](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app) your application with ``http://localhost:8000/callback`` as the redirect URI.

## Setup
Clone the repository to your device.

You will need to install the following packages with `pip`:
`pip install flask`
`pip install requests`

Next, create a virtual environment and set required environment variables in your Python shell:
    ` venv/Scripts/activate`
    
   Then, if you are in Windows terminal:
    `set FLASK_APP=hello.py`
    
   Or if you're using PowerShell:
    `$env:FLASK_APP = "flask_server.py"`

    

## Usage
Before running the program, you must set it up so it can connect with the Spotify API.

 In `SpotifyClient.py` fill in the variables `client_id` and `client_secret` with your client id and client secret that can be accessed at https://developer.spotify.com/dashboard/applications after you create an app.
```
client_id = "YOUR CLIENT ID HERE"
client_secret = "YOUR CLIENT SECRET HERE"
```
Now the program is ready to run:
1) Run the following command. `flask run -h localhost -p8000`

2) Access `http://localhost:8000/` in your browser and login.
