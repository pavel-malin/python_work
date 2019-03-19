# Exercise numbers 1-20
exercise_numbers = []
for value in range(1,21):
    exercise_numbers.append(value)
print(exercise_numbers)

# Exercise numbers 1-1000000
one_mil = []
for value in range(1,1000000):
    one_mil.append(value)
print(one_mil)

# Max, min 1-1000000
print(max(one_mil))
print(min(one_mil))
print(sum(one_mil))

# Odd numbers
odd_num = []
for value in range(1,21,2):
    odd_num.append(value)
print(odd_num)

# Multiple 3
multiple = []
for value in range(3,30,3):
    multiple.append(value)
print(multiple)

# Cubes
cubes = []
for value in range(3,11,3):
    cubes.append(value**2)
print(cubes)

# Cubes 10
cubes = [value**2 for value in range(1,11)]
print(cubes)