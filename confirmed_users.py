# We start with lists: users for verification and
# an empty list for storing trusted users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# We check each user, while there are unwired users.
# Each user who passes the test is moved to the list
# of verified ones.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Displays all verified users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)