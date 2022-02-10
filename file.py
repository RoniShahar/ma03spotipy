import configparser
import json
import logging
import zipfile

from music.album import Album
from music.artist import Artist
from music.song import Song
from music.spotify_content import SpotifyContent


def read_config_file(path, section, parameter):
    parser = configparser.ConfigParser()
    parser.read(path)
    return parser.get(section, parameter)


# logging.basicConfig(filename=read_config_file('properties.properties', 'config', 'logs_file_path'), level=logging.DEBUG, format='%(asctiome)s - %(funcName)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=read_config_file('properties.properties', 'config', 'logs_file_path'), level=logging.DEBUG)


def open_files_in_zip_file(file_path):
    zip_file = zipfile.ZipFile(file_path)
    logging.debug(f'the zip file: {file_path} opened')
    for file_info in zip_file.infolist():
        file = zip_file.open(file_info)
        load_json_file(file)


def load_json_file(file):
    def_object_by_file_content(json.load(file))
    file.close()


def def_object_by_file_content(song_details):
    song = Song(song_details['track']['id'], song_details['track']['name'], song_details['track']['popularity'])
    SpotifyContent.add_song(song)
    logging.debug(f'the song: {song.name} created')

    album = Album(song_details['track']['album']['id'], song_details['track']['album']['name'])
    SpotifyContent.add_album(album, song)
    logging.debug(f'the album: {album.name} created')

    artist = Artist(song_details['track']['artists'][0]['id'], song_details['track']['artists'][0]['name'])
    SpotifyContent.add_artist(artist, album)
    logging.debug(f'the artist: {artist.name} created')


def load_file(path, message="file not exist"):
    try:
        file = open(path)
        return json.load(file)
    except:
        print(message)
        return None


"""def write_to_users_file():
    json_string1 = json.dumps(User("roni").__dict__, indent=2)
    json_string2 = json.dumps(User("amit").__dict__, indent=2)
    with open('roni', 'w') as users_file:
        users_file.write(json_string1)

    with open('amit', 'w') as users_file:
        users_file.write(json_string1)"""
