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

user1 = User('Laineys', 'boo', '05/11/1996', 'I love my laineyboo so much', 'Paramount')
user1.describe_user()
user1.greet_user()