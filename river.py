# The name of the river and country in
# which it is located using the dictionary
river = {
    'nile': 'egypt',
    'yangzi': 'asia',
    'mississippi': 'north America',
    }

for name, value in river.items():
    print("The " + name.title() + "runs through " + value.title())

# River name
river = {
    'nile': 'egypt',
    'yangzi': 'asia',
    'mississippi': 'north America',
    }
print("Names river:")

for name in river.keys():
    print(name.title())

# The name of the country
river = {
    'nile': 'egypt',
    'yangzi': 'asia',
    'mississippi': 'north America',
    }
print("Names a country:")

for key in river.values():
    print(key.title())
