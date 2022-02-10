from file import load_file
from menu.menu import *
from music.song import Song
from music.spotify_content import SpotifyContent
from user.playlist import Playlist
from music.search import *


def login_menu():
    menu = ConsoleMenu("Login")
    login_item = FunctionItem("Login", check_if_user_exist, should_exit=True)
    menu.append_item(login_item)
    menu.show()


def advanced_menu():
    menu = ConsoleMenu('Welcome to Spotipy', show_exit_option=False)
    item1 = FunctionItem("See existing playlists", print_user_playlists)
    item2 = FunctionItem("add new playlist", add_new_playlist)
    item3 = FunctionItem("add song to playlist", add_song_to_playlist)
    item4 = FunctionItem("search in spotipy", search_menu)
    item5 = FunctionItem("logout", logout, should_exit=True)
    menu.append_item(item1)
    menu.append_item(item2)
    menu.append_item(item3)
    menu.append_item(item4)
    menu.append_item(item5)
    menu.show()

def search_menu():
    menu = ConsoleMenu('Welcome to Spotipy', show_exit_option=False)
    item1 = FunctionItem("show all artists in spotipy", get_all_artists)
    item2 = FunctionItem("look for albums by artist", get_artist_albums)
    item3 = FunctionItem("show top 10 songs of artist", get_top_ten_songs_of_artist)
    item4 = FunctionItem("look for songs by album", get_album_songs)
    item5 = FunctionItem("return to main menu", advanced_menu)
    menu.append_item(item1)
    menu.append_item(item2)
    menu.append_item(item3)
    menu.append_item(item4)
    menu.append_item(item5)
    menu.show()



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
    user_name = input("enter your user name:")

    user_details = load_file(user_name, "this user name does not exist, you can try again or sign up :(")
    if user_details is not None:
        upload_user_details(user_details)
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
    playlist_name = input("Enter name for your new playlist:")
    is_name_exist = False
    if User.user_name != "":
        for playlist in User.playlists:
            if playlist.name == playlist_name:
                is_name_exist = True

    if is_name_exist:
        print("this name already exist, playlist cannot be created")
        advanced_menu()
    else:
        User.playlists.append(Playlist(playlist))


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
            is_song_exist_in_chosen_playlist = User.is_song_exist_in_given_playlist(index, s.id)
            if is_song_exist_in_chosen_playlist:
                print(f'{song_name} already exist in {playlist_name} playlist')
            else:
                User.playlists[index].add_song(s.id)


def logout():
    #write to file user playlist
    User.user_name = ""
    User.playlists = []
    User.user_status = ""