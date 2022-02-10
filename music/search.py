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


def get_top_ten_songs_of_artist(num_of_returned_record=10):
    from user.user import User
    artist_name = input("Enter artist name: ")
    songs = []
    for artist in SpotifyContent.artists:
        if artist.name == artist_name:
            for album in artist.albums:
                for song in album.songs:
                    songs.append(song)
    if User.user_status == "f":
        num_of_returned_record = num_of_items_printed_in_search_for_free_users()
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
    from user.user import User
    list.sort()
    if User.user_status == "f":
        num_of_items_to_print = num_of_items_printed_in_search_for_free_users()
        print(*(list[:num_of_items_to_print]), sep=sep)
    else:
        print(*list, sep=sep)


def num_of_items_printed_in_search_for_free_users():
    from file import read_config_file
    return int(read_config_file('properties.properties', 'config', 'num_of_items_printed_in_search'))

