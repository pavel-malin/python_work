# Save information about ordered pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Description order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

def make_pizza(*toppings):
    '''List the additions ordered.'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_0pizza(*toppings):
    '''List the additions ordered.'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_0pizza('pepperoni')
make_0pizza('mushrooms', 'green peppers', 'extra cheese')

def make_1pizza(size, *toppings):
    '''Displays  description of the pizza.'''
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_1pizza(16, 'pepperoni')
make_1pizza(12, 'mushrooms', 'green peppers', 'extra cheese')