'''returns a dictionary that holds info about an album'''
def make_album(artist_name, album_name, track_num = ''):
    if track_num:
        album_info = {
            'artist': artist_name,
            'album': album_name,
            'Track Number': track_num,
        }
    else:
        album_info = {
            'artist': artist_name,
            'album': album_name,
        }
    return album_info

terminate = 'continue'
while terminate != 'quit':
    print('type quit to exit loop or follow the prompts')

    artist_name = input('Enter an artist name: ')
    if artist_name == 'quit':
        break

    album_name = input('Enter the album name: ')
    if album_name == 'quit':
        break

    track_num = input('How many tracks does the album have: ')
    if track_num == 'quit':
        break

    album = make_album(artist_name, album_name, track_num)

    print(album)