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

    @staticmethod
    def is_song_exist(song_name: str):
        for s in SpotifyContent.songs:
            if song_name == s.name:
                return s, True
        return None, False

    @staticmethod
    def is_artist_exist(artist_name: str):
        for artist in SpotifyContent.artists:
            if artist_name == artist.name:
                return artist.albums, True
        return None, False

    @staticmethod
    def is_album_exist(album_name: str):
        for album in SpotifyContent.albums:
            if album_name == album.name:
                return album.songs, True
        return None, False
