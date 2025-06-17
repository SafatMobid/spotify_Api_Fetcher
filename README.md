🎵 Spotify API Fetcher

+++++ FOR SPOTIFY USER DATA +++++

I chose this project to dive deeper into working with external APIs, particularly one I personally use and enjoy. Spotify's API offered a great opportunity to combine my interest in music with Python, while learning about OAuth authentication and structured data extraction.

This Python script uses the Spotify Web API to authenticate a user and fetch personal Spotify data, such as profile information, playlists, and top tracks. It serves as the foundational step for a more advanced playlist and track scraper.

Great for understanding how OAuth 2.0 works in real applications

Useful introduction to working with third-party APIs

Bridges personal interest with technical learning

🚀 Features:

Authenticate with the Spotify API using OAuth 2.0

Fetch and display user profile information (e.g., display name, user ID)

Retrieve and display playlist names and top 5 tracks

Lays groundwork for playlist and track data scraping

📦 Requirements:

Python 3.7+

spotipy (Spotify Web API wrapper for Python)

A Spotify Developer Account

🔧 Setup Instructions:

1️⃣ Create a Spotify Developer App

Go to the Spotify Developer Dashboard

Create a new app and note down:

Client ID

Client Secret

Redirect URI (e.g., http://localhost:8000/callback)

2️⃣ Install Dependencies

bash
Copy
Edit
pip install spotipy
3️⃣ Configure Your Credentials
Update your script:

python
Copy
Edit
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8000/callback'
4️⃣ Run the Script

bash
Copy
Edit
python spotify_auth_test.py
5️⃣ Authenticate via Browser
Log into your Spotify account and authorize the app when the browser opens.

6️⃣ See Your Spotify Data

View your display name, user ID

List your playlists and top 5 songs

🗂️ TO BE ADDED:

Export playlist and track data to a CSV file

Automatically refresh access token

Build a simple web or GUI interface to explore scraped data

📄 License:
MIT License

🙌 Acknowledgments:
Thanks to Spotipy for simplifying interaction with the Spotify Web API

By working on this, I gained hands-on experience with API authentication, data parsing, and token-based security flows. It also expanded my understanding of how to use third-party libraries and prepare for more complex data extraction and automation workflows.
