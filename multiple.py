# Multiple
multiple = input("See a multiple of 10: ")
number = int(multiple)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " +str(number) + " is odd")