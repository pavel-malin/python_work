# 
'''
def make_album(artist_name, album_name):
    if artist_name:
        album = {'artist': artist_name, 'album': album_name}
        return album
    elif album_name:
        album  ={'artist': artist_name, 'album': album_name}
        return album
    else:
        album = {'artist': artist_name, 'album': album_name}
        return album

make = make_album('Fimlsc', 'bront')
print(make)

make = make_album('AAAA', 'AAAAAA')
print(make)

make = make_album('QQQQ', 'QQQQQQ')
print(make)

def make_0album(artist_name='AAAA', album_name='QQQ', number_of_tracks=''):
    album = {'artist': artist_name, 'album': album_name}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

make = make_0album('QQQQQ', 'WWWW')
print(make)

make = make_0album()
print(make)

make = make_0album('WWWW', 'EEEE', number_of_tracks=25)
print(make)
'''

def make_1album(artist_name, album_name):
    album = "\nArtist: " + artist_name + "\nAlbum: " + album_name
    return album.title()

while True:
    print("\nArtist and album:")
    print("(enter 'q' at any time to quit)")
    
    f_artist = input("Artist: ")
    if f_artist == 'q':
        break

    f_album = input("Album: ")
    if f_album == 'q':
        break

    make = make_1album(f_artist, f_artist)
    print(make)