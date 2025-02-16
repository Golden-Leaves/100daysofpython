import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import datetime
import pprint
print = pprint.pprint
#TODO: Abandoned as of 12/25/2024 to due unclear requirements and buggy as apis(?), may return later. P.S maybe include artist info
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET= os.getenv("SPOTIFY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")
    
    while True:
        global print
        try:
            song_period = input("Enter the time period for songs(YYYY-MM-DD): ")
            formatted_song_period = datetime.date(year=int(song_period.split("-")[0]),month=int(song_period.split("-")[1]),day = int(song_period.split("-")[2]))

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
            response = requests.get(f"https://www.billboard.com/charts/hot-100/{formatted_song_period}/",headers=headers)
            billboard100_webpage = response.text
            soup = BeautifulSoup(billboard100_webpage,"html.parser")
            song_titles = [song.get_text(strip=True) for song in soup.select(selector="li ul li h3")]
            
            scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read"
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))
            spotipy_uri_list = []
            for title in song_titles:
                results = sp.search(q=f"track:{title} year:{song_period.split("-")[0]}", type="track")
                print(results)
                for track in results['tracks']['items']:
                    print(track['name'], track['artists'][0]['name'])
                print("PLACEHOLDER")

  
            break
        except ValueError :
            print("Incorrect date format entered, please try again.")
            continue
            

    print("DEBUG STOP")
if __name__ == "__main__":
    main()