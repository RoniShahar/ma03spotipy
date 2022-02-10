from file import load_file, read_config_file
from user.playlist import Playlist
from music.search import *
from config_values import ConfigValues
import logging

logging.basicConfig(filename=read_config_file(parameter='logs_file_path'), level=logging.DEBUG)


class User:
    user_name = ""
    playlists = []
    user_status = ""

    @staticmethod
    def add_playlist(playlist: Playlist):
        User.playlists.append(playlist)

    @staticmethod
    def is_playlist_exist(playlist_name: str):
        for index, playlist in enumerate(User.playlists):
            if playlist_name == playlist.name:
                return index, True
        return False

    @staticmethod
    def is_song_exist_in_given_playlist(playlist_index: int, song_id: str):
        for s_id in User.playlists.__getitem__(playlist_index).songs:
            if s_id == song_id:
                return True
        return False


def check_if_user_exist():
    from menu.menu import advanced_menu, login_menu
    user_name = input("enter your user name:")

    user_details = load_file(user_name, "this user name does not exist, you can try again or sign up :(")
    if user_details is not None:
        upload_user_details(user_details)
        logging.debug(f'user: {user_name} log in successfully')
        advanced_menu()
    else:
        login_menu()


def upload_user_details(user_details):
    User.user_name = user_details['user_name']
    User.user_status = user_details['status']

    for playlist in user_details['playlists']:
        user_playlist = Playlist(playlist['name'])
        for song in playlist['songs']:
            user_playlist.add_song(song)
        User.playlists.append(user_playlist)


def print_user_playlists():
    if User.user_name != "":
        if len(User.playlists) == 0:
            print("you don't have any playlist yet :(")
        else:
            for playlist in User.playlists:
                print(playlist.name)
                count = 1
                for p_song in playlist.songs:
                    for song in SpotifyContent.songs:
                        if song.id == p_song:
                            print(str(count) + '. ' + song.name)
                            count += 1


def add_new_playlist():
    if ((User.user_status == ConfigValues.free_user and (
            len(User.playlists) < ConfigValues.num_of_max_playlists_for_free_user)) or (
            User.user_status == ConfigValues.premium_user)):
        playlist_name = input("Enter name for your new playlist:")
        is_name_exist = False
        if User.user_name != "":
            for playlist in User.playlists:
                if playlist.name == playlist_name:
                    is_name_exist = True
        if is_name_exist:
            print("this name already exist, playlist cannot be created")
        else:
            User.playlists.append(Playlist(playlist_name))
            logging.debug(f'user: {User.user_name} add new playlist called {playlist_name}')
            print(f'{playlist_name} playlist added successfully!')
    else:
        print("You've reached your playlist quota, playlist cannot be created :(")


def add_song_to_playlist():
    playlist_name = input("Enter playlist name: ")
    song_name = input("Enter song name: ")
    s, is_song_exist_in_spotipy = SpotifyContent.is_song_exist(song_name)
    if not is_song_exist_in_spotipy:
        print(f'this song not exist in spotipy :(')
    else:
        index, is_playlist_exist = User.is_playlist_exist(playlist_name)
        if not is_playlist_exist:
            print(f'{playlist_name} playlist not exist')
        else:
            if ((User.user_status == ConfigValues.free_user and len(User.playlists[
                                                                        index].songs) < ConfigValues.num_of_max_songs_in_playlist_for_free_user) or User.user_status == ConfigValues.premium_user):
                is_song_exist_in_chosen_playlist = User.is_song_exist_in_given_playlist(index, s.id)
                if is_song_exist_in_chosen_playlist:
                    print(f'{song_name} already exist in {playlist_name} playlist')
                else:
                    User.playlists[index].add_song(s.id)
                    logging.debug(f'user: {User.user_name} add new song called {song_name} to {playlist_name} playlist')
                    print(f'{song_name} added to {playlist_name} playlist successfully!')
            else:
                print("You've reached your songs quota in this playlist, song cannot be added :(")


def logout():
    # write user playlist to file
    logging.debug(f'user: {User.user_name} log out successfully')
    User.user_name = ""
    User.playlists = []
    User.user_status = ""
