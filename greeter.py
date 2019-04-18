# User enters his name for greeting with him
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# Extension of user information (+=)
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

def greet_user():
    '''Displays a simple greeting'''
    print("Hello!")

greet_user()

def greet1_user(username):
    '''Displays a simple greeting'''
    print("Hello, " + username.title() + "!")

greet1_user('jesse')
greet1_user('sarah')

def get_formatted_name(first_name, last_name):
    """Returns a neatly formatted full name."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Endless cycle!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def get_formatted_0name(first_name, last_name):
    '''Returns a neatly formatted full name.'''
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_0name(f_name, l_name)
    print("\nHellom, " + formatted_name + "!")
