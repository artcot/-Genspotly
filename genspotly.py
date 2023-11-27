import spotipy
import spotipy.util as util
import lyricsgenius
from lyricsgenius import Genius
from deep_translator import GoogleTranslator
from credentials import USERNAME, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, GENIUS_CLIENT_ID, GENIUS_CLIENT_SECRET, GENIUS_ACCESS_TOKEN

scope = 'user-read-currently-playing'

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

try:
    sp = spotipy.Spotify(auth=sp_token)
except:
    sp_token = util.prompt_for_user_token(USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
    sp = spotipy.Spotify(auth=sp_token)

current_song = sp.currently_playing()
if current_song:
    sp_artist = current_song['item']['artists'][0]['name']
    name_song = current_song['item']['name']
else:
    print("Spotify not playing")

#print(sp_artist + " - " + name_song)

song_lyrics = genius.search_song(name_song, artist=sp_artist)

print(song_lyrics.lyrics)

translated_lyrics = GoogleTranslator(source="auto", target="ru").translate(song_lyrics.lyrics)
print(translated_lyrics)
