boo = {
    'first name': 'Lainey', 
    'last name': 'Boo', 
    'age': 24,
    'city': 'Buena Park',
    }

laineysboo = {
    'first name': 'Laineys',
    'last name': 'boo',
    'age': 24,
    'city': 'Paramount',
}

batman = {
    'first name': 'Bruce',
    'last name': 'Wayne',
    'age': 37,
    'city': 'Gotham City',
}

people = [boo, laineysboo, batman]

for person in people:
    name = person['first name'] + ' ' + person['last name']
    print('\nName: ' + name + 
        '\nAge: ' + str(person['age']) +
        '\nLocation: ' + person['city'])