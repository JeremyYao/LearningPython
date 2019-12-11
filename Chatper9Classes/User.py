# 9-3. Users: Make a class called User . Create two attributes called first_name
# and last_name , and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts() . Print login_attempts again to
# make sure it was reset to 0.

class User:

    def __init__(self, first_name, last_name):
        self.first_name = str(first_name).title()
        self.last_name = str(last_name).title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name + "\nLast name: " + self.last_name)

    def greet_user(self):
        print(f"Hello {self.first_name}")

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges , that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class  Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        for priv in self.privileges:
            print(priv)

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges , that stores a list
# of strings like "can add post" , "can delete post" , "can ban user" , and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin , and call your method.
class Admin(User):

    def __init__(self, first_name, last_name, privileges = []):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()


johnCena = User("John", "Cena")
johnCena.describe_user()
johnCena.greet_user()

print("********** 9-5")
for i in range(0,5):
    johnCena.increment_login_attempts()

print(johnCena.login_attempts)
johnCena.reset_login_attempts()
print(johnCena.login_attempts)

print("******ADMIN PRiv stuff")
admin = Admin("Cee", "Jaey", ["Post memes", "IDK", "Everything"])
admin.show_privileges()
admin.greet_user()
