age = input('How old are you: ')
age = int(age)

while age != 0:
    if age <= 3:
        print('Your ticket is free. Enjoy the movie')
    elif age > 3 and age <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
    age = input('How old are you: ')
    age = int(age)
