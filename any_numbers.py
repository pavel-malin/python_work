# Favorite number of friends with the conclusion
# if the numbers
any_numbers = {
    'Bob': '6',
    'Tedi': '25',
    'Finar': '13',
    'Any': '93',
    }
print("Favorite number Bob: " + any_numbers['Bob'] +
    "\n" + "Favorite number Tedi: " + any_numbers['Tedi'] +
    "\n" + "Favorite number Finar: " + any_numbers['Finar'] +
    "\n" + "Favorite number Any: " + any_numbers['Any'])

# Simplifying the top example using a dictionary and
# adding favorite numbers of people
any_numbers = {
    'bob': {
        'number': '6',
        'numbers': '11',
        },
    'Tedi': {
        'number': '25',
        'numbers': '22',
        },
    'Finar': {
        'number': '13',
        'numbers': '3',
        },
    'Any': {
        'number': '93',
        'numbers': '3',
        },
    }

for name, number_info in any_numbers.items():
    print("\nFavorite number: " + name.title())
    number = number_info['number'] + ", " + number_info['numbers']
    print("\tNumbers: " + number)