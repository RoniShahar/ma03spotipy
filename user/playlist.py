from music.song import Song


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
