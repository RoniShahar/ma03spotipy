import zipfile
import json
from music.spotify_content import SpotifyContent
from music.song import Song
from music.album import Album
from music.artist import Artist


def open_files_in_zip_file(file_path):
    zip_file = zipfile.ZipFile(file_path)
    for file_info in zip_file.infolist():
        file = zip_file.open(file_info)
        read_json_file(file)


def read_json_file(file):
    song_details = json.load(file)
    song = Song(song_details['track']['id'], song_details['track']['name'], song_details['track']['popularity'])
    SpotifyContent.add_song(song)

    album = Album(song_details['track']['album']['id'], song_details['track']['album']['name'])
    SpotifyContent.add_album(album, song)

    artist = Artist(song_details['track']['artists'][0]['id'], song_details['track']['artists'][0]['name'])
    SpotifyContent.add_artist(artist, album)

    file.close()
