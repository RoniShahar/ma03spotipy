from music.album import Album


class Artist:
    def __init__(self, artist_id, name):
        self.id = artist_id
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        self.albums.append(album)
