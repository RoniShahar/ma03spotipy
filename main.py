from music.file import open_files_in_zip_file
from music.spotify_content import SpotifyContent


def main():
    open_files_in_zip_file('C:/Users/Ronis/Desktop/code/songs.zip')
    x = SpotifyContent.albums
    y = 8

if __name__ == "__main__":
    main()
