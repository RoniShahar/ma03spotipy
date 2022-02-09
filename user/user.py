from file import load_file
from user.playlist import Playlist


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.playlists = []

    def add_playlist(self, playlist: Playlist):
        self.playlists.append(playlist)


def check_if_user_exist():
    user_name = input("enter your user name:")

    try:
        load_file(user_name, "this user name does not exist, you can try again or sign up :(")
    except:
        print("")

