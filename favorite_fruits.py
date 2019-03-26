# What's on your favorite fruit list
favorite_fruits = ['apples', 'a pineapple', 'cherry', 'strawberry', 'watermelon']

if 'peppir' in favorite_fruits:
    price = 'peppir'
elif 'brikli' in favorite_fruits:
    price = 'brikli'
elif 'mandarin' in favorite_fruits:
    price = 'mandarin'
elif 'apples' in favorite_fruits:
    price = 'apples'
else:
    price = 'not fruits'

print("You really like bannanas! " + str(price).title())