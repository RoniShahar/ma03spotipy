from file import read_config_file


class ConfigValues:
    logs_file_path = read_config_file(parameter='logs_file_path')
    num_of_items_printed_in_search_for_free_users = int(read_config_file(
        parameter='num_of_items_printed_in_search_for_free_users'))
    num_of_top_songs_to_display = int(read_config_file(parameter='num_of_top_songs_to_display'))
    premium_user = read_config_file(parameter='premium_user')
    free_user = read_config_file(parameter='free_user')
    num_of_max_playlists_for_free_user = int(read_config_file(parameter='num_of_max_playlists_for_free_user'))
    num_of_max_songs_in_playlist_for_free_user = int(read_config_file(
        parameter='num_of_max_songs_in_playlist_for_free_user'))
