from song import Song


class Album():

    def __init__(self, id, name, songs: list[Song]):
        self.id = id
        self.name = name
        self.songs = songs
