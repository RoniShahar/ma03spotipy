from config_values import ConfigValues
from music.spotify_content import SpotifyContent


def get_all_artists():
    artists = set()
    for artist in SpotifyContent.artists:
        artists.add(artist.name)
    print_sorted(list(artists))


def get_artist_albums():
    artist_name = input("Enter artist name: ")
    albums, is_artist_exist = SpotifyContent.is_artist_exist(artist_name)
    if is_artist_exist:
        print_sorted(list(map((lambda x: x.name), albums)))
    else:
        print("sorry, artist not exist :(")


def get_top_songs_of_artist():
    from user.user import User
    num_of_returned_record = ConfigValues.num_of_top_songs_to_display
    artist_name = input("Enter artist name: ")
    songs = []
    for artist in SpotifyContent.artists:
        if artist.name == artist_name:
            for album in artist.albums:
                for song in album.songs:
                    songs.append(song)
    if User.user_status == ConfigValues.free_user:
        num_of_returned_record = ConfigValues.num_of_items_printed_in_search_for_free_users
    songs = sorted(songs, key=lambda x: x.popularity, reverse=True)[:num_of_returned_record]
    print(list(map((lambda x: x.name), songs)))


def get_album_songs():
    album_name = input("Enter album name: ")
    songs, is_album_exist = SpotifyContent.is_album_exist(album_name)
    if is_album_exist:
        print_sorted(list(map((lambda x: x.name), songs)))
    else:
        print("sorry, album not exist :(")


def print_sorted(music_objects, sep="\n"):
    from user.user import User
    music_objects.sort()
    if User.user_status == ConfigValues.free_user:
        num_of_items_to_print = ConfigValues.num_of_items_printed_in_search_for_free_users
        print(*(music_objects[:num_of_items_to_print]), sep=sep)
    else:
        print(*music_objects, sep=sep)
