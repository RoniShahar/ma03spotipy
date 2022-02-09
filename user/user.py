from user.playlist import Playlist


class User:

    def __init__(self, user_name):
        self.user_name = user_name
        self.playlists = []

    def add_playlist(self, playlist: Playlist):
        self.playlists.append(playlist)
