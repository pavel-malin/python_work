# Say hello to all users
user_name = ['adam', 'guest1', 'guest2', 'admin', 'fiz']

for user_names in user_name:
    print("Hello user name:\n" + user_names.title())

# Hello to  admins
user_name = ['adam', 'guest1', 'guest2', 'admin', 'fiz']

for user_names in user_name:
    if user_names in 'admin':
        print("Hello " + user_names.title() + ", would you like to see a status report?")
    else:
        print('Hello ' + user_names.title() + ', thank you for logging in again')