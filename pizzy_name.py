# List one pizza name
pizzy_name = ['margarita', 'diabola', 'calzone']
for pizzy_names in pizzy_name:
    print(pizzy_names)

# Before each message name
pizzy_name = ['margarita', 'diabola', 'calzone']
for pizzy_names in pizzy_name:
    print("I like pepperoni pizza " + pizzy_names.title())

# Two message posts before each pizza name
pizzy_name = ['margarita', 'diabola', 'calzone']
for pizzy_names in pizzy_name:
    print("I like pepperoni pizza " + pizzy_names.title() + 
       " I really love pizza! " + pizzy_names.title())

# Dispay message in front of pizza name
pizzy_name = ['margarita', 'diabola', 'calzone']
for pizzy_names in pizzy_name:
    print("I like pepperoni pizza " + pizzy_names.title() + ".")

# See all the pizzas you want to order
pizzy_name = "\nSee all the pizzas you want to order."
pizzy_name += "\nTo complete the order 'quit': "
pizza = ""

while pizza != 'quit':
       pizza = input(pizzy_name)

       if pizza != 'quit':
              print(pizza)
