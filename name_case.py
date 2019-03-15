# Exercise
# We make a variable and output them with the same names to
# connect them, with a different conclusion from the beginning
# of a capital letter, and all ostolnoe lowercase, all ppercase,
# all lowercase.
message1 = "hello "
message2 = ", would you like to learn some Python today?"
name1 = "eric"
name2 = "ada"
print(message1.title() + name1.title() + message2)
print(message1.title() + name2.title() + message2)
print(message1.upper() + name1.upper() + message2.upper())
print(message1.lower() + name2.lower() + message2.lower())
print(message1.title() + name1.title() + message2.title())
print(message1.title() + name2.title() + message2.title())

# Line break with \n
cits = 'Albert Einstein once said, "A person who never made a\n mistake never tried anything new."'
print(cits)

# Concatenate strings with a line break
famous_person = "Albert Einstein"
message  = '"A person who never made a mistake tried anythng new."'
print(famous_person + message)
print('Albert Einstein once said, "Aperson who never made a\n mistake never tried anything new.')

# tabbed out
print('\tAbert \nEinstein once\tsaid\n,')

# Removing indents from all sides
center = "  center   "
right1 = "      right"
left1 = "left        "
print(center.strip(), center.lstrip(), center.rstrip())
print(right1.strip(), right1.lstrip(), right1.rstrip())
print(left1.strip(), left1.lstrip(), left1.rstrip())
