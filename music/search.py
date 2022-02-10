from music.spotify_content import SpotifyContent


def get_all_artists():
    artists = []
    for artist in SpotifyContent.artists:
        artists.append(artist.name)
    print_sorted(artists)


def get_artist_albums():
    artist_name = input("Enter artist name: ")
    albums, is_artist_exist = SpotifyContent.is_artist_exist(artist_name)
    if is_artist_exist:
        print_sorted(list(map((lambda x: x.name), albums)))
    else:
        print("sorry, artist not exist :(")


def get_top_ten_songs_of_artist(num_of_returned_record=10):
    artist_name = input("Enter artist name: ")
    songs = []
    for artist in SpotifyContent.artists:
        if artist.name == artist_name:
            for album in artist.albums:
                for song in album.songs:
                    songs.append(song)
    songs = sorted(songs, key=lambda x: x.popularity, reverse=True)[:num_of_returned_record]
    print(list(map((lambda x: x.name), songs)))


def get_album_songs():
    album_name = input("Enter album name: ")
    songs, is_album_exist = SpotifyContent.is_album_exist(album_name)
    if is_album_exist:
        print_sorted(list(map((lambda x: x.name), songs)))
    else:
        print("sorry, album not exist :(")


def print_sorted(list, sep="\n"):
    list.sort()
    print(*list, sep=sep)

