import json 

def get_stored_username() :
    '''Loads in a username from a file'''
    file_name = 'text-files/username.json'

    try :
        with open(file_name) as f_obj :
            username = json.load(f_obj)
    except FileNotFoundError :
        return None
    else :
        return username

def get_new_username() :
    '''Prompts the user for a username and writes it to a file'''
    file_name = 'text-files/username.json'
    username = input("What is your name? ")

    with open(file_name, 'w') as f_obj :
        json.dump(username, f_obj)
    return username

def greet_user() :
    '''Greet the user by name.'''
    username = get_stored_username()

    if username :
        print('The user that is logged in is ' + username)
        answer = input('Is this correct? (y/n)')

        if answer == 'y' :
            print("Welcome back, " + username + "!")
        else :
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else :
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()