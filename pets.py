# Dictionary dictionary all the information
# about animals and who owns them
pets = {
    'dog': {
        'animal owner': 'Adam',
        'age': '5',
        'color': 'black',
        },
    'cat': {
        'animal owner': 'Dori',
        'age': '2',
        'color': 'white',
        },
    'parrot': {
        'animal owner': 'Firint',
        'age': '59',
        'color': 'yellow',
        },
}

for animal, animal_info in pets.items():
    print("\nAnimal: " + animal.title())
    animal_owner = animal_info['animal owner']
    age = animal_info['age']
    color = animal_info['color']
    print("\tAnimal owner: " + animal_owner.title())
    print("\tAge: " + age)
    print("\tColor: " + color.title())

# 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)