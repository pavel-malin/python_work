def greet_users(names):
    '''Display a simple greeting for each user in the list.'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
username = ['hannah', 'ty', 'margot']
greet_users(username)