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
💻 Usage
1️⃣ Configure Your Credentials

Update the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI in the script:

python
Copy
Edit
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8888/callback'
2️⃣ Run the Script

bash
Copy
Edit
python spotify_auth_test.py
3️⃣ Authenticate via Browser

A browser window will open. Log into your Spotify account and grant access.

4️⃣ See Your Spotify Profile Info

If authentication is successful, you’ll see output like:

pgsql
Copy
Edit
Logged in as: YourSpotifyName
🔧 Next Steps
✅ Scrape all your playlists and tracks
✅ Save data to CSV or database
✅ Add audio features and analytics
✅ Build a web interface for exploring your music data

📄 License
MIT License

🙌 Acknowledgments
Spotipy for the Spotify Web API wrapper

Spotify Web API
