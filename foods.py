# Copying the list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Add to list copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
# This doesn't work:
my_foods.append('cannoli')
friend_foods = my_foods
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Exercises with copying
my_foods = ['pizzy', 'falafel', 'carrot cake', 'ice']
print("The first three items in the list are:")
for my_food in my_foods[:3]:
    print(my_food.title())
print("\nThe first three items in the list are:")
friend_foods = my_foods[:]
for friend_food in friend_foods[:3]:
    print(friend_food.title())

# Output from the middle of the list
my_foods = ['pizzy', 'falafel', 'carrot cake', 'ice']
print("Three items from the middle of the list are:")
for my_food in my_foods[:3]:
    print(my_food)
friend_foods = my_foods[:3]
print("\nThree items from the middle of the list are:")
for friend_food in friend_foods[:3]:
    print(friend_food)

# Output from the middle of the list
my_foods = ['pizzy', 'falafel', 'carrot cake', 'ice']
print("The last three items in the list are:")
for my_food in my_foods[1:]:
    print(my_food)
friend_foods = my_foods[:4]
print("\nThe last three items in the list are:")
for friend_food in friend_foods[1:]:
    print(friend_food)

# Copying and adding to the list and displaying the result
pizzy_name = ['margarita', 'diabola', 'calzone']
friend_pizzas = pizzy_name[:]
print("My favorite pizzas are:")
pizzy_name.append('capricciosa')
for pizzy_names in pizzy_name:
    print(pizzy_names.title())
friend_pizzas.append('hawaiian')
print("\nMy friend's favorite pizzas are:")
for friend_pizzy in friend_pizzas:
    print(friend_pizzy.title())



