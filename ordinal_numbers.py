# The number in the list goes to the list, then the
# corresponding ending is added
odinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for odinal_number in odinal_numbers:
    if odinal_number in '1':
        price = "st"
        print(odinal_number + price)
    if odinal_number in '2':
        price = "nd"
        print(odinal_number + price)
    if odinal_number in '3':
        price = 'rd'
        print(odinal_number + price)
    if odinal_number in '4':
        price = 'th'
        print(odinal_number + price)
    if odinal_number in '5':
        price = 'th'
        print(odinal_number + price)
    if odinal_number in '6':
        price = 'th'
        print(odinal_number + price)
    if odinal_number in '7':
        price = 'th'
        print(odinal_number + price)
    if odinal_number in '8':
        price = 'th'
        print(odinal_number + price)
    if odinal_number in '9':
        price = 'th'
        print(odinal_number + price)

for odinal_number in odinal_numbers:
    print(odinal_number)

# Check whether number is included
ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

if '1' in ordinal_numbers:
    print("1st")
elif '0' in ordinal_numbers:
    print("0st")
else:
    print("Sorry")

if '2' in ordinal_numbers:
    print("2nd")
elif '10' in ordinal_numbers:
    print("10st")
else:
    print("Sorry")

if '3' in ordinal_numbers:
    print("3rd")
elif '11' in ordinal_numbers:
    print("11st")
else:
    print("Sorry")

if '4' in ordinal_numbers:
    print("4th")
elif '12' in ordinal_numbers:
    print("12st")
else:
    print("Sorry")

if '5' in ordinal_numbers:
    print("5th")
elif '13' in ordinal_numbers:
    print("13st")
else:
    print("Sorry")

if '6' in ordinal_numbers:
    print("6th")
elif '14' in ordinal_numbers:
    print("14st")
else:
    print("Sorry")

if '7' in ordinal_numbers:
    print("7th")
elif '15' in ordinal_numbers:
    print("15st")
else:
    print("Sorry")

if '8' in ordinal_numbers:
    print("8th")
elif '16' in ordinal_numbers:
    print("16st")
else:
    print("Sorry")

if '9' in ordinal_numbers:
    print("9th")
elif '17' in ordinal_numbers:
    print("17st")
else:
    print("Sorry")