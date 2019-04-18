# Concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# Capitalization Concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

# Concatenation  due(message)
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# 
def name(first_name, last_name):
    full_name = "\nHello, " + first_name + ' ' + last_name + "!"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at  any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    names = name(f_name, l_name)
    print(names) 