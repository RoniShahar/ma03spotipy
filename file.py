import configparser
import json
import logging
import zipfile

from music.album import Album
from music.artist import Artist
from music.song import Song
from music.spotify_content import SpotifyContent


def read_config_file(parameter, section='config', path='properties.properties'):
    parser = configparser.ConfigParser()
    parser.read(path)
    return parser.get(section, parameter)


logging.basicConfig(filename=read_config_file(parameter='logs_file_path'), level=logging.DEBUG)


def open_files_in_zip_file(file_path):
    zip_file = zipfile.ZipFile(file_path)
    logging.debug(f'the zip file: {file_path} opened')
    for file_info in zip_file.infolist():
        file = zip_file.open(file_info)
        def_music_object_by_file_content(json.load(file))
        file.close()


def def_music_object_by_file_content(song_details):
    song = song_details['track']
    album = song['album']
    artist = song['artists'][0]

    song = Song(song['id'], song['name'], song['popularity'])
    SpotifyContent.add_song(song)
    logging.debug(f'the song: {song.name} created')

    album = Album(album['id'], album['name'])
    SpotifyContent.add_album(album, song)
    logging.debug(f'the album: {album.name} created')

    artist = Artist(artist['id'], artist['name'])
    SpotifyContent.add_artist(artist, album)
    logging.debug(f'the artist: {artist.name} created')


def load_file(path, message="file not exist"):
    try:
        file = open(path)
        return json.load(file)
    except:
        print(message)
        return None
