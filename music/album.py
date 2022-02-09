from music.song import Song


class Album:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
