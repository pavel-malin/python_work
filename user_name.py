class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.name = first_name + ' ' + last_name
        self.login_attempts = 0

    def describe_user(self):
        long_name = str(self.age) + ' ' + self.name
        return long_name.title()

    def greet_user(self):
        print("Age :" + str(self.login_attempts))

    def reset_login_attempts(self, person):
        if person >= self.login_attempts:
            self.login_attempts = person
        else:
            print("0 person")

    def increment_login_attempts(self, persons):
        self.login_attempts += persons

    def user_registration(self):
        while True:
            print("Re-enter the name if you make a mistake the you see 'q'")
            print("If you entered your name correctly, you can exit by 'exit'")
            users = input("You name: ")
            if users == 'q':
                user.pop(0)
                continue
            if users == 'exit':
                break
            user.append(users)
            print("Thank, " + str(user) + " for registering")

class Privileges():
    def __init__(self, privileges='Adam'):
        self.privileges = privileges

    def show_privileges(self):
        print("Hello Admin: " + self.privileges + "!")
    
    def bann(self):
        while True:
            bann = input("Name user ban list: ")
            if bann == 'q':
                break
            if bann in 'user':
                print(user)
            bann = input("Name user ban: ")
            if bann in user:
                user_bann = user.pop(0)
                bann_user.append(user_bann)
            print("You have the right to ban any user. " + user_bann.title())
            print("Deleting user: " + user_bann.title())

    def message_privileges(self):
        message = input("Add a message to all users? ")
        print(message)

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

    def delete_user(self):
        while True:
             for users in user:
                users = input("Delete name user: ")
                if users == 'q':
                    continue
                if users == 'exit':
                    break
                print("Sorry, you " + users.title() + "deleting Admin")

user = []
bann = []
bann_user = []
site_user = User('bob', 'adam', '1')
site_admin = Admin('Adam', 'aaaas', 12)

site_user.user_registration()
site_admin.privileges.bann()
site_user.reset_login_attempts(0)
site_user.greet_user()
site_user.increment_login_attempts(10)
site_user.greet_user()

'''
site_user = User('bob', 'adam', 19)
site_0user = User('bib', 'histo', 35)
site_1user = User('adam', 'mob', 22)
print("Hello, " + site_user.name.title() + "!")
print("Name: " + site_user.name.title() + "\tAge: " + str(site_user.age))
print("Hello, " + site_0user.name.title() + "!")
print("Name: " + site_0user.name.title() + "\tAge: " + str(site_0user.age))
print("Hello, " + site_1user.name.title() + "!")
print("Name: " + site_1user.name.title() +"\tAge: " + str(site_1user.age))
'''