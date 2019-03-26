# Check whether the list
tests_0 = 'bmw'
tests_1 = 'audi'
tests_2 = 'Mersedes'
tests_3 = 'toyota'
tests_4 = 'nissan'
tests_5 = 'hynda'
tests_6 = 'hyndai'
print("False. tests_0 == 'lada'")
print(tests_0 == 'lada')
print("True. tests_0 == 'bmw'")
print(tests_0 == 'bmw')
print("False. test_1 == 'toyota")
print(tests_1 == 'toyota')
print("True. tests_1 == 'audi")
print(tests_1 == 'audi')
print("False tests_0 == tests_3")
print(tests_0 == tests_3)

# Lower case comparison
print("False. tests_2 == 'nissan'")
print(tests_2.lower() == 'nissan')
print("True. tests_2 == 'mersedes")
print(tests_2.lower() == 'mersedes')
print("True. tests_2 != 'nissan'")
print(tests_2 != 'nissan')

# Number comparison
numbers_0 = 12
numbers_1 = 24
print(numbers_0 >= numbers_1, numbers_0 <= numbers_1,
    numbers_0 == numbers_1, numbers_0 != numbers_1)

# Number comparison (and, or)
numbers_0 = 11
numbers_1 = 59
print(numbers_0 >= numbers_1 and numbers_0 <= numbers_1)
print(numbers_0 == numbers_1 and numbers_0 != numbers_1)
print(numbers_0 >= numbers_1 or numbers_0 <= numbers_1)
print(numbers_0 == numbers_1 or numbers_0 != numbers_1)

# Check whether not included in the list
elements = ['pipi', 'mimi', 'nono']
elements_0 = 'gaga'
if elements_0 not in elements:
    print(elements_0.title() + ' not list')
