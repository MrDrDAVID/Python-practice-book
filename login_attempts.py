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
        self.login_attempts = 0
    
    def describe_user(self) :
        print('User info: ')
        print(' name: ' + self.first_name + ' ' + self.last_name)
        print(' DOB: ' + self.date_of_birth)
        print(' bio: ' + self.bio)
        print(' location: ' + self.location)

    def greet_user(self) :
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name + ', welcome back.')

    def increment_login_attempts(self) :
        self.login_attempts += 1

    def reset_login_attempts(self) :
        self.login_attempts = 0

first_user = User('Lainey', 'Boo', '04/03/1996', 'I love jalapena, and my boo', 'Buena Park')
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print('The user ' + first_user.first_name + first_user.last_name +
        f'has logged in {first_user.login_attempts} times.')

first_user.reset_login_attempts()
print(f'Login attempts have been reset to {first_user.login_attempts}')