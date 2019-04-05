# Dictionary dictionary all the information about
# the city and to which country they belong
cities = {
    'Moscow': {
        'country': 'russia',
        'population': '144,5 million',
        'fact': 'The Kremlin is the residence of the Russian president. On its territory you can visit the Armory.',
        },
    'Minsk': {
        'country': 'belarus',
        'population': '9,508 million',
        'fact': 'On the wide Independence Avenue 15 kilometers long there are museums.',
        },
    'Warsaw': {
        'country': 'poland',
        'population': '38,43 million',
        'fact': 'Here you can see Gothic churches and neoclassical palaces.',
        },
    }

for city, info_city in cities.items():
    print("\nCity: " + city.title())
    country = info_city['country']
    population = info_city['population']
    fact = info_city['fact']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + population.title())
    print("\tFact: " + fact.title())
