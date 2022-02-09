from album import Album


class Artist:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        self.albums.append(album)