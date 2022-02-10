from music.song import Song


class Album:
    def __init__(self, album_id, name):
        self.id = album_id
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
