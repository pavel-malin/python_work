# Conclusion of all information of the
# person in the dictionary
person = {
    'first_name': 'Bob',
    'last_name': 'Djreme',
    'age': '25',
    'city': 'New Year',
    }
print("First names: " + person['first_name'] + "\n" +
        "Last names: " + person['last_name'] + 
        "\n" + "Age: " + person['age'] + "\n" +
        "City: " + person['city'])

# Dictionary in the dictionary with output
# all information
people = {
    'bob': {
        'first_name': 'Bob',
        'last_name': 'Djreme',
        'age': '25',
        'city': 'New Year',
        },
    'adam': {
        'first_name': 'Adam',
        'last_name': 'Babibo',
        'age': '20',
        'city': 'London',
        },
    'bro': {
        'first_name': 'Bro',
        'last_name': 'Firin',
        'age': '15',
        'city': 'Moscow',
        },
    }

for username, user_ifno in people.items():
    print("\nUsername: " + username)
    full_name = user_ifno['first_name'] + " " + user_ifno['last_name']
    age = user_ifno['age']
    city = user_ifno['city']
    print("\tFull name: " + full_name.title())
    print("\tAge: " + age.title())
    print("\tCity: " + city.title())


def build_person(first_name, last_name):
    '''Returns a dictionary with information about a person.'''
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_0person(first_name, last_name, age=''):
    '''Returns a dictionary with information about a person.'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_0person('jimi', 'hendrix', age=27)
print(musician)

