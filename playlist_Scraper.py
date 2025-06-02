import spotipy
from spotipy.oauth2 import SpotifyOAuth

#-----------CONFIG TO ACCESS ACCOUNT-------------------#

CLIENT_ID = "yourClientID"
CLIENT_SECRET = "yorClientSecret"
REDIRECT_URL = "http://127.0.0.1/callback"
SCOPE = 'playlist-read-private' #-------> Used to get to playlist

#------------AUTH TO LOG IN ------------------#
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=SCOPE))

# -----------------TEST-----------------#
# Get current user info
user = sp.current_user()
print(f"Logged in as: {user['display_name']} ({user['id']})")