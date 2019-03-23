# Matching cycles for conclusions by age of amounts(if-elif-else)
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("You admission cost is $10.")

# Matching cycles for conclusions by age of amounts(contraction)
age = 12

if age < 4:
    price  = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# Matching cycles for conclusions by age of amounts(with old age)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# Matching cycles for conclusions by age of amounts(without else)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
