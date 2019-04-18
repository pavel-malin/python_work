# 
sandwich_orders = ['croque monsieur', 'croc-madame', 'peanut butter jam sandwich', 'pastrami',
                    'pastrami', 'pastrami', 'pastrami', 'pastrami', 'pastrami',]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your tuna sandwich " + sandwich.title())
    finished_sandwiches.append(sandwich)

print("\nAll made sandwiches:")
for finished_sandwiche in finished_sandwiches:
    print("\t" + finished_sandwiche.title())

while 'pastrami' in finished_sandwiches:
    print("\nDelete is pastrami")
    finished_sandwiches.remove('pastrami')
print("No longer available pastrami:")
print("\t" + str(finished_sandwiches))

def sandwich_show(*toppings):
    print(toppings)

sandwich_show('crique monsieur', 'croc-madame')
sandwich_show('peanut butter jam sandwich', 'pastrami')

def sandwich_0show(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

sandwich_0show('crique monsieur', 'croc-madame')
sandwich_0show('peanut butter jam sandwich', 'pastrami')
sandwich_0show('crique monsieur')
sandwich_0show('pastrami')