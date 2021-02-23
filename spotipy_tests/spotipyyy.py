import sys
import spotipy
import spotipy.util as util

username = 'Rubikown'
skip_time = 40
skip_words = ['interlude', 'intermission', 'intro', 'outro']

def show_tracks(tracks):
    """ Looking for tracks which don't fit """
    for i, item in enumerate(tracks['items']):
        track = item['track']

        if track['duration_ms'] // 1000 < skip_time:
            print(f"{i} {track['artists'][0]['name']} {track['name']}")
            continue
        for word in skip_words:
            if word in track['name'].lower():
                print(f"{i} {track['artists'][0]['name']} {track['name']}")
                break


def loved_tracks():
    scope = 'user-library-read'

    auth_manager = spotipy.SpotifyOAuth(scope=scope)
    if auth_manager:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)


def delete_short_tracks():
    scope = 'playlist-modify-public playlist-modify-private'

    auth_manager = spotipy.SpotifyOAuth(scope=scope)
    if auth_manager:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        playlists = sp.current_user_playlists()
        for playlist in playlists['items']:
            print(f"Playlist name: {playlist['name']}; Total tracks: {playlist['tracks']['total']}")
            if playlist['name'] == 'TestPlaylist':
                results = sp.playlist(playlist['id'],
                                      fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
        # if results.name == 'RU':

    else:
        print("Can't get token for", username)


delete_short_tracks()
