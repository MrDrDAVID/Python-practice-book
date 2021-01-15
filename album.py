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

album = make_album('Laineyboo', 'Boos greatest hits', 12)
album2 = make_album('Laineysboo', 'Boo love songs')

print(album)
print(album2)