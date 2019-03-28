# Say hello to all users
user_name = ['adam', 'guest1', 'guest2', 'admin', 'fiz']

if user_name:
    for user_names in user_name:
        print("Hello user: " + user_names.title() + ".")
else:
    print("Adding list users")

 
if user_name:
    for user_names in user_name:
        print("Hello user: " + user_names.title() + ".")
else:
    print("We need to find some users!")

# Remove user name
user_name = ['adam', 'guest1', 'guest2', 'admin', 'fiz']
users_del = 'guest1'
user_name.remove(users_del)

if user_name:
    if 'guest1' in user_name:
        print("not delete")
    elif 'guest1' not in user_name:
        print("\nDelete users names: " + users_del)

        user_del = 'guest2'
        user_name.remove(user_del)
    if 'guest2' in user_name:
        print("not delete")
    elif 'guest2' not in user_name:
        print("Delete users names: " + user_del)
    
        user_del = 'adam'
        user_name.remove(user_del)
    if 'adam' in user_name:
        print("not delete")
    elif 'adam' not in user_name:
        print("Delete users names: " + user_del)

        user_del = 'admin'
        user_name.remove(user_del)
    if 'admin' in user_name:
        print("not delete")
    elif 'admin' not in user_name:
        print("Delete users names: " + user_del)

        user_del = 'fiz'
        user_name.remove(user_del)
    if 'fiz' in user_name:
        print("not delete")
    elif 'fiz' not in user_name:
        print("Delete users names: " + user_del)

# Check and username does not exist
user_names = ['Adam', 'Guest1', 'Guest2', 'ADMIN', 'Fiz']

for user_name in user_names:
    if user_name.lower() in 'adam':
        print("Is games names: " + user_name)
    if user_name.lower() in 'guest1':
        print("Is games names: " + user_name)
    if user_name.lower() in 'guest2':
        print("Is games names:" + user_name)
    if user_name.lower() in 'admin':
        print("Is games names: " + user_name)
    if user_name.lower() in 'fiz':
        print("Is games names: " + user_name)

# Compare two user lists
user_names = ['adam', 'guest1', 'guest2', 'admin', 'fiz']
user_guests = ['adam', 'guest1', 'guest2', 'admin', 'fiz', 'bob']

for user_guest in user_guests:
    if user_guest in user_names:
        print("User exists " + user_guest.title() + ".")
    else:
        print("\nSorry, not users, please to register " + user_guest.title() + ".")
print("))))")

# Comparison of two lists of users with different case
# of letters
current_users = ['bob', 'fiz', 'Adam', 'Bib', 'Jon','Bab']
new_users = ['bob', 'fiz', 'adam', 'bib', 'jon', 'bab']

for current_user in current_users:
    if current_user.lower() in new_users:
        print("Username such alredy exists:" + current_user.title() + "\nPlease register with a different name.")


