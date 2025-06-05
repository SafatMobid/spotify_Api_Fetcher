import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#-----------CONFIG TO ACCESS ACCOUNT-------------------#
config = configparser.ConfigParser()
config.read("config.ini")

CLIENT_ID = config["auth"]["Client_ID"]
CLIENT_SECRET = config["auth"]["Client_Secret"]
REDIRECT_URI = "http://127.0.0.1:8000/callback"
SCOPE = "playlist-read-private user-read-recently-played user-top-read" #-------> Used to give permission on what to access

#------------AUTH TO LOG IN------------------#
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))  #Access to the API

# -----------------TEST to confirm user log in-----------------#
# Get current user info
user = sp.current_user()
print(f"Logged in as: {user["display_name"]} ({user["id"]})")
    
# # TEST to see if I can get top 5 song - Works
# # Just for fun
top_songs = sp.current_user_top_tracks(limit=5, time_range="short_term") # short_term = 4 weeks, medium_term = 6 months, long_term = couple of years
print("Your Top 5 Tracks Right Now:")
for i, item in enumerate(top_songs["items"], start=1):
    track_name = item["name"]
    artists = ", ".join(artist["name"] for artist in item["artists"])
    print(f"{i}. {track_name} by {artists}")

#------------GETTING PLAYLISTS------------------#

# Get a list of the playlists
print("Your Playlists:")
playlists = sp.current_user_playlists()
for playlist in playlists["items"]:   

# To try to handle non standard playlist names (i.e Playlist with emojis)
    try:
        name = playlist["name"]
        print(f"- {name} (ID: {playlist["id"]})")
    except UnicodeEncodeError:
        print(f"- [undefined playlist name] (ID: {playlist["id"]})") #Got it to work but it will define all unreadable playlist name as undefined

#---------------SONGS-----------------------------------#

    # Get songs from the playlist
    results = sp.playlist_items(playlist["id"])
    
    # Loop through each track
    for item in results['items']:
        track = item['track']
        if track:  # Some may be None (e.g. removed tracks)
            song_name = track['name']
            artists = ", ".join([artist['name'] for artist in track['artists']])
            print(f"   - {song_name} by {artists}")

# need to fix error when it is not a song(i.e podcast, removed song)"

