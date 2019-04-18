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

 
def describe_pet(animal_type, pet_name):
    '''Displays information about the animal'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


def describe_0pet(animal_type, pet_name):
    '''Displays information about the animal'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_0pet(animal_type='hamster', pet_name='harry')
describe_0pet(animal_type='harry', pet_name='hamster')

def describe_1pet(pet_name, animal_type='dog'):
    '''Displays information about the animal'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_1pet(pet_name='willie')
describe_1pet(pet_name='harry', animal_type='hamster')
describe_1pet('willie')
describe_1pet(pet_name='willie')
describe_1pet('harry', 'hamster')
describe_1pet(pet_name='harry', animal_type='hamster')
describe_1pet(animal_type='hamster', pet_name='harry')

# Error
def describe_2pet(animal_type, pet_name):
    '''Displays information about the animal'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_2pet()
