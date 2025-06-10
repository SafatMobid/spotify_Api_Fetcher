🎵 Spotify Playlist Scraper


A simple Python script to authenticate with the Spotify API using OAuth and fetch your Spotify profile information. This is the first step toward building a playlist and track scraper.

🚀 Features
Authenticate with the Spotify API using OAuth 2.0

Fetch and display your Spotify profile information (e.g., display name, user ID)

Lay the foundation for scraping playlists and tracks

📦 Requirements
Python 3.7+

Spotipy (Spotify Web API wrapper for Python)

A Spotify Developer Account

🔑 Setup
1️⃣ Create a Spotify Developer App

Go to the Spotify Developer Dashboard

Log in and create a new app

Save your:

Client ID

Client Secret

Redirect URI (e.g., http://localhost:8888/callback)

2️⃣ Install Dependencies

bash
Copy
Edit
pip install spotipy


1. Configure Your Credentials

Update the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI in the script:

python
Copy
Edit
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8000/callback'

2. Run the Script

bash
Copy
Edit

python spotify_auth_test.py
3. Authenticate via Browser

A browser window will open. Log into your Spotify account and grant access.

4. See Your Spotify Profile Info
Your top 5 songs
Playlist Names + Songs

TO BE ADDED:
Exporting it all to a CSV File


📄 License
MIT License

🙌 Acknowledgments
Spotipy for the Spotify Web API wrapper

Spotify Web API
