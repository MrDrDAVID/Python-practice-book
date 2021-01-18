magician_names = ['David Blaine', 'Cris Angel', 'Houdini', 'Harry Potter', 'Wutan']

def great_magicians(magicians):
    '''Function that modifies the string in a list'''
    magicians[:] = ['The Great ' + magician for magician in magicians]

def show_magicians(magicians):
    '''Function that prints out all the elements in a list'''
    for magician in magicians:
        print('Please welcome to the stage ' + magician)

print('Before the modification to magician names: ')
show_magicians(magician_names)

great_magicians(magician_names)
print('\nAfter the modification to magician names: ')
show_magicians(magician_names)