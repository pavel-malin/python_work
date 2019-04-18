from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")



"""
# Key output
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# Dictionary name and language output
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

# Dictionary output by name
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

# Output a specific message from the
# list by name in the dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends =['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")

# Conclusion if the name is not in
# the dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Sort dictionary by name
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Enumeration of all dictionary values
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languagues have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Dictionary output without repeating
# the language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following laguages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Displays all names from the dictionary, displays a
# message if there is no name from the list in the
# dictionary. Check dictionary using list
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['jen', 'phil', 'adam', 'gaga']

for name in favorite_languages.keys():
    print("The names: " + name.title())
    if name in friends:
        print("Thank you for participating in the survey " +
        name.title())
if friends[2] not in favorite_languages:
    print("Please participate in the survey " + 
        friends[2].title())
if friends[3] not in favorite_languages:
    print("Please participate in the survey " + 
        friends[3].title())
if 'gaga' not in favorite_languages.keys():
    print("Please participate in the survey Gaga")
if 'adam' not in favorite_languages.keys():
    print("Please participate in the survey Adam")

# Reducing the previous example. Output separately if
# the language was specified one
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
        if 1 >= len(language):
            print(name.title() + "'s favorite language is " + language.title())
"""