from user_name import Admin, User, Privileges

site_user = User('bob', 'adam', '1')
site_admin = Admin('Adam', 'aaaas', 12)

site_user.user_registration()
site_admin.privileges.bann()
site_user.reset_login_attempts(0)
site_user.greet_user()
site_user.increment_login_attempts(10)
site_user.greet_user()