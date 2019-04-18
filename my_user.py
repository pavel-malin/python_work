from user_name import User
from user_name import Admin, Privileges

site_user = User('bob', 'adam', 1)
print(site_user.describe_user())

site_admin = Admin('Adam', 'aaaas', 12)
site_admin.privileges.show_privileges()