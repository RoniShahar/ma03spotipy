from music.spotify_content import SpotifyContent


def get_all_artists():
    artists = []
    for artist in SpotifyContent.artists:
        artists.append(artist.name)
    return artists


def get_artist_albums(artist_id):
    albums = []
    for artist in SpotifyContent.artists:
        if artist.id == artist_id:
            for album in artist.albums:
                albums.append(album.name)


def get_top_ten_songs_of_artist(artist_id, num_of_returned_record=10):
    songs = []
    for artist in SpotifyContent.artists:
        if artist.id == artist_id:
            for album in artist.albums:
                for song in album:
                    songs.append(song)

    return sorted(songs, key=lambda x: x.popularity, reverse=True)[:num_of_returned_record]


def get_album_songs(album_id):
    songs = []
    for album in SpotifyContent.albums:
        if (album.id == album_id):
            for song in album:
                songs.append(song)
    return songs
