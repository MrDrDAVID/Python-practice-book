"""Module that contains the User, Admin, and Privileges classes"""

class User() :
    """
    user class made to instantiate user profiles
    """
    def __init__(self, first_name, last_name, date_of_birth, bio, location) :
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.bio = bio
        self.location = location
    
    def describe_user(self) :
        print('User info: ')
        print(' name: ' + self.first_name + ' ' + self.last_name)
        print(' DOB: ' + self.date_of_birth)
        print(' bio: ' + self.bio)
        print(' location: ' + self.location)

    def greet_user(self) :
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name + ', welcome back.')

class Admin(User) :
    """
    A user that has more authoritative attributes than the common user
    """
    def __init__(self, first_name, last_name, date_of_birth, bio, location) :
        super().__init__(first_name, last_name, date_of_birth, bio, location)
        self.privileges = Privileges()

class Privileges() :
    """
    class to represent attributes an admin has over a common user
    """
    def __init__(self, privileges=['ban a user', 'add a post', 'delete a post', 'modify user info']) :
        self.privileges = privileges

    def show_privileges(self) :
        print('An admin can do the following: ')
        for privilege in self.privileges :
            print(' -' + privilege)