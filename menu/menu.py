from consolemenu import *
from consolemenu.items import FunctionItem
from user.user import *
from music.search import *


def login_menu():
    from user.user import check_if_user_exist
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
    item3 = FunctionItem("show top 10 songs of artist", get_top_songs_of_artist)
    item4 = FunctionItem("look for songs by album", get_album_songs)
    item5 = FunctionItem("return to main menu", advanced_menu)
    menu.append_item(item1)
    menu.append_item(item2)
    menu.append_item(item3)
    menu.append_item(item4)
    menu.append_item(item5)
    menu.show()
