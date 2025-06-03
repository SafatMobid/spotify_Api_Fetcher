import spotipy
from spotipy.oauth2 import SpotifyOAuth

#-----------CONFIG TO ACCESS ACCOUNT-------------------#

CLIENT_ID = "yourClientID"
CLIENT_SECRET = "yorClientSecret"
REDIRECT_URL = "http://127.0.0.1:8000/callback"
SCOPE = 'playlist-read-private' #-------> Used to get to playlist

#------------AUTH TO LOG IN ------------------#
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=SCOPE))  #Access to the API

# -----------------TEST-----------------#
# Get current user info
user = sp.current_user()
print(f"Logged in as: {user['display_name']} ({user['id']})")

# Get a list of the playlists
playlists = sp.current_user_playlists()
for playlist in playlists['items']:

# To try to handle non standard playlist names (i.e Playlist with emojis)
    try:
        name = playlist['name']
        print(f"- {name} (ID: {playlist['id']})")
    except UnicodeEncodeError:
        print(f"- [undefined playlist name] (ID: {playlist['id']})") #Got it to work but it will define all unreadable playlist name as undefined