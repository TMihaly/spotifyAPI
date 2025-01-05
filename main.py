import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Nincs benne a client_id-m és client_secretem adatvédelem miatt, ez a filehívás kihagyható

with open("spotifyapicr/client_resources.txt", "r") as client_data:
    lines = client_data.readlines()
lines = str(lines)
inputs = lines.split(',')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=inputs[0], # ezekhez ""-ben a client_id és a secret, ha nem akarsz külön mappát meghívni, akkor a felsőt törölni kell
    client_secret=inputs[1],
    redirect_uri="http://localhost:8000/callback", # callback a spotify authenticatornek
    scope="user-library-read user-top-read" # jogok
))


artist = sp.current_user_top_artists(3) # 2 <- ennyit vesz ki vizsgálatra, max 20


if isinstance(artist, dict):  
    for item in artist["items"]:
        print(item["name"])
        