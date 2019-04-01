# Conclusion of the whole dictionaly,
# conclusion of the dictionary design
glossary = {
    'list': 'title',
    'tuple': 'append',
    'string': 'new string',
    'numbers': 'str',
    'teams': 'if-elif-else',
    }
print(glossary)
print("List: " + glossary['list'] + "\n" + 
    "Tuple: " + glossary['tuple'] + "\n" +
    "String: " + glossary['string'] + "\n" +
    "Numbers: " + glossary['numbers'] + "\n" +
    "Teams: " + glossary['teams'])

# Code reduction with for
glossary = {
    'list': 'title',
    'tuple': 'append',
    'string': 'new string',
    'numbers': 'str',
    'teams': 'if-elif-else',
    }
for name, value in glossary.items():
    print(name.title() + ": " + value)