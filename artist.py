from album import Album


class Artist():

    def __init__(self, id, name, albums: list[Album]):
        self.id = id
        self.name = name
        self.albums = albums
