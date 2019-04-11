# Information is stored about people's favorite
# places in the dictionary and where they are
favorite_places = {
    'bob': {
        'city': 'moscow',
        'place': 'tertiary',
        'city1': 'moscow',
        'place1': 'gorky park',
        },
    'adam': {
        'city': 'moscow',
        'place': 'vdnh',
        'city1': 'moscow',
        'place1': 'clean ponds',
        },
    'obo': {
        'city': 'minsk',
        'place': 'nemiga',
        'city1': 'minsk',
        'place1': 'victory Square',
        },
    }

for place, place_info in favorite_places.items():
    print("\nNames: " + place.title())
    city = place_info['city'] + "\t" + place_info['city1']
    place_1 = place_info['place'] + "\t" + place_info['place1']
    print("\tCity: " + city.title())
    print("\tPlace: " + place_1.title())