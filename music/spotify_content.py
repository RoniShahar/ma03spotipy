from music.song import Song
from music.album import Album
from music.artist import Artist


class SpotifyContent:
    songs = []
    albums = []
    artists = []

    @staticmethod
    def add_song(song: Song):
        if song not in SpotifyContent.songs:
            SpotifyContent.songs.append(song)

    @staticmethod
    def add_album(album: Album, song: Song):
        if album not in SpotifyContent.albums:
            album.add_song(song)
            SpotifyContent.albums.append(album)
        else:
            for i, exist_album in enumerate(SpotifyContent.albums):
                if exist_album.id == album.id:
                    SpotifyContent.albums[i].add_song(song)

    @staticmethod
    def add_artist(artist: Artist, album: Album):
        if artist not in SpotifyContent.artists:
            artist.add_album(album)
            SpotifyContent.artists.append(artist)
        else:
            for i, exist_artist in enumerate(SpotifyContent.artists):
                if exist_artist.id == artist.id:
                    SpotifyContent.artists[i].add_album(album)